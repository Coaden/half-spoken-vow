# Causal Continuity Ledger Schema

`WorldState/ContinuityLedger.json` retains `facts[]` for static canon and adds companion sections for
changing narrative state. Do not cram causal state into static fact entries.

## Obligations

Each consequential obligation uses:

```json
{
  "id": "OB-001",
  "name": "short name",
  "bound_party": ["character or institution"],
  "beneficiary": ["character or institution"],
  "origin_episode": "B1E01",
  "creating_act": "the act that created it",
  "operative_language": "exact language or a precise paraphrase",
  "scope": "what it requires and does not require",
  "enforcement_system": ["Marrow Trust written record"],
  "known_by": ["character IDs"],
  "validity_status": "accepted | disputed | unclear",
  "character_positions": {"character ID": "believed validity and interpretation"},
  "effective_from": "episode or condition",
  "suspended_by": "act or null",
  "resumes_when": "condition or null",
  "satisfied_by": "condition or null",
  "waived_by": "required parties or null",
  "defeated_by": "condition or null",
  "current_status": "active | suspended | satisfied | waived | defeated | abandoned",
  "as_of_episode": "B1E##"
}
```

Keep Article clauses, vow exposure, surety, membership, residence, cutter commissions, and ordinary
human contracts separate. Neighboring obligations never merge merely because the same characters are
involved.

## Character state

Store snapshots only at meaningful changes, not every episode by rote:

```json
{
  "as_of_episode": "B1E05",
  "knows": [],
  "believes": [],
  "suspects": [],
  "incorrect_beliefs": [],
  "withholding": [],
  "does_not_know": [],
  "learned_this_episode": [],
  "belief_changed_this_episode": [],
  "emotional_carryover": [],
  "immediate_want": "",
  "rights_and_standing": [],
  "active_obligation_ids": []
}
```

`character_state` is keyed by canonical character ID. World-bible truth belongs in `facts`; it does not
enter `knows` until witnessed, told, or verified in manuscript prose.

## Causal bridges

```json
{
  "id": "CB-001",
  "from": ["fact, event, or episode IDs"],
  "to": ["fact, event, or episode IDs"],
  "question": "What state transition requires a cause?",
  "required_answer": null,
  "status": "verified | inference | productive_gap | gap_detected | repaired",
  "first_reader_pressure": "B1E##",
  "must_be_resolved_by": "B1E## or condition",
  "evidence": [],
  "proposed_minimum_repair": null
}
```

Use `gap_detected` when the current manuscript merely assumes the transition. Do not fill
`required_answer` with model inference.

## Explanation debts

```json
{
  "id": "ED-001",
  "question": "the reader-facing unanswered question",
  "known_answer": null,
  "reader_currently_knows": [],
  "character_state": {},
  "first_raised": "B1E##",
  "known_by": [],
  "reason_withheld": "",
  "payoff_episode_or_condition": null,
  "latest_safe_episode": null,
  "thread_class": "episode | movement | book | series",
  "urgency": "blocking | high | medium | low",
  "status": "open | partially_paid | paid"
}
```

An unknown answer cannot be marked as intentional merely because a later episode could explain it.

## Reader-inference gaps

```json
{
  "id": "RIG-001",
  "omitted_bridge": "",
  "supporting_facts": [],
  "dominant_inference": "",
  "first_occurs": "B1E##",
  "status": "safe | monitor | promoted_to_debt"
}
```

Use only when the inference requires no new event or rule and has one dominant reading.

## Contradictions

```json
{
  "id": "CON-001",
  "claim_a": {"source": "", "text": ""},
  "claim_b": {"source": "", "text": ""},
  "authority_assessment": "",
  "reader_effect": "",
  "severity": "blocking | high | medium | low",
  "status": "open | resolved | accepted_ambiguity",
  "proposed_minimum_repair": ""
}
```

Do not silently change either source during report-only work.

## Episode state

Use compact episode-level state to connect releases:

```json
{
  "episode": "B1E01",
  "trigger": "why this episode happens now",
  "entry_cause": "Because X, the viewpoint character does Y.",
  "objective_changes": [],
  "knowledge_changes": {},
  "belief_changes": {},
  "obligation_changes": [],
  "relationship_changes": [],
  "material_changes": [],
  "decision": "",
  "next_causal_bridge": "Because X happened, Y will now Z.",
  "audit_status": "clean | clean_with_inference | debt | contradiction"
}
```

## Institutional interpretations

For each load-bearing term:

```json
{
  "concept": "standing",
  "objective_effect": "",
  "civil_law_effect": "",
  "articles_effect": "",
  "local_nine_effect": "",
  "marrow_trust_effect": "",
  "other_institution_effects": {},
  "character_beliefs": {},
  "reader_knows_as_of": {"episode": "B1E##", "facts": []}
}
```

The same word may legitimately denote different rules in different systems. Preserve those distinctions.
