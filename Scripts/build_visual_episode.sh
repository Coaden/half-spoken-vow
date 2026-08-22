#!/usr/bin/env bash

set -euo pipefail

if [[ $# -ne 3 ]]; then
  echo "Usage: $0 AUDIO.mp3 TIMELINE_MAP.md OUTPUT.mp4" >&2
  exit 64
fi

audio_path=$1
map_path=$2
output_path=$3

for command_name in ffmpeg ffprobe perl; do
  if ! command -v "$command_name" >/dev/null 2>&1; then
    echo "Required command not found: $command_name" >&2
    exit 69
  fi
done

if [[ ! -f "$audio_path" ]]; then
  echo "Audio file not found: $audio_path" >&2
  exit 66
fi

if [[ ! -f "$map_path" ]]; then
  echo "Timeline map not found: $map_path" >&2
  exit 66
fi

map_dir=$(cd "$(dirname "$map_path")" && pwd)
audio_duration=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$audio_path")
transition_duration=1
frame_rate=30
ffmpeg_preset=${SERIES_FFMPEG_PRESET:-medium}

declare -a start_seconds
declare -a end_seconds
declare -a image_paths

timestamp_to_seconds() {
  local timestamp=$1
  local minutes=${timestamp%%:*}
  local seconds=${timestamp##*:}
  echo $((10#$minutes * 60 + 10#$seconds))
}

while IFS=$'\t' read -r start_time end_time image_name; do
  start_seconds+=("$(timestamp_to_seconds "$start_time")")
  end_seconds+=("$(timestamp_to_seconds "$end_time")")
  image_paths+=("$map_dir/$image_name")
done < <(
  perl -Mutf8 -CSDA -ne '
    if (/^\|\s*(\d+:\d+)\x{2013}(\d+:\d+)\s*\|.*\|\s*`([^`]+)`\s*\|/) {
      print "$1\t$2\t$3\n";
    }
  ' "$map_path"
)

image_count=${#image_paths[@]}
if (( image_count < 2 )); then
  echo "The map must contain at least two timestamped still-image rows." >&2
  exit 65
fi

for ((index = 0; index < image_count; index++)); do
  if [[ ! -f "${image_paths[$index]}" ]]; then
    echo "Mapped still not found: ${image_paths[$index]}" >&2
    exit 66
  fi

  if (( end_seconds[index] <= start_seconds[index] )); then
    echo "Invalid time range for: ${image_paths[$index]}" >&2
    exit 65
  fi

  if (( index > 0 )); then
    if (( start_seconds[index] != end_seconds[index - 1] )); then
      echo "Timeline gap or overlap before: ${image_paths[$index]}" >&2
      exit 65
    fi
  fi
done

mapped_duration=${end_seconds[$((image_count - 1))]}
duration_difference=$(perl -e 'print abs($ARGV[0] - $ARGV[1])' "$audio_duration" "$mapped_duration")
if ! perl -e 'exit($ARGV[0] <= 1.1 ? 0 : 1)' "$duration_difference"; then
  echo "Map ends at ${mapped_duration}s, but audio is ${audio_duration}s." >&2
  echo "Reconcile the timeline before rendering." >&2
  exit 65
fi

declare -a ffmpeg_inputs
filter_graph=""

for ((index = 0; index < image_count; index++)); do
  hold_duration=$((end_seconds[index] - start_seconds[index]))
  input_duration=$((hold_duration + transition_duration))
  ffmpeg_inputs+=(
    -loop 1
    -framerate "$frame_rate"
    -t "$input_duration"
    -i "${image_paths[$index]}"
  )

  filter_graph+="[$index:v]scale=1920:1080:force_original_aspect_ratio=increase,"
  filter_graph+="crop=1920:1080,"
  filter_graph+="zoompan=z='min(zoom+0.000025,1.04)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
  filter_graph+="d=$((input_duration * frame_rate)):s=1920x1080:fps=$frame_rate,"
  filter_graph+="setsar=1,format=yuv420p[v$index];"
done

current_label="v0"
for ((index = 1; index < image_count; index++)); do
  next_label="mix$index"
  transition_offset=${start_seconds[$index]}
  filter_graph+="[$current_label][v$index]xfade=transition=fade:duration=$transition_duration:offset=$transition_offset[$next_label];"
  current_label=$next_label
done
filter_graph+="[$current_label]format=yuv420p[video_out]"

audio_input_index=$image_count
output_dir=$(dirname "$output_path")
mkdir -p "$output_dir"
temporary_base=$(mktemp "${TMPDIR:-/tmp}/series-visual-render.XXXXXX")
rm -f "$temporary_base"
temporary_output="${temporary_base}.mp4"

cleanup_temporary_output() {
  rm -f "$temporary_output"
}

trap cleanup_temporary_output EXIT

echo "Rendering $image_count stills over ${audio_duration}s of audio..."
ffmpeg -hide_banner -y \
  "${ffmpeg_inputs[@]}" \
  -i "$audio_path" \
  -filter_complex "$filter_graph" \
  -map "[video_out]" \
  -map "$audio_input_index:a:0" \
  -c:v libx264 \
  -preset "$ffmpeg_preset" \
  -crf 18 \
  -profile:v high \
  -level 4.1 \
  -pix_fmt yuv420p \
  -c:a aac \
  -b:a 192k \
  -ar 48000 \
  -movflags +faststart \
  -t "$audio_duration" \
  -shortest \
  "$temporary_output"

mv -f "$temporary_output" "$output_path"
trap - EXIT
echo "Created: $output_path"
