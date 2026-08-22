---
name: series-visual-storyboard
description: Build a CapCut-ready visual beat sheet and AI image prompts from an episode and its finished audio runtime. Use when creating still-image or limited-motion YouTube visuals for a narrated episode, including timestamped image-generator prompts.
---

# Visual Storyboard

Read the complete supplied episode before planning visuals. Build a restrained cinematic slideshow that supports the narration rather than illustrating every sentence.

## Inputs

Use the supplied:

- Episode text
- Finished audio runtime, if available
- Any current character visual references or approved cover art
- Any updated canon from `WorldState/BookCodex.json`, `WorldState/VisualBible.md`, and `WorldState/ContinuityLedger.json`

If a runtime is not supplied, estimate it at approximately 145 spoken words per minute and clearly label all times as estimates.

## Visual pacing

Use roughly one new still every 28–38 seconds. Treat this as a planning average, not a rigid timer.

For a typical 8–12 minute episode, produce 16–24 stills. An episode near 11 minutes should usually use about 20–22 stills. Fewer than roughly 15 stills across 11 minutes reads as static on video platforms.

Allow a strong image to hold for 40–50 seconds during quiet, reflective, or sustained dialogue passages when the composition continues to support the narration. Use quicker 15–30-second changes around major reversals, physical discoveries, setting changes, action, or cliffhangers. Balance these variations so the episode-wide average remains near 28–38 seconds per still.

Do not make a new image for every line of dialogue. Let a strong image hold while dialogue plays over it.

Reserve actual generated motion/video clips for major moments only, usually zero to three per episode. The default deliverable is still-image prompts.

## Continuity rules

Preserve established visual canon from `WorldState/VisualBible.md`. Do not let a generic image model redefine a character.

Maintain one approved character brief per recurring character in the visual bible, and paste it verbatim into every prompt that includes that character. Use the project's locked base style prompt, also recorded in the visual bible, unless the episode calls for a justified variation. The base style should fix genre, period, setting, materials, lighting, mood, `widescreen 16:9`, and `no lettering, no logos, no watermark`.

Never place readable dialogue, titles, episode numbers, logos, or invented UI text inside generated images.

Do not add characters, action, technology, or locations that are not supported by the episode text or established canon.

## Workflow

1. Identify the opening hook, setting-establishing beat, key dialogue reversals, physical discoveries, emotional turns, and final hook.
2. Select 16–24 images using the pacing rule, normally targeting 20–22 images for an episode near 11 minutes.
3. Divide the finished runtime into rough visual holds. Align image changes with story beats, not exact equal intervals.
4. Make the final visual hold longer when the ending hook needs time to land.
5. Write prompts that are specific enough to generate the pictured moment, but not so overloaded that the image model loses the composition.

## Required output

Begin with:

- Episode title
- Audio runtime
- Recommended still count
- One reusable visual-baseline prompt
- Optional recommendation for zero to three motion clips, only if genuinely useful

Then provide a Markdown table with these columns:

| Track time | Suggested hold | Story beat | Image prompt |

Use timestamps in `M:SS–M:SS` form. Write every image prompt as a complete, paste-ready prompt for the chosen image model. Include the base visual style and needed character details in each prompt, or tell the user to append the visual-baseline prompt to every row.

Conclude with a short CapCut assembly note:

- Place the exported chapter audio on the primary timeline.
- Put each still above it at the listed timestamps.
- Use subtle slow push-ins, pans, or dissolves; avoid flashy transitions.
- Keep narration untouched.
- Hold the final image through the final sentence and add two to four seconds of silence only if the ending benefits from it.

## Still timeline map

When the stills are generated, save them to `Assets/Stills/B1E##/` and record a `B1E##_Still_Timeline_Map.md` in that folder. The render skill and the book build script both read that map, so give every row a start time, an end time, and the image filename in backticks, with continuous non-overlapping coverage from `0:00` to the audio duration.

## Quality check

Before delivering, verify:

- The number of stills matches the runtime.
- The average visual hold is approximately 28–38 seconds, with longer or shorter holds justified by the scene rather than convenience.
- Every major plot beat is represented.
- No invented visual contradicts canon.
- Recurring characters match their approved visual-bible descriptions.
- Prompts are widescreen 16:9 and contain no title text.
- The last image supports the episode's cliffhanger rather than resolving it visually.
