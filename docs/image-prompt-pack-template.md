# Image Prompt Pack — Template

Paste-ready structure for handing one episode's storyboard to an image generator (Google Labs Flow, or any comparable model). Fill it from the storyboard skill's output, then paste the whole document into the generator.

---

Develop a storyboard, generating one image for every Track time prompt.

# Visual baseline

Append this baseline to every image prompt:

> `<TODO: paste the base style prompt from WorldState/VisualBible.md, plus the locked character briefs for everyone appearing in this episode. Name each character explicitly and forbid unsupported demographic or wardrobe invention.>`

## Visual timeline and prompts

| Track time | Suggested hold | Story beat | Image prompt |
| --- | --- | --- | --- |
| 0:00–0:32 | 32 sec | `<TODO: beat>` | `<TODO: complete paste-ready prompt for this moment>` |

## Continuity controls

Add the episode-specific prohibitions that would otherwise be invented by the model:

- `<TODO: how a vulnerable or non-consenting character must never be depicted>`
- `<TODO: which objects or places are ordinary and must not be rendered as glowing or magical>`
- `<TODO: what ambiguity must remain visually unresolved>`
- Do not show readable text, credentials, coordinates, notes, or invented displays.

---

When image generation is finished, return a table of generated filenames and descriptions matching each track time.

Save the results to `Assets/Stills/B1E##/` and write `B1E##_Still_Timeline_Map.md` in that folder with continuous, non-overlapping rows from `0:00` to the audio duration, each naming its image file in backticks. The render script validates that map before building the MP4.
