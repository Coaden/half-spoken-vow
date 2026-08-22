# Post-Build Audit — 2026-08-18

Recorded because two of these findings were real defects, and the reasoning should survive the session.

## 1. Werewolf/vampire asymmetry — FAILED, redesigned

**Counterfactual applied:** if June's wolf lineage were replaced by an ordinary human union, family,
religious community, or political faction, how much of Book One survives unchanged?

**Result: almost all of it.** Measured across the sixty mapped episodes, only eight touched anything
genuinely wolf-specific, while all sixty ran on institutional material — the Hall, dues, roster,
charter, elected business agent, burial fund, open vote, and June's lack of standing — every bit of
which survives the swap to a trade local intact. Clause one (residence) and clause two (surety)
survive. Marta's arithmetic survives. The entire spine survives.

The wolf side was decorative. The union framing was a deliberate modern-collision choice and remains
good, but a lineage that only supplies flavor is not load-bearing.

**Fix — the union is now *caused by* the lineage rather than decorating it.** Three nights a month,
involuntary and public, means three nights of lost wages, jobs that cannot be held, injuries no
employer will believe, and a body that must be safely housed on schedule. Dues, benefits, burial fund,
safe rooms and the housing roster all exist *because* members are predictably incapacitated. Remove
the moon and the institution has no reason to exist.

Added alongside it: members smell fear, arousal, illness, recent violence and blood kinship, so
sustained face-to-face lying is effectively impossible, voting is by open roll call because a position
cannot be hidden anyway, and kinship is a fact no filing can alter. That last one supplies the wolf
side's central wound — **every member in the Hall can smell June is a Havlik, and they voted to hand
her over anyway**, which is considerably crueller than not knowing.

## 2. Research-import audit — one bolted-on mechanic, unified

No prophecy and no imprisoned offstage power were imported; those findings were correctly left behind.
But `price_is_a_deed` was standing as a universal canon rule in a series containing almost no
"supernatural boons" for it to price — its only referent was the cutter. A rule with no ecology
behind it is exactly the shopping-list failure.

**Fix — one underlying logic, from which every rule is now derived:** *nothing binds until it enters a
record, and the two lineages disagree in good faith about what a record is.* Trustees are bound by
writing; members are bound by what is borne and witnessed.

Everything now follows from that single premise rather than sitting beside it:
- Prices are deeds because money leaves no binding record in either system.
- Completion is irrevocable because a completed vow sits in both registers plus a living witness's memory, and neither system holds an instrument of erasure — only annotation.
- Cutting reaches an incomplete attachment (a borne record only) but cannot touch a completed bond, which is why a completed bond is worth a war and why the Trust needs one.
- June's erasure worked on paper and could not touch the borne record, which is the wolf side's wound.
- Tampering with a record is the world's defining crime, which is what Yolanda's roster gap and the altered minutes actually are.
- And June — who makes records for a living, and is a wolf who fights like a trustee — becomes the thematic center of the supernatural system rather than merely its victim.

Two research lessons that solved the same problem were collapsed into this one synthesis rather than
both being retained.

## 3. Mate-bond permanence — changed as directed

Completion is now irrevocable, with correspondingly strict consent conditions, and the permanence is
defined narrowly: five facts, none of them love, obedience, fidelity, or proximity. The new cost —
completion forfeits the capacity to swear any other binding oath — produces the season's sharpest
engine, because it means **June can be bonded or initiated, never both.** Her two routes to standing
cancel each other.

## 4. Single-narrator architecture — mostly already satisfied

Already in place: single-narrator rule, per-character verbal signatures, and natural viewpoint
identification rather than name headers. **Added:** POV may change only at a clean scene boundary and
never twice in an episode; prose must never depend on separate performers; and narrator gender is
explicitly unlocked as a casting decision, with a note that the eighty-percent bride weighting may
favor a female voice without any of the writing assuming it.

## 5. Pocket FM first — trimmed

`video_assembly` and `elevenlabs_voice_cast` reduced to explicit deferred stubs. `VisualBible.md`
retained but relabelled a lightweight future-facing reference with low priority, since the codex's
`visual_identity` fields point at it and deleting it would break a pointer for no gain. Sound motifs
kept — the stenotype and read-back motifs are genuine storytelling devices, not production decoration.

## Preserved unchanged

The setting, the nine clauses, the three engines, the cast, the twenty-four-chapter arc, the sixty-episode
map, the durability rules, the heat policy, the originality blacklist, and the 80/20 bride-weighted dual
POV were all audited and left alone because they already satisfied the intent.

---

# Pre-Architect Stress Test — 2026-08-18 (1.1.1)

Two items examined. **Both failed.** Nothing else was changed.

## Scope of "nothing binds until it enters a record" — FAILED, tightened

As written the principle was unqualified, and a downstream writer could reasonably infer that ordinary
promises, crimes, debts, affection, and human legal obligation are meaningless unless recorded. The
serious version of that risk is consent: an unscoped reading would suggest a refusal needs a record to
count, which contradicts `symptoms_are_never_consent` and the entire consent architecture.

"Binds" is now defined as one narrow category — a claim a lineage institution will enforce, carrying
supernatural effect or altering standing. Everything ordinary is explicitly and fully binding with no
record. Human institutions operate independently and cannot be overridden by a lineage argument about
records. And consent is explicitly excluded and inverted: a record *creates* an obligation and never
validates a refusal.

The writing-versus-borne/witnessed ontology was preserved exactly as it was.

## Universal deed-price rule — FAILED, removed

The stated derivation was that "money leaves no binding record in either system." That is false in this
world. Trustees are lawyers running a perpetual property trust: they transact in money constantly,
convey estates by written instrument, own June's building, and collect her rent. A trustee would insist
a receipt binds perfectly. The justification was a rationalization written over an imported mechanic,
not a consequence of the first principle — precisely the fossil the brief warned about.

Checked what actually depended on it: exactly one referent, the cutter. The climax's "price" is a
consequence, not a purchased boon, and the Articles' clauses are contract terms. The world works
identically without a universal rule, so the universal rule is gone.

Kept only the genuinely derived half — a supernatural obligation exists once named aloud before
witnesses and is discharged by performance of what was named. Cutters now take deeds for a reason
specific to their trade: cutting is a crime against a record, so no court will enforce a cutter's fee,
and a deed performed in view is their only available security. That is character and engine rather than
cosmology, and it is sound.

**Architecture frozen at 1.1.1.**
