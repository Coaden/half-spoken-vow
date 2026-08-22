---
name: series-visual-render
description: Render a still-image episode into a CapCut-ready MP4 from an episode's MP3, stills folder, and Markdown timeline map. Use when building or rebuilding a narrated visual episode from `Assets/Stills/B1E##`, `Assets/MP3/B1E##-*.mp3`, and `B1E##_Still_Timeline_Map.md`.
---

# Visual Render

Create an importable, editable-in-CapCut MP4 master from the approved stills and map. This produces an MP4, not a native CapCut project; keep the source stills and Markdown map as the editable timing source of truth.

## Inputs and output

For episode `B1E##`, require:

- One audio file matching `Assets/MP3/B1E##-*.mp3`.
- A stills folder at `Assets/Stills/B1E##/`.
- A map at `Assets/Stills/B1E##/B1E##_Still_Timeline_Map.md`.

Render to `Assets/MP4/<audio-basename>.mp4`. For example, use `Assets/MP3/B1E02-Episode-Title.mp3` to produce `Assets/MP4/B1E02-Episode-Title.mp4`.

Use the case-sensitive project renderer at `Scripts/build_visual_episode.sh`.

## Preflight

Before rendering:

1. Confirm exactly one matching MP3 exists.
2. Confirm the stills folder and its Markdown map exist.
3. Confirm every JPEG in the stills folder is referenced exactly once in the map, ignoring non-image files such as `.DS_Store`.
4. Confirm the map rows are continuous from `0:00`, contain no gaps or overlaps, and end within one second of the MP3 duration.
5. Do not overwrite an existing output MP4 without the user's explicit direction. Report the existing path and ask whether to replace it or choose a distinct output name.

The renderer independently verifies mapped files, timing continuity, and audio/map duration agreement. Fix a failed preflight or renderer validation before attempting a render.

## Render

Run:

```bash
Scripts/build_visual_episode.sh \
  "Assets/MP3/B1E##-Episode-Title.mp3" \
  "Assets/Stills/B1E##/B1E##_Still_Timeline_Map.md" \
  "Assets/MP4/B1E##-Episode-Title.mp4"
```

The renderer creates a 1920 by 1080, 30-frame-per-second H.264/AAC MP4 with subtle push-ins and one-second dissolves. It copies no additional music, sound effects, captions, title cards, or branding into the master. Preserve the approved narration and mapped still timing.

## Verify and hand off

After rendering:

1. Use `ffprobe` to confirm H.264 video, AAC audio, 1920 by 1080 resolution, and a duration matching the MP3 within one second.
2. Decode the completed MP4 with FFmpeg and require no errors.
3. Inspect representative frames, including at least one transition and the final hook, for correct aspect ratio, readable composition, and no unexpected black tail.
4. Report the MP4 path, duration, resolution, codecs, and file size.
5. State that the MP4 is ready to import into CapCut for optional captions, titles, or hand-tuned visual adjustments; retain the map and JPEGs for any timing or image substitutions.
