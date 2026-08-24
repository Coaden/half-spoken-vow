# Narrative IDE Sidequest

> Author scratchpad. Non-canonical product/design speculation. Do not use as input for book-creation skills.

## The idea

This is not merely a diagram generator. It is a **domain-specific visual modeling environment for fiction**: Rational Rose, Visio, or UML, but with story-native primitives and structured data behind every node.

The project already contains much of the underlying model in `BookCodex.json`, `EpisodeMap.json`, `ContinuityLedger.json`, storyline files, canon rules, obligations, character states, and explanation debts. In software terms, the story’s AST exists before its editor.

**Working name:** Narrative IDE — an IDE for story architecture and continuity.

## Story-native primitives

- Character
- Event
- Hook
- Payoff
- Knowledge
- Obligation
- Relationship
- Location
- Mystery
- Branch
- Scene
- Episode
- Chapter
- Arc
- Institution
- State transition

Each node carries structured data, rather than only a label.

## Rendering and interaction

Graphviz is useful as an automatic renderer for generated dependency graphs. It accepts a graph definition in DOT and handles layout, but is not itself an interactive authoring GUI.

For an interactive canvas, investigate tools such as React Flow, Cytoscape.js, JointJS, GoJS, and the interaction model behind draw.io or Visio. A custom app could store a `THSV.storygraph` file and open it as an explorable canvas.

## Swimlanes

A swimlane view can show characters, institutions, or plot threads across episodes and make absences visible.

```text
             E01      E02      E03      E04      E05

June         Named    Lies     Hall     Marta    Bridge
              │        │        │        │        │
Elias        Vow ──────┘                 │      Explains
              │                          │
Tess                                            [offstage]
              │
Articles     Naming   Suspended  Standing  Copy   Clock
```

For example, this view makes “where did Tess disappear for nine episodes?” obvious.

## Sankey-style story-thread density

Sankey diagrams normally show weighted flows such as energy or money. For fiction, line thickness could represent narrative weight, number of scenes, stakes, or dependency density.

```text
Articles ━━━━━━━━━━━┓
                    ┣━━> B1E14
Moon ━━━━━━━━┓      ┃
             ┣━━━━━━┛
June Safety ━┛

                         ━━━━━> B1E36 payoff
```

This is not a universal view, but it could be a powerful story-thread density map.

## Episode inspector concept

Double-clicking an episode node should reveal its state, obligations, threads, and dependencies.

```text
Episode: B1E14
Title: Nineteen Days to Nine
POV: June
Movement: 2

ENTRY STATE
- No Local standing
- 19 days until moon
- Knows private containment is unsafe

TRIGGER
- Hall formally refuses safe-room access

HOOKS CREATED
- Seller has unsafe alternate plan
- Receipt proves Local contradiction

OBLIGATIONS
- OB-008 room purchase
- OB-009 conditional return

THREADS
- Moon / containment
- Local Nine exclusion
- June independence

PAYOFFS
- B1E35
- B1E36
```

Visible, semantic edges should connect every field to the relevant nodes elsewhere in the graph.

## MCP interface

An MCP server could allow Codex to query and modify the structured story model directly:

```text
get_episode(B1E14)
get_character_state("June", "B1E14")
find_open_hooks()
find_unpaid_debts()
create_hook(...)
link_payoff(...)
move_event(...)
show_dependency_path(B1E03, B1E36)
show_character_knowledge("Tess")
validate_transition(B1E13, B1E14)
```

Then questions such as “show every hook introduced before E20 that still has no payoff” or “move the Tess reveal from E11 to E13 and tell me what breaks” can be answered structurally instead of by repeatedly rereading the corpus.

## Typed graph model

### Node types

```text
Character
Episode
Scene
Event
Hook
Payoff
Fact
KnowledgeState
Obligation
Institution
Location
Relationship
Mystery
Arc
```

### Edge semantics

```text
CAUSES
REVEALS
DEPENDS_ON
PAYS_OFF
KNOWS
LEARNS
WITHHOLDS
OWES
BELONGS_TO
CONTRADICTS
SUPERSEDES
APPEARS_IN
MOTIVATES
```

The semantic layer is the important distinction. A generic graph only records `June -> B1E14`; the fiction model records an action such as `June --DECIDES_IN--> B1E14` or `B1E03 --CREATES_EXPLANATION_DEBT--> ED-001`.

## Timeline and graph hybrid

The other core UI view is a timeline plus graph: episode number on the horizontal axis and story threads on rows.

```text
              01 02 03 04 05 06 07 08 09 10 11 12 13 14 ...

Articles      ███████████████████████████████████████
Half-vow      ███████──────████────█████████████████
Moon                ███████──────██████████████████
Tess                                  ███████████
Cyd           ██────██──────████████────────██████
Mother             ██──────────────██─────────────
```

Selecting a block should jump into the corresponding graph. This combines macro pacing with micro causality.

## Product principle

The result should be a reasoning substrate, not a pretty corkboard: a model that knows what an edge means, can validate transitions, locate open obligations and mysteries, and expose the downstream consequences of a story change.
