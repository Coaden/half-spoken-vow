# Session Init Prompt — Romantasy Pocket FM Series

Paste everything below the line into a new Claude Code session started in
`/Users/coaden/Documents/WerewolfVampireBride`.

---

You are initializing a brand-new serialized Romantasy audio-fiction series for Pocket FM in this project. The platform (instructions, skills, folder structure, WorldState templates) is already here and was forked from a completed sci-fi series. Your job is to fill it with an original world, cast, and story skeleton — not to write prose yet.

**The folder name `WerewolfVampireBride` is a working label, not the title.** You will create the real title.

## Step 1 — Load the platform

Read these completely before anything else:

1. `AGENTS.md` — the production contract. Note every `<TODO:>` marker; you will fill them.
2. `.agents/skills/series-novel-architect/SKILL.md` — this is the skill you are operating under for this task. Follow its architecture workflow and required episode-map schema.
3. `.agents/skills/series-chapter-writer/SKILL.md` — read it so the skeleton you build actually feeds it. Every episode object must contain what that skill needs to draft without asking questions.
4. `WorldState/*.json` and `WorldState/*.md` — the templates. Each JSON has a `_template` block explaining its purpose and rules. Honor those rules, then **delete the `_template` blocks** in the files you finalize.

## Step 2 — Read the genre library

Reference library: `/Users/coaden/Documents/Books/Werewolf-Vampire-Brides` (1,516 files, 5.6 GB).

Read **18 novels and 3 sourcebooks**. That is the whole corpus — resist the urge to add "just one more." Past roughly twenty works the signal smears and later reading mostly re-confirms what you already knew, at the cost of the attention you need for architecture. Each entry below is here because it teaches something the others do not. Paths are relative to `Vampire Ebook Collection [2013] [PDF]-V3nom/` unless marked *(root)*.

**Tier A — required, all eight.** Load-bearing.

| Work | Path | What to extract |
| --- | --- | --- |
| J.R. Ward, *Dark Lover* | `Ward, J.R/Black Dagger Brotherhood [S-U]/Black Dagger Brotherhood 01 - Dark Lover.pdf` | Long-series ensemble architecture: rotating couple-per-book over a continuous war arc. Study how book one seeds a dozen sequels. |
| Kresley Cole, *The Warlord Wants Forever* | `Cole, Kresley/Immortals After Dark = Valkyrie [S-O]/Valkyrie 01 - The Warlord Wants Forever.pdf` | **The single most valuable structural reference here.** Factions that manufacture future plots on demand — exactly what a 300-episode engine needs. |
| Christine Feehan, *Dark Prince* | `Feehan, Christine/Dark Series, Carpathians [S-O]/Dark 01 - Dark Prince.pdf` | The classic fated-mate machinery in its purest form. Understand it thoroughly, largely so you know what to modernize — especially around consent and agency. |
| Patricia Briggs, *Cry Wolf* | `Briggs, Patricia/Alpha & Omega [S-O]/Alpha & Omega 01 - Cry Wolf.pdf` | Pack hierarchy plus relationship agency. This is your ethical baseline for the mate-bond. |
| Jeaniene Frost, *Halfway to the Grave* | `Frost, Jeaniene/Night Huntress/Night Huntress 01 - Halfway to the Grave.pdf` | Audio-friendly chemistry and banter; first-person voice that survives being read aloud. |
| Katee Robert, *Court of the Vampire Queen* | *(root)* `Court of the Vampire Queen by Katee Robert EPUB` | Contemporary commercial heat level and pacing, as written for today's market. |
| Gena Showalter, *Vampire's Bride* | `Showalter, Gena/Atlantis [S-O]/Atlantis 04 - Vampire's Bride.pdf` | Unusually close to the literal bride premise. |
| Anne Rice, *Complete Vampire Chronicles* | *(root)* `Complete Vampire Chronicles (Omnibus) by Anne Rice.epub` | Myth, interiority, immortal psychology, atmosphere. Read the openings of *Interview* and *The Vampire Lestat*, plus one late section. **See the constraint below.** |

> **Rice constraint — read this twice.** Rice is in the corpus for mythology, immortal psychology, and the emotional weight of very long life. She is **not** the stylistic center of this project and her pacing is actively wrong for it. Do not let that voice set your prose density, sentence length, or scene rhythm. An eleven-minute Pocket FM episode cannot afford a character contemplating velvet curtains; it needs a cold open, a payoff, and a hook. Mine Rice for *what immortality feels like*, and take pacing from Cole, Frost, Caine, and Robert.

**Tier B — all six, no substitutions.**

| Work | Path | What to extract |
| --- | --- | --- |
| Rachel Caine, *Glass Houses* | `Caine, Rachel/Morganville Vampires [S-O]/Morganville 01 - Glass Houses.pdf` | **Strategically the most important entry in this tier.** Short, serial, immediate-pressure storytelling — closest thing in the library to the episode rhythm you are actually building. |
| Keri Arthur, *Full Moon Rising* | `Arthur, Keri/Riley Jenson Guardian [S-O]/Riley Jensen 01 - Full Moon Rising.pdf` | Crosses werewolf and vampire lineage territory in one protagonist, rather than teaching only one side of the ecosystem. |
| Chloe Neill, *Some Girls Bite* | `Neill, Chloe/Chicagoland Vampires [S-O]/Chicagoland Vampires 01 - Some Girls Bite.pdf` | Outsider-entry model: the protagonist learns a supernatural political system at the same rate the audience does. |
| Charlaine Harris, *Dead Until Dark* | `Harris, Charlaine/Sookie Stackhouse [S-O]/Stackhouse 01 - Dead Until Dark.pdf` | Accessible first-person voice; supernatural politics made local and socially legible instead of encyclopedic. |
| MaryJanice Davidson, *Undead and Unwed* | `Davidson, MaryJanice/Betsy 01 - Undead and Unwed.pdf` | Comic register. Paranormal romance does not have to brood under a crimson moon for three hundred episodes — humor is structural oxygen, and a series this long will suffocate without it. |
| C.T. Adams & Cathy Clamp, *Touch of Evil* | `Adams, C.T. & Clamp, Cathy/Thrall Series [S-O]/Thrall 01 - Touch of Evil.pdf` | Direct vampire-werewolf faction conflict. |

**Tier C — three studies.**

| Study | Path | What to extract |
| --- | --- | --- |
| **The Hamilton paired study** *(read both)* | `Hamilton, Laurell K/Anita Blake, Vampire Hunter [S-O]/Anita Blake Vampire Hunter 01 - Guilty Pleasures.pdf` and *(root)* `Slay, Anita Blake Vampire Hunter (30) by Laurell K. Hamilton EPUB` | Book one and book **thirty**. Do not ask "what did Hamilton do?" Ask: **what storytelling commitments were sustainable in book one that became liabilities by book thirty?** Cast bloat, stakes inflation, arcs that stopped closing, a protagonist who outgrew every threat. Your answer must materially shape `story_engines`, `recurring_characters`, and `do_not_resolve_yet`. This is the most important reading in the corpus for a series meant to run for years. |
| Nora Roberts, *Inheritance* | *(root)* `Inheritance, The Lost Bride (01) by Nora Roberts EPUB` | Commercial structure from a master of it. Roberts is here to remind you that popular fiction still has to **pay things off** — on schedule, every time, not eventually. A gothic bride/inheritance plot is the bonus. |
| Jay Kristoff, *Empire of the Vampire* | *(root)* `Empire of the Vampire by Jay Kristoff EPUB` | Prose craft and how a dark mythos earns its cruelty rather than posturing at it. |

**Tier D — exactly three sourcebooks, then stop.** From `Werewolf - The Apocalypse/`:

1. `WOD - Werewolf - The Apocalypse - Werewolf the Apocalypse (2nd Ed.).pdf` — the core rulebook
2. one Tribe book from `Tribe Books/` — a single faction-focused supplement, your choice
3. `WOD - Werewolf - The Apocalypse - Axis Mundi (The Book Of Spirits).pdf` — the cosmology/spirit-world supplement

> **Why the hard cap.** These books have enormous proprietary conceptual gravity. Read six and you will start designing definitely-not-Tribes and a definitely-not-spirit-ecology without noticing you are doing it. You want the *shape of a taxonomy* — how lineages, factions, a spirit world, and a mounting cosmic threat get organized into rules a long series can run on. Extract the organizing principle, then get out. Do not marinate.

Reading method: these are novels, so do not read them end to end. For each, read the opening 15–20 pages, one mid-book chapter, and the ending if reachable — enough to extract hook mechanics, POV and tense, chapter length, escalation cadence, and how romantic tension is sustained rather than resolved. PDFs read via the `pages` parameter (20 pages max per request). You may spawn subagents to read in parallel and report structured findings back; that is expected and encouraged for a job this size.

**Originality guardrail.** You are extracting *patterns*, never *property*.

No distinctive invented proper noun, faction name, supernatural taxonomy, coined term, or signature phrase may match or closely resemble the source corpus. Ordinary human given names are **not** considered collisions unless paired with another identifying element — a common first name shared with some character in a 2008 anthology is not a problem and is not worth investigating. Do not burn effort grep-searching the library to clear ordinary names; apply judgment to the handful of terms you actually coined.

Genre conventions are shared inheritance and fair to use: fated mates, blood debts, arranged marriage, clan politics, the moon cycle, courts and territories. A specific author's invented taxonomy, spirit ecology, or signature vocabulary is not. If a term feels distinctive enough to be someone's signature, invent your own replacement.

**Character originality — apply this to every named character you create.**

Archetypes are shared property and you are expected to use them: the brooding immortal lord, the reluctant bride, the alpha protector, the cynical hunter, the loyal second, the scheming matriarch. What you may never reproduce is a **recognizable character** — an archetype re-inhabited with the identifying details that make a specific author's creation theirs.

The risk is not any single detail; it is the **cluster**. Plagiarism reads as: same archetype + same name (or a near-homophone or obvious respelling) + same age or apparent age + same rank or title + same origin story or turning event + same signature trait, possession, or physical marker. Two matches in that cluster is a coincidence worth breaking; three is a copy regardless of intent.

Concretely, for every character you create:

- **Names.** No invented, coined, archaic, or otherwise distinctive name that appears in the corpus. Ordinary given names are fine on their own, but never pair an ordinary name with the same role a source character holds — a vampire sheriff named Eric or a Carpathian prince named Mikhail is a collision even though both first names are common. Say your names aloud: they also have to be speakable by one narrator and phonetically distinct from each other.
- **Ages and turning dates.** Do not reuse a source character's age, apparent age, century of birth, or age at turning. If a famous immortal was turned at twenty-five in 1791, yours is not.
- **Backstory.** No borrowed origin wound, no borrowed turning event, no borrowed family tragedy in its distinctive specifics. "Lost their family" is a genre situation; the particular circumstances of a known character's loss are not.
- **Signatures.** Invent your own physical markers, scars, eye colors, weapons, vehicles, pets, verbal tics, and habits. Signature possessions and quirks are among the most recognizable things an author owns.
- **Titles and ranks.** Do not lift a coined rank, order, or honorific from any source. Build your own vocabulary of power.

**Self-check, required before you finalize the codex.** For each principal and each recurring character, write one line in your research notes:

```
<Character> — archetype: <the shared archetype being used>
   nearest source character: <who they could be mistaken for, and from where>
   departures: <at least three concrete differences: name, age, origin, role, signature, arc>
```

If you cannot name three real departures, the character is not original enough yet — change it before it reaches `BookCodex.json`. If you cannot name a nearest source character at all, that is a good sign, but still record the archetype.

The goal is not to avoid the genre. It is to write characters who feel inevitable within it and belong to no one else.

Write your findings to `docs/genre-research-notes.md` **before** writing any canon. For every source, record a compact structured entry rather than a summary:

```
### <Title> — <Author>
KEEP:   <what this does that our series should do>
AVOID:  <what this does that would break a 300-episode audio serial>
ADAPT:  <the thing worth taking only if it is changed — and how>
WHY:    <one line: what makes this judgment specific to our series>
```

Then close with a short synthesis: hook mechanics, pacing and chapter length, POV and tense conventions, heat level, which tropes actually pay off in serialized audio, and the failure modes you observed. Keep the whole document to about two pages.

The point of the KEEP/AVOID/ADAPT/WHY format is that it gives the codex a **decision substrate** instead of twenty book reports. When you write `story_engines` and `canon_rules`, you should be able to trace nearly every choice back to a line in this file. This is a working document, not a deliverable.

## Step 3 — Ask me the decisions you cannot infer

Before writing canon, ask me **one batch** of questions (use the question tool, 3–4 questions max) covering only choices that materially change the series and that research cannot settle. Likely candidates:

- Heat level and explicitness ceiling for a Pocket FM audience
- Setting and era (contemporary hidden-world, secondary-world court fantasy, gothic historical)
- Whether the mate-bond is literal supernatural fact or cultural/political fiction the characters argue about
- Single close POV versus dual POV alternating between the bride and her counterpart

Recommend an option for each. Then proceed — do not stall on anything else.

## Step 4 — Create the title

Propose **five** title candidates with a one-line rationale each, pick your strongest, and record it in the codex with `"title_status": "working"`. Titles must work as spoken audio, read well truncated in an app list, and signal Romantasy without generic mush. Do not wait for my approval to continue — I will change it if I disagree.

## Step 5 — Build the WorldState

This series is designed to run **hundreds** of 8–12 minute episodes across multiple seasons, so architect for endurance, not just for Book One.

Produce, in this order:

**`WorldState/BookCodex.json`** — the canon authority. Fill every section of the template, and design specifically for the long run:
- `series` — title, format, premise, season-one A-plot, and a `series_promise` that can be paid hundreds of times without being used up.
- `canon_rules` — short, absolute guardrails. Include the supernatural rules (what each lineage can and cannot do, and the price of every power), what the protagonists are never allowed to become, and the tonal floor and ceiling.
- `primary_characters` — 5–7 principals, each with a role, a locked visual identity, a personality, a **core misbelief**, a core conflict, a personal stake, and an address policy (canonical name, ordinary narration name, formal address). Names must not collide phonetically with each other when spoken aloud by one narrator.
- `recurring_characters` — 6–10 more, each with their own want and cost.
- `story_engines` — the repeatable machines that generate episodes indefinitely. Give each one an `escalation` ladder of at least four stages so reuse never reads as repetition. A series that must sustain 300 episodes needs at least three independent engines (for example: a political/court engine, an intimate relationship engine, and a mounting external threat), plus a `practical_pressure` that keeps ordinary survival stakes under every supernatural beat.
- `do_not_resolve_yet` — the questions that survive well past Book One. Be explicit about which season each is *earliest* allowed to be touched.
- `setting` — the primary location and 5–8 key places, each earning its place by the recurring story work it does.

**`WorldState/Book-One-Storyline.md`** — the macro arc. 20–24 chapters, each with want / obstacle / change / consequence. Fill the protagonist arc (misbelief, cost, turn, ending state), the structural landmarks, what Book One resolves, and what it preserves. Also add a short **series horizon** section: a one-paragraph sketch of Seasons Two and Three so Book One plants what they will need.

**`WorldState/BookOneEpisodeMap.json`** — the release map. Target 60 episodes for Book One (acceptable range 48–72), 2–3 per macro chapter.
- Fill `chapter_anchors` for every chapter, `mini_arcs` for every 4–6 episode group, the `acquisition_runway` promises for episodes 1–12, and `season_structure`.
- **Episodes 1 through 10 must be fully specified** — every field the chapter-writer skill requires: cold open, pressure, 3+ progression beats, concrete payoff, exact end hook, sound-native reveal channel, continuity updates, POV, location, foreground characters (4–6 max), and word targets. These ten are what I will hand to the writing skill immediately after you finish, so they must be draftable with zero further questions.
- Episodes 11–60 need at minimum an ID, chapter ID, title, POV, one-line premise, payoff, and end hook. More detail is welcome; less is not acceptable.

**`WorldState/ContinuityLedger.json`** — seed with the facts your canon establishes at `CL-001` onward, each with status and origin. Twenty to forty foundational entries is a reasonable start.

**`WorldState/AudioProductionBible.json`** — fill `pronunciations` for every invented name you coined (this is why you keep names speakable), `address_policy` for each principal, and the world-specific `sound_design.recurring_motifs`. Leave `selected_narrator` and the ElevenLabs cast unset — I choose voices on the platform later.

**`WorldState/VisualBible.md`** — the base style prompt and a locked brief per principal, written prompt-ready.

**`AGENTS.md`** — replace every `<TODO:>` marker with the decisions you just made, and delete the template banner at the top.

**`WorldState/CHANGELOG.md`** — add one entry above the existing creation line recording the series initialization: title chosen, canon locked, episode count planned.

## Step 6 — Verify before you report

1. Every JSON file parses (`python3 -m json.tool`).
2. No `<TODO:` markers and no `_template` blocks remain in any file you finalized.
3. Cross-file pointers agree: the codex's `authority` paths exist, the episode map's `macro_source` matches the storyline filename, and every character referenced in the episode map exists in the codex.
4. Episode IDs are contiguous `B1E01`–`B1E##` with no gaps, and every episode maps to a real chapter anchor.
5. Your coined proper nouns, faction names, and taxonomy terms are original per the originality guardrail. Review the short list of terms you actually invented; do not audit ordinary given names.
6. Every principal and recurring character has a completed archetype self-check in the research notes, each with at least three concrete departures from its nearest source character. No character shares a name-plus-role, age, or origin cluster with anything in the corpus.
7. Every episode in 1–10 has both a payoff and an end hook, and no reveal channel depends on a silent visual.

Then report: the chosen title, the cast in one line each, the three story engines, the Book One shape, and confirmation that episodes 1–10 are draft-ready. Do not write episode prose — I will start that in the next instruction.
