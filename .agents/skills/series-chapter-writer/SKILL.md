---
name: series-chapter-writer
description: Write immersive, publication-ready release episodes or macro chapters from the approved episode map, optimized for Pocket FM single-narrator text upload, psychological realism, concrete payoffs, and sharp end hooks. Use when asked to draft, continue, revise, or polish an episode, chapter, or scene.
---

# Episode and Chapter Writer

Default to the mapped short release episode, not a full macro chapter, unless the user explicitly requests a chapter-length manuscript.

## Required source review

1. Read `AGENTS.md` completely.
2. Read `WorldState/BookCodex.json` and every canonical file it points to.
3. For every Book One request, read `WorldState/BookOneEpisodeMap.json` and `WorldState/Book-One-Storyline.md` completely before drafting. The JSON owns the release-episode packet; the Markdown owns the macro chapter and book context. Use both, including neighboring episode boundaries, so a draft neither contradicts the chapter arc nor consumes a later episode's payoff.
4. For later books, read the complete episode map and macro storyline declared in `BookCodex.json` → `authority.episode_map` and `authority.macro_storyline` before drafting. Do not assume Book One's paths remain current after the authority pointers move.
5. Read `WorldState/AudioProductionBible.json` for voices, addresses, pronunciation, spoken-text normalization, and sound rules.
6. Read `WorldState/WritingStyle.md` completely before drafting. It governs register, sentence craft, the interiority budget, ending discipline, and the integrity pass.
7. Read relevant entries in `WorldState/ContinuityLedger.json`.
8. Read `Example Writing and Dialogs` in full before drafting prose. Use its rhythm and dialogue behavior only, never its content as canon.
9. If finished episodes already exist, sample the most relevant past episodes before drafting: always inspect the immediately neighboring episode or episodes, then sample earlier episodes featuring the requested viewpoint and principal speaking characters. Use them to preserve established narration, dialogue cadence, attribution habits, and scene-to-scene continuity. Past episode prose is a style reference, not a canon authority; `WorldState/WritingStyle.md`, live WorldState, and the current episode map take precedence whenever they differ.
10. Apply `.agents/skills/narrative-causal-continuity/SKILL.md` before drafting. Establish the requested episode's character entry state and causal trigger from finalized prose and the causal sections of `ContinuityLedger.json`; never use the map itself as the missing cause.

If the requested episode lacks a mapped point of view, progression, payoff, or end hook, stop and ask one concise question rather than inventing a conflicting episode.

**Know where you are in the arc.** Check the episode's `movement` and the arc's position in
`BookCodex.json` → `arc_architecture`. A movement-one episode establishes; a movement-five episode
converges and pays off. An episode in the final movement may not open a new book thread, and an episode
anywhere may not consume a later episode's payoff. If the map shows a thread closing in this episode,
close it on the page — do not defer it.

## Canon and voice constraints

- Use live WorldState facts over pasted or remembered material.
- Honor every locked entry in `canon_rules` and in the `AGENTS.md` canon guardrails.
- Keep each principal's voice distinct in the spoken channel, following the production bible's address policy.
- Lock narration to the mapped viewpoint. Reveal only what that character senses, infers, remembers, or misunderstands.
- Build the world through labor, fatigue, weather, texture, cost, cramped or grand space, and the delay between wanting help and getting it.
- Use humor only to ground pressure, never to defuse it.

## Short-episode workflow

1. Aim for the mapped duration and word band recorded in the codex — currently 10–12 minutes and 1,650–1,800 spoken words. Never deliver a Pocket FM episode source below the hard minimum of 1,000 words, and never pad to reach a target: see the integrity pass.
2. Begin on the mapped disturbance within the first 30–60 seconds. Do not open with a general recap.
3. Center one dominant episode question. Six foreground speaking voices is a hard ceiling, not a target; two or three is preferred when the scene's work is between two people, and a two-hander must never be padded with bystanders to reach a count.
4. Write connected scenes in which each changes the situation, a relationship, or listener understanding.
5. Deliver the mapped concrete payoff before the closing hook.
6. Make every essential reveal audible. Convert written or visual information into spoken reading, an overheard exchange, a sound at a threshold, or another varied sound-native action.
7. Use silence only after the listener understands what happened.
8. Escalate during the final 200–300 words toward the exact mapped hook and end sharply. Honor the mapped turn type — not every episode ends on a cliffhanger, but every episode ends on a state change.
9. Do not consume a later episode's payoff or answer a protected mystery.
10. After drafting, run the causal exit-state audit from `narrative-causal-continuity`: record knowledge, belief, obligation, relationship, emotional, material, and decision changes, then verify that the next mapped episode follows from them. If the user requested report-only work, do not rewrite prose.

## Pilot and batch calibration

When beginning a new arc, production batch, voice configuration, or materially changed episode format, validate the workflow with one episode before drafting the batch:

1. Draft the first mapped episode as finished prose at the current editorial word target.
2. Run a focused continuity, audio-legibility, pacing, payoff, and end-hook pass on that episode.
3. After the prose is approved, create a clean Pocket FM upload master when production output is requested: continuous prose, ordinary dialogue punctuation, and no Markdown syntax, labels, production notes, or bracketed sound cues.
4. Obtain an actual runtime from Pocket FM's preview using the selected narrator, or from a representative read when preview timing is unavailable, before drafting far ahead. Do not estimate batch pacing from word count alone.
5. Use the measured delivery rhythm, necessary pauses, and performance density to calibrate subsequent episodes. Preserve mapped story boundaries and canon; record any approved production-target change in `WorldState/AudioProductionBible.json` and `WorldState/CHANGELOG.md`.

For later episodes in a calibrated batch, repeat the editorial and audio-legibility pass but do not require a new timing pilot unless the narrator, platform rendering, script format, or pacing target materially changes.

## Pocket FM upload output

- Default to finished editorial prose while drafting. After approval, create the upload master only when requested.
- Optimize the primary upload for the single selected narrator recorded in `AudioProductionBible.json`. Favor natural conversational flow without weakening tension or clarity.
- Keep narration and dialogue in continuous prose. Use clear attribution, character-specific wording, cadence, and context because separate character voices are unavailable.
- Remove Markdown syntax, speaker labels, production notes, and bracketed sound cues from the upload master.
- Put the episode title in Pocket FM's title field and repeat it as the upload body's first plain-text line so the narrator speaks it. Use `Episode [spoken number]: [Title]` with the **platform** episode number spelled out — the Pocket FM feed counts continuously and does not restart with a new book, so `B2E01` is spoken as `Episode Sixty-One`. Add one paragraph break and begin the cold open immediately without recap.
- Spell out all numerals, clock times, decimals, measurements, symbols, abbreviations, and all-caps display text as they should be spoken.
- Follow the production bible's names and pronunciations. Avoid dialogue that depends on typography.
- Render necessary sound through prose rather than production cues.
- Create separated narration and speaker blocks only when the user explicitly requests an external multi-voice adaptation.

## Episode file conventions

Save approved episode prose as `Assets/<Book Name>/Episodes/B#E##-Title-In-Kebab-Case.md` — Book One's
episodes live in `Assets/Book One/Episodes/B1E01-...`, Book Two's in `Assets/Book Two/Episodes/B2E01-...`.
Begin each file with a single heading in the form `# Episode Seven: The Title`, using the **canonical**
arc-scoped number in the file name and heading. `Scripts/build_book_pdf.py` parses both the heading and
the filename pattern, so keep them exact. Full naming rules are in `BookCodex.json` → `file_conventions`.

## Writing for both formats

Every episode ships twice: as a serial installment and as part of a book. Two consequences for drafting.

**The chapter layer is the book's structure.** The episode map groups episodes under macro chapters, and
that grouping does nothing for the serial — a Pocket FM listener never sees it. At assembly it becomes the
ebook's table of contents, with two or three episodes forming each chapter. So episodes inside one chapter
anchor should read as continuous scenes of a single chapter when set end to end: avoid re-establishing
setting or restating a situation the previous episode just left, because in the book version there is no
gap between them. Where an episode must orient a returning listener, do it through present-tense action
that a continuous reader will experience as momentum rather than repetition.

**No serial scaffolding in the prose.** Never write "previously," "as you'll remember," or any recap
addressed to a listener who paused. Refresh a standing threat through dialogue, action, or consequence
instead — which reads correctly in both formats. The same discipline that keeps the serial from sounding
like a soap opera is what makes the book assemble cleanly.

## Readiness check

Verify canon, point of view, character distinction, audio legibility, the 1,000-word hard minimum, word target, concrete payoff, exact end hook, and episode boundary.

Treat a blocking causal-continuity gap exactly like a missing mapped payoff: stop before finalizing prose and report it. A scene cannot be ready when it assumes knowledge, motive, standing, obligation, emotion, or a rule that no prior scene created. Productive mysteries and safe reader-inference gaps remain valid when classified and tracked.

Then run the integrity pass in `WritingStyle.md` section sixteen. It targets the failure modes that
survive a first draft because they sound like prose: self-canceling clauses, fragment stacking,
restatement disguised as emphasis, characters explaining what they already know, cute repeated
identifiers, accidental echoes, AI-shaped rhetoric, and — most detectable of all — passages written to
reach a word count. If a passage was added for length, it is the passage where nothing changes. Cut it
and find a real beat instead.

If the episode is the last of an arc, verify book-level closure separately: the arc's principal question
answered, its primary conflict resolved, its emotional arc paid, a real denouement present, and any hook
for the next book placed **after** the resolution rather than in place of it. Do not change WorldState merely because a draft introduces an idea; update canon only after author approval.
