---
name: narrative-causal-continuity
description: Audit or maintain causal, epistemic, emotional, institutional, obligation, and temporal continuity across serial episodes. Use before or after drafting episodes, when reviewing transitions, or when a character may know, believe, owe, pursue, or feel something the preceding manuscript did not establish.
---

# Narrative Causal Continuity

Keep independently drafted episodes inside one continuous chain of causes. A locally strong scene is not
ready if it begins from knowledge, motive, standing, obligation, emotion, location, or a rule that prior
prose never produced.

This skill audits continuity. It does not authorize rewriting finalized prose. When the user requests an
audit or report, record findings and proposed minimum repairs without changing manuscript files.

## Authority

Check claims in this order:

1. `WorldState/BookCodex.json` and locked canon.
2. Published or finalized manuscript prose.
3. `WorldState/ContinuityLedger.json`.
4. The authoritative episode map and macro storyline pointed to by the codex.
5. Draft notes.
6. Model inference.

The manuscript controls what was actually dramatized. If finalized prose conflicts with a ledger entry,
flag the conflict; do not force the prose to match an erroneous summary. Follow `AGENTS.md` maintenance
rules when the author approves a correction.

Before using or changing causal ledger sections, read
[the ledger schema](references/ledger-schema.md). Read only the episode range and neighboring material
needed for the requested audit, plus any later episode necessary to verify a planned payoff.

## Core rule

Every episode begins in a world previous episodes actually created.

Never infer a missing bridge because the current map needs it. When a bridge is absent:

1. propose the minimum causal bridge;
2. propose an action that follows from the existing state; or
3. classify the omission as an intentional gap and record its payoff.

Never silently teleport knowledge, belief, motive, emotion, obligation, permission, standing, location,
relationship state, or world rules.

## Pre-draft continuity gate

Before drafting an episode, establish the entry state of every principal character appearing in it:

- **Knowledge:** personally witnessed, explicitly told, or independently verified facts; also note canon
  the character does not know.
- **Belief:** the character's present model, including incorrect beliefs. Do not update it without an event.
- **Interpretation:** what the character thinks recent facts mean.
- **Obligations:** source, bound party, beneficiary, scope, enforcement system, effective condition,
  ending condition, awareness, and perceived validity.
- **Rights and standing:** what the character may do or refuse, and which institution recognizes it.
- **Immediate want:** what the character wants today, not the abstract book goal.
- **Emotional carryover:** the unresolved feeling produced by the prior episode.
- **Immediate prior cause:** complete `Because X happened, Character Y now does Z.`

Then answer `Why does this episode happen now?` with a trigger already present in story state: notice,
deadline, evidence, another character's act, prior decision, material necessity, emotional fallout, or a
physical consequence. A map destination is not a trigger.

If the causal sentence or trigger cannot be supported, stop before prose and classify the gap. A blocking
gap must be resolved by the author or by an already-authorized, canon-compatible bridge.

## Scene-entry check

For every scene, establish:

- why each person is physically present;
- why they speak now;
- what each expects;
- what each knows about the others; and
- what changed since their previous encounter.

Do not open three conversational steps after the exchange the reader needed unless that omission is an
intentional, tracked choice.

## Revelation types

Classify every consequential reveal:

- **new fact:** neither character nor reader previously knew it;
- **existing fact newly revealed:** it was true but concealed;
- **existing fact newly understood:** the information was known but its importance was not;
- **changed fact:** the world state itself changed.

Preserve a plausible reaction or model update. Genre pacing permits compressed processing and omitted
questions, but readers tolerate omitted explanation more readily than omitted reaction.

## Gap classification

- **Productive gap:** the missing bridge is intentional; the author knows what happened, when, who knows,
  why it is withheld, and its payoff condition.
- **Reader-inference gap:** established facts support one dominant bridge without a new event or rule.
- **Continuity debt:** the bridge is deliberately unavailable and must be paid later. Record first reader
  pressure, who knows, concealment reason, payoff condition, and latest safe episode.
- **Accidental gap:** neither prose nor canon contains the bridge, but the scene assumes it. Flag for repair.

A mystery announces that something does not add up. A continuity error behaves as if everything adds up
when it does not. Never relabel an accidental gap as mystery after the fact.

## Exit-state update

After an episode, record for each principal:

- new objective fact;
- new knowledge;
- belief strengthened, weakened, changed, or made uncertain;
- obligation created, satisfied, suspended, resumed, defeated, waived, transferred, or clarified;
- relationship and emotional change;
- material change in money, housing, work, health, schedule, transport, or reputation;
- decision that causes later action; and
- `Because ___ happened here, ___ will now ___.`

If the next mapped episode cannot be reached through such sentences, flag the transition.

## Post-draft audit

Check whether anyone:

1. knows something not learned;
2. forgets material knowledge;
3. changes belief without cause;
4. acquires or loses an obligation without a creating or terminating act;
5. pursues a goal without learning why it matters;
6. accepts a rule without enough reaction to show an updated model;
7. begins several causal steps past the previous exit state;
8. relies on undramatized bible knowledge;
9. carries an emotional reset between adjacent episodes; or
10. leaves an apparent discontinuity unclassified.

Also verify that the next episode follows from this exit state.

Prefer the smallest proposed repair: one sentence, question, incoming notice, recalled line, observable
consequence, or corrected ledger entry. Do not add exposition automatically.

## Genre compression

Compression may remove travel, duration, repetition, routine research, or mundane process. It must not
remove the event that creates important knowledge, motive, obligation, permission, or consequence.

Rule: skip steps that consume time; do not skip steps that create state.

## Institutional interpretation

For load-bearing terms such as `bride`, `standing`, `record`, `binding`, `residence`, `claim`, and
`witness`, separately track:

- objective supernatural or civil effect;
- Local Nine's interpretation;
- the Marrow Trust's interpretation;
- other institutional interpretations;
- the current viewpoint character's belief; and
- what the reader has been shown.

Never blend two systems because they use the same word.

## Movement and book gates

Before each ten-to-twelve-episode movement, audit open explanation debts, active obligations, principal
knowledge states, unresolved relationship changes, planned causal triggers, and any future episode that
assumes an unscheduled event.

Before closing a book, pay every book-level causal debt, preserve only intentional series unknowns, flag
accidental contradictions, and establish a clean exit state. Readers may finish with mysteries; they must
not finish unsure whether the story knows its own rules.

## Report format

For a requested episode range, report:

1. overall causal verdict;
2. blocking contradictions or gaps;
3. high-, medium-, and low-priority debts;
4. productive and reader-inference gaps that should remain untouched;
5. obligation changes;
6. character knowledge and belief changes;
7. episode-to-episode causal chain; and
8. proposed minimum repairs, clearly separated from findings.

Never modify manuscript prose during a report-only audit.
