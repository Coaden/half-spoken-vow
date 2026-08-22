---
name: series-novel-architect
description: Architect canon-faithful books, arcs, and serial episode maps for a hybrid publishing model — a continuing episodic serial for platforms such as Pocket FM, and the same material as self-contained books for ebook and audiobook distribution. Use when asked to plan, restructure, outline, pace, extend, or revise a book, arc, movement, chapter spine, release-episode map, character arc, mystery progression, thread ledger, or retention runway.
---

# Serial Architect

Convert the literary macro arc into short, cumulative, audio-native episodes that also assemble into
complete, satisfying books — without sacrificing psychological realism or mystery discipline.

## The hybrid publishing model

Every episode you plan has two jobs, and neither is optional.

1. **As a serial installment** it must earn the next tap: a real event, a change, forward momentum.
2. **As part of a book** it must occupy a defined position inside a ~50-episode arc that resolves.

The unit of *publication* is the episode. The unit of *story* is the book. When those two pull against
each other, the book wins, because a serial that never closes anything cannot be sold as a book, while
a book made of strong episodes can always be sold as a serial.

**A reader who buys only one book must feel they received a complete story.** That is the standard.

## Required source review

1. Read `AGENTS.md` completely.
2. Read `WorldState/BookCodex.json` and every canonical file it points to, including `arc_architecture`.
3. Read the authoritative macro storyline path declared in `WorldState/BookCodex.json`.
4. Read the current episode map, `WorldState/ContinuityLedger.json`, and `WorldState/AudioProductionBible.json` when present.
5. Read `WorldState/WritingStyle.md` before planning any beat that depends on voice or register.
6. Read `Example Writing and Dialogs` only when assessing voice. Style reference, never canon.

If the codex still contains unresolved `<TODO: …>` markers that the requested work depends on, stop and
ask one concise question rather than inventing canon.

## Authority and conflict handling

- Use live WorldState files over pasted copies, old drafts, or prior chats.
- Preserve every locked entry in the codex's `canon_rules` and in the `AGENTS.md` canon guardrails.
- Flag a true canon conflict before proceeding. Resolve ordinary planning gaps with the strongest canon-compatible choice.

## Arc architecture — the book is the unit of story

Organize the continuing series into major arcs of approximately **fifty episodes**. Each arc is a
**book**.

    Episodes 1–50     Book One
    Episodes 51–100   Book Two
    Episodes 101–150  Book Three

Fifty is the planning target. A boundary may shift when narrative necessity genuinely demands it —
record any deviation and its reason in `arc_architecture` — but do not drift casually, and never extend
an arc simply because the material has not converged. Failure to converge is a planning failure, not a
reason to move the finish line.

**Terminology:** in this project *book*, *arc*, and *season* denote the same unit. Do not introduce a
second unit of that scale. Where legacy fields say "season," read "book."

### Book-level closure is mandatory

The final episode of an arc is not another serial installment and not a batch boundary. By the end of
each arc:

- the arc's principal dramatic question is answered;
- the primary conflict introduced for this arc reaches meaningful resolution;
- the principal emotional arc receives its payoff;
- promises made specifically by this book are fulfilled;
- the audience gets a genuine climax, a denouement, and the felt sense of completion.

The **series** does not end. Relationships, mythology, political conflict, worldbuilding, and future
threats continue. What must not continue is the arc's own central question.

### The four thread classes

Classify every thread you open. Record the class in the episode map. This is the single most important
discipline in this document.

| Class | Span | Obligation |
| --- | --- | --- |
| **Episode thread** | 1–2 episodes | Propels the listener into the next installment. Resolves almost immediately. |
| **Movement thread** | 5–15 episodes | A conflict inside one movement of the current book. Resolves inside the book, usually inside its movement. |
| **Book thread** | the arc | **Must substantially resolve by the end of this arc.** These are the book's promises. |
| **Series thread** | multiple books | Deliberately designed to survive. Gated in the codex's `do_not_resolve_yet` with an earliest book. |

**Never promote a Book thread to a Series thread in order to prolong the serial.** If an arc approaches
its final movement with a Book thread unresolved, resolve it — do not reclassify it. Reclassification
is only legitimate when the *story* has genuinely revealed the question to be larger than the book, and
it requires an explicit author decision and a CHANGELOG entry, never a quiet edit.

The reverse error also matters: a Series thread must not be accidentally resolved to tidy up a finale.
Each protected question instead pays a **partial instalment per book** — one proven fact, never a tease.

## Five-movement book architecture

Default planning model. Divide each arc into five movements of roughly ten episodes.

| Movement | Episodes | Work |
| --- | --- | --- |
| **One** | 1–10 | Setup, disruption, the book's central dramatic question, establishment of its conflict. |
| **Two** | 11–20 | Escalation, complication, relationship development, rising cost and commitment. |
| **Three** | 21–30 | Major reversal, revelation, or midpoint transformation in how the characters understand the conflict. |
| **Four** | 31–40 | Consequence and convergence. Pressure intensifies, alternatives disappear, threads begin colliding. |
| **Five** | 41–50 | Final escalation, climax, consequence, emotional payoff, denouement. |

Scale proportionally for a longer or shorter arc — a sixty-episode book runs five movements of twelve.

This is a structural guide and not a formula. Stories breathe differently, and a movement may run long
or short. What must hold is the *sequence of functions*: no book may reach movement five without a
midpoint reversal behind it, and no book may spend movement five opening material.

### Convergence discipline

From the start of movement four, **converge**. Stop proliferating.

- Open no new Book thread after movement four begins. Episode threads remain fine.
- Entering the final movement, every Book thread must have a named episode where it closes.
- Audit the thread ledger at the movement three/four boundary. That is the checkpoint.
- If the count of open Book threads exceeds what the remaining episodes can dramatize, cut threads then, deliberately, in the map — not later, in exposition.

**Do not discover at episode forty-eight that twelve Book threads are open and solve them in a speech.**
That failure is always visible ten episodes earlier to anyone who looks, so look.

## Book transitions

The last episode of an arc closes the story. The first episode of the next arc begins a book.

The new arc needs a fresh dramatic engine: a new central problem, changed circumstances, a new threat,
a new relationship problem, consequences arising from the previous book, an expansion of the world, or
another major question the continuing series has earned.

Continuity stays strong. Characters remember. Relationships keep their development. Consequences
persist. But the opening of Book Two must not read as episode fifty-one of a five-hundred-episode
serial that happened to be exported into a second file. **It must read as Book Two.**

Design the first movement of every arc to work for two audiences at once: someone continuing, and
someone starting here. Achieve that through dramatized present-tense need rather than recap. A new
listener should understand the situation because it is *happening*, not because they were briefed.

## Ending philosophy

A book ending may carry a hook for the next book — **after** the current book has delivered its promised
resolution.

**Correct:** the protagonists resolve the book's central threat, make the decisive emotional choice,
absorb the immediate consequences, and reach a new equilibrium. Then, often in the final scene, something
suggests the next problem.

**Wrong:** the climax begins in the penultimate episode and the last episode ends on a stranger in a
doorway and the words *end of Book One*. That is a serial cliffhanger wearing a book ending's clothes.
Do not do it.

The distinction is load-bearing: a hook placed *after* resolution is an invitation, and a hook placed
*instead of* resolution is a debt.

## Episode design

Every episode must still work as a compelling installment. Each needs an immediate objective or
dramatic movement, a change between its first and last line, progression of character or relationship
or conflict or mystery or world, enough substance to justify its existence, and momentum into the next.

**Serial fiction does not mean every episode ends on a cliffhanger.** Vary the closing turn across:
revelation, decision, reversal, emotional turn, discovery, consequence, an unanswered question, a new
objective, an earned cliffhanger, and the quieter compelling transition.

What every ending owes is a **state change** — a status, standing, obligation, or fact that is different
than it was. That is the floor. The cliffhanger is one instrument among ten, not the floor itself.

Avoid the machinery of shock ending, immediate defusal, fresh shock ending. It trains an audience to
stop believing the shock.

## Architecture workflow

1. Preserve the macro chapters as anchors unless the user changes them.
2. Split the macro arc into short release episodes, roughly 2–3 per macro chapter, and record the arc total in the episode map.
3. Honor the word and duration band recorded in the codex. Treat it as an editorial planning range unless a platform requirement makes it binding, in which case say so in the map.
4. Give each episode one dominant question, a payoff, an earned final turn, and no more foreground voices than the codex's ceiling.
5. Open on concrete pressure. Avoid recap-led openings.
6. Build 4–6 episode mini-arcs with local setup, escalation and payoff. Do not postpone all satisfaction to the finale.
7. Design the opening movement as an acquisition runway: establish the protagonist and their misbelief, the central relationship and its cost, the world's rules and their limits, the human conflict that is not about the supernatural, and an escalating reason to continue.
8. Keep protected information constrained. Whatever the story's oracle-shaped element is, it stays fragmentary, unsolicited, and incapable of answering arbitrary questions.
9. Vary sound-native reveal channels. Never make a silent visual the only carrier of a major beat.
10. Escalate each recurring threat rather than replaying it; every reuse needs a new consequence or an irreversible change.
11. Resolve the arc's central crisis and the protagonist's primary internal arc for this book, while preserving the series questions gated in `do_not_resolve_yet`.
12. Assign every episode a movement, and every thread a class. An episode with no movement and a thread with no class are both planning defects.

## Character architecture

- Make the protagonist's flaw active: name the misbelief they must abandon, and give it a cost in nearly every mini-arc.
- Give the protagonist a **book-scoped** internal arc that completes, distinct from any series-scoped growth that continues.
- Treat the protagonist's closest ally as a person with their own stakes, not an advice dispenser.
- Give each recurring character a distinct duty and consequence. Retain the ensemble while limiting foreground voices per episode.
- Ensure at least one supporting character challenges a lead's judgment about the central relationship or the power they are claiming, and that the challenge costs something.
- Use the address and pronunciation policies from the production bible to prevent spoken-channel confusion.

## Required episode-map schema

For each release episode provide:

- stable episode ID, macro chapter ID, **arc/book ID**, and **movement number**;
- title, point of view, location, and foreground characters;
- cold open;
- emotional or physical pressure;
- scene progression;
- concrete payoff;
- exact end hook, and its **turn type** (revelation, decision, reversal, emotional turn, discovery, consequence, open question, new objective, cliffhanger, transition);
- sound-native reveal channel;
- continuity facts established or changed;
- **threads opened, advanced, or resolved, each with its class**;
- target duration and spoken-word range.

Also provide, per arc: the five movement boundaries and their milestones; mini-arc groupings; the
opening acquisition runway; the midpoint reversal; the low point; the climax; the book resolution; the
seeds deliberately planted for the next book; and a **thread ledger** listing every Book thread with the
episode where it opens and the episode where it closes.

## The arc plan

Before drafting an arc, produce and store an explicit plan containing: arc number; episodes covered;
central dramatic question; primary external conflict; primary emotional and relationship arc; major
character arcs; book-specific promises; series-level promises in play; the five movement milestones; the
expected climax; the expected resolution; and the seeds intentionally planted for the following book.

While drafting, keep the thread ledger current — which promises are open, advanced, resolved, or
deliberately retained as series material. A ledger that is not updated during drafting is the mechanism
by which episode forty-eight becomes a speech.

## The chapter layer serves the book

The episode map groups episodes under macro chapters at roughly two to three episodes each. That grouping
is invisible to a serial listener and does real work at assembly: **macro chapters become the ebook's
table of contents.** Preserve it and plan it deliberately.

- A chapter anchor should be a coherent unit of story, not an arbitrary bracket around three episodes. If its episodes do not belong together as one chapter of a novel, re-cut it.
- Episodes inside one anchor should read continuously when set end to end. Do not plan an episode that must re-establish a setting or restate a situation the previous episode just left — in the book there is no gap between them.
- Chapter titles are book-facing and should read as chapter titles. Episode titles are serial-facing and may be blunter.
- An arc's five movements are planning structure and need not appear in the assembled book. The chapters are what the reader sees.
- `Scripts/build_book_pdf.py` assembles episodes into a PDF or EPUB from the heading and filename patterns, so the chapter layer is the mechanism by which an arc becomes a sellable book. Keep it clean.

## File and naming conventions for a new arc

Book One established the pattern. Every later arc follows it exactly — do not invent a new scheme.

- **Arcs are named in words:** `Book One`, `Book Two`, `Book Three`. Same in folders and file names.
- **Episode IDs are arc-scoped and restart each arc.** Book One is `B1E01`–`B1E60`; Book Two is `B2E01`–`B2E50`. An ID is stable forever once published.
- **Two numbering systems exist and must never be conflated.** The canonical ID is arc-scoped (`B2E01`). The platform number is continuous across the whole serial (`episode sixty-one`), because Pocket FM is one feed and does not restart. Record the platform offset in each arc's episode map. The spoken first line of an upload uses the **platform** number; the file name uses the **canonical ID**.
- **Per-arc WorldState files:** `WorldState/Book-Two-Storyline.md` and `WorldState/BookTwoEpisodeMap.json`. The two patterns differ — hyphenated for the storyline, camel-joined for the map. That is inherited and deliberately preserved; match it rather than normalizing it.
- **Series-wide files are never duplicated per arc:** `BookCodex.json`, `ContinuityLedger.json`, `AudioProductionBible.json`, `VisualBible.md`, `WritingStyle.md`, `CHANGELOG.md`. One ledger and one style guide, forever.
- **Assets:** `Assets/Book Two/Episodes/B2E##-Title-In-Kebab-Case.md` and `Assets/Book Two/EpisodeDescriptions/`. Stills go in `Assets/Stills/B2E##/`. `Assets/Covers`, `MP3`, `MP4` and `Videos` are series-wide and not split per arc.
- **Starting an arc** creates two asset folders and two WorldState files. Nothing else.
- **When an arc closes,** move its storyline and map paths into the codex's `authority.completed_arcs` and repoint the live `macro_storyline` and `episode_map` keys at the new arc. Never delete a completed arc's files.

See `BookCodex.json` → `file_conventions` for the authoritative version.

## Canon maintenance

When the user requests or approves a structural change, update the owning WorldState artifact rather
than duplicating it elsewhere:

- core canon, arc architecture and pointers → `BookCodex.json`
- macro story → the authoritative macro storyline path declared in `BookCodex.json`
- chapters, episodes, movements and thread ledger → the current episode map
- prose register and integrity checks → `WritingStyle.md`
- production and TTS rules → `AudioProductionBible.json`
- fact origins → `ContinuityLedger.json`
- version history → `CHANGELOG.md`

Validate every modified JSON file before completion.
