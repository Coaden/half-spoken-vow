# The Half-Spoken Vow

Private creative-production repository for *The Half-Spoken Vow*, a contemporary romantasy series by Troy Locke. The project maintains one canon-controlled manuscript for episodic audio publication and self-contained ebook and audiobook volumes.

## Start here

Work top-down — each step's decisions are inputs to the next.

1. **`AGENTS.md`** — project-wide creative, canon, production, and workflow instructions. Everything downstream reads this file first.
2. **`WorldState/BookCodex.json`** — series, setting, characters, canon rules, story engines, and the mysteries that stay unresolved.
3. **`WorldState/Book-One-Storyline.md`** — the macro arc, as 20–24 chapters with want / obstacle / change / consequence.
4. **`WorldState/BookOneEpisodeMap.json`** — expand each chapter into 2–3 release episodes with a payoff and an exact end hook.
5. **`WorldState/AudioProductionBible.json`** — narrator, pronunciations, address policy, and spoken-text rules, before drafting prose.
6. Draft episodes into `Assets/Book One/Episodes/B1E##-Title.md`, one pilot first, then calibrate against measured runtime.

## Skills

| Skill | Use it to |
| --- | --- |
| `series-novel-architect` | Plan or restructure seasons, chapter spines, and episode maps |
| `series-chapter-writer` | Draft and revise release episodes and upload masters |
| `series-visual-storyboard` | Build timestamped still-image beat sheets and prompts |
| `series-visual-render` | Render stills plus narration into a CapCut-ready MP4 |

## Scripts

- `Scripts/build_book_pdf.py` — assemble episodes into a PDF or EPUB via Calibre. Set `SLUG`, `TITLE`, and `AUTHOR` at the top of the file.
- `Scripts/build_visual_episode.sh` — build `AUDIO.mp3 + TIMELINE_MAP.md → OUTPUT.mp4`. Requires `ffmpeg`, `ffprobe`, and `perl`.

## Conventions

- Episode IDs are `B1E##` and are stable forever once published.
- Episode files are `Assets/Book One/Episodes/B1E##-Title-In-Kebab-Case.md`, opening with `# Episode Seven: The Title`.
- Stills live in `Assets/Stills/B1E##/` beside a `B1E##_Still_Timeline_Map.md`.
- Any approved canon or production change updates the owning WorldState file **and** `WorldState/CHANGELOG.md` in the same task.
- Binary-asset storage and release-artifact policy is recorded in `docs/asset-storage-policy.md`.

## Privacy

This repository contains an unpublished manuscript and private production material. Keep the GitHub repository private unless the author explicitly decides otherwise.
