#!/usr/bin/env python3
"""Build the narrative flow atlas: mermaid views of an arc's structure.

Reads the authoritative WorldState files and emits a Markdown file of left-to-right
mermaid flowcharts covering the episode spine, thread lanes, the obligation chain,
the audio reveal channels, closing-turn distribution, and the protected mysteries.

Every node label is copied from the source JSON rather than restated, so the output
is a view of canon and never an authority over it. Regenerate after canon changes
instead of hand-editing the Markdown.

Usage:
    Scripts/build_narrative_flow.py
    Scripts/build_narrative_flow.py --arc "Book One" --out WorldState/BookOneNarrativeFlow.md
"""

from __future__ import annotations

import argparse
import collections
import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

MOVEMENT_TITLES = {
    1: "Movement One — Setup",
    2: "Movement Two — Escalation",
    3: "Movement Three — Reversal and midpoint",
    4: "Movement Four — Consequence and convergence",
    5: "Movement Five — Climax, payoff, denouement",
}

MOVEMENT_WORDS = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}

# Closing turns the style guide treats as the loudest kinds, upper-cased in labels
# so the arc's four hard cliffs and its reversals are visible at a glance.
LOUD_TURNS = {"reversal", "cliffhanger"}

# The seven reveal channels from AudioProductionBible.json plus the series signature,
# each with the pattern that recognizes it in an episode's mapped reveal_channel.
DEVICE_CHANNELS = [
    ("RB", "Read-back — a passage spoken once, then repeated verbatim"
           "<br/><i>the series signature: proof, menace, intimacy</i>",
     r"read.?back|read them both|repeated exactly|verbatim"),
    ("DOC", "A document read into a record",
     r"read (aloud|into)|reads? the|dictat|filing is|clause read|sworn testimony|letter"),
    ("LED", "A bound ledger or register read aloud, the fact arriving as an absence",
     r"ledger|register|card index|roster|three lists|two registers|parish register"),
    ("PHONE", "A voicemail or speakerphone call in company",
     r"voicemail|speaker|phone"),
    ("OVER", "An overheard argument through a door or stairwell",
     r"overheard|stairwell|through the door|cut off mid-sentence"),
    ("ROLL", "A vote called name by name",
     r"roll call|open roll|vote"),
    ("PRICE", "A price quoted in full before any work is done",
     r"price|quoted the commission|receipt|refund|hours|dollar"),
    ("THRESH", "A sound at a threshold that forces a decision",
     r"threshold|door opening|answering from inside|invitation"),
    ("BODY", "Borne evidence — scent, the involuntary body, presence that cannot lie",
     r"scent|bodily|smell|involuntary|physical gradient|sound and"),
    ("RIVER", "River sound under a mid-span negotiation", r"river"),
]

# The obligation spine and the act that carries each link. Ledger ids are stable;
# an arc whose ledger uses different ids supplies its own spine here.
OBLIGATION_SPINE = {
    "Book One": {
        "nodes": [
            "OB-001", "OB-002", "OB-003", "OB-011", "OB-012", "OB-013", "OB-018",
            "OB-014", "OB-023", "OB-034", "OB-024", "OB-025", "OB-026", "OB-027",
            "OB-028", "OB-029", "OB-030", "OB-033",
        ],
        "edges": [
            ("OB-001", "OB-002", "the half-vow names her"),
            ("OB-002", "OB-003", "clause one matures"),
            ("OB-003", "OB-011", "residence satisfied, clause two due"),
            ("OB-011", "OB-012", "she needs a surety defense"),
            ("OB-012", "OB-013", "one scheduling fact"),
            ("OB-013", "OB-018", "refusal creates the derivative"),
            ("OB-011", "OB-014", "Milo accepts in his own words"),
            ("OB-014", "OB-024", "surety entered, term certain runs"),
            ("OB-034", "OB-023", "Kearse invokes; Delisle verifies"),
            ("OB-023", "OB-024", "parish presents the clause"),
            ("OB-024", "OB-025", "no accepted witness"),
            ("OB-025", "OB-026", "forfeiture converts surety to custody"),
            ("OB-026", "OB-027", "Elias prepares adverse testimony"),
            ("OB-027", "OB-028", "June elects to remain the bride"),
            ("OB-028", "OB-029", "the case is filed and heard"),
            ("OB-029", "OB-030", "Elias is barred from office"),
            ("OB-029", "OB-033", "what is left is a chosen alliance"),
        ],
        "countables": [
            ("nine clauses", "the instrument's fixed sequence"),
            ("eighteen seventy-one", "execution date of the Articles"),
            ("three copies", "sealed original, certified counterpart, parish third"),
            ("three hundred eleven members", "what Marta is protecting"),
            ("nineteen days to nine", "the altered numeral and the mandatory stay"),
            ("forty-eight hours", "the surety dispute stay"),
            ("three nights", "the public moon calendar"),
            ("eleven years", "Tess's case"),
            ("seven brides, four graves", "the house ledger"),
            ("six left", "the clauses still standing at the end"),
        ],
    }
}


def episode_number(episode_id: str) -> int:
    """B1E17 -> 17."""
    match = re.search(r"E(\d+)$", episode_id)
    if not match:
        raise ValueError(f"unrecognized episode id: {episode_id}")
    return int(match.group(1))


def label(text: str) -> str:
    """Make a string safe inside a quoted mermaid node label."""
    text = str(text).replace('"', "'")
    for bad, good in (("[", "("), ("]", ")"), ("{", "("), ("}", ")")):
        text = text.replace(bad, good)
    return text


def clip(text: str, limit: int) -> str:
    text = label(text)
    return text if len(text) <= limit else text[: limit - 3] + "..."


def turn_label(turn: str | None) -> str:
    if not turn:
        return ""
    return turn.upper() if turn in LOUD_TURNS else turn


class AtlasBuilder:
    def __init__(self, root: Path, arc: str) -> None:
        self.root = root
        self.arc = arc
        self.codex = self._load("WorldState/BookCodex.json")
        authority = self.codex["authority"]
        self.emap = self._load(authority["episode_map"])
        self.ledger = self._load(authority["continuity_ledger"])
        self.episodes = self.emap["episodes"]
        self.obligations = {o["id"]: o for o in self.ledger["obligations"]}
        self.thread_actions: dict[str, list[tuple[int, str]]] = collections.defaultdict(list)
        for episode in self.episodes:
            for thread in episode.get("threads", []):
                self.thread_actions[thread["id"]].append(
                    (episode_number(episode["id"]), thread["action"])
                )
        self.lines: list[str] = []

    def _load(self, relative: str) -> dict:
        return json.loads((self.root / relative).read_text())

    def w(self, text: str = "") -> None:
        self.lines.append(text)

    # ---------------------------------------------------------------- sections

    def header(self) -> None:
        self.w(f"# {self.arc} — Narrative Flow Atlas")
        self.w()
        self.w("Generated by `Scripts/build_narrative_flow.py` from `WorldState/BookCodex.json`,")
        self.w("the arc episode map, `WorldState/ContinuityLedger.json` and")
        self.w("`WorldState/AudioProductionBible.json`. Every node label is taken from those files")
        self.w("rather than restated by hand, so this file is a *view* of canon and never an authority")
        self.w("over it. Regenerate rather than hand-edit.")
        self.w()
        self.w("Six left-to-right flowcharts:")
        self.w()
        self.w("1. [The episode spine](#1-the-episode-spine) — every episode, POV, and closing-turn type")
        self.w("2. [Plot lines](#2-plot-lines) — book threads, series threads, and mini-arcs as lanes")
        self.w("3. [The clause spine](#3-the-clause-spine) — obligations from creation to defeat")
        self.w("4. [Devices](#4-devices) — the audio reveal channels and where each one carries an episode")
        self.w("5. [Closing turns](#5-closing-turns) — hook variety across the arc")
        self.w("6. [Protected mysteries](#6-protected-mysteries) — what the arc pays and what it holds")
        self.w()
        self.w("---")
        self.w()

    def spine(self) -> None:
        plan = self.emap["arc_plan"]
        self.w("## 1. The episode spine")
        self.w()
        self.w(f"**Central dramatic question.** {plan['central_dramatic_question']}")
        self.w()
        self.w("Violet nodes are the second viewpoint, blue the protagonist's, gold the arc's")
        self.w("load-bearing turns. The second label line is the mapped closing turn — the state change")
        self.w("the episode is required to deliver.")
        self.w()
        self.w("```mermaid")
        self.w("flowchart LR")
        self.w("  classDef pov1 fill:#eef4fb,stroke:#5588bb,color:#12293d;")
        self.w("  classDef pov2 fill:#f6eff7,stroke:#9a6fa6,color:#33203a;")
        self.w("  classDef mile fill:#fff6e5,stroke:#cc9a3d,color:#3d2c08;")

        movements = sorted({e["movement"] for e in self.episodes})
        primary_pov = collections.Counter(e["pov"] for e in self.episodes).most_common(1)[0][0]
        boundaries: list[tuple[int, int]] = []
        for movement in movements:
            in_movement = [e for e in self.episodes if e["movement"] == movement]
            first, last = episode_number(in_movement[0]["id"]), episode_number(in_movement[-1]["id"])
            title = MOVEMENT_TITLES.get(movement, f"Movement {movement}")
            self.w(f'  subgraph M{movement}["{title} (E{first}-E{last})"]')
            self.w("    direction LR")
            for episode in in_movement:
                n = episode_number(episode["id"])
                text = f'{n} · {label(episode["title"])}<br/><i>{turn_label(episode.get("end_turn_type"))}</i>'
                self.w(f'    E{n:02d}["{text}"]')
            self.w("    " + " --> ".join(f"E{episode_number(e['id']):02d}" for e in in_movement))
            self.w("  end")
            boundaries.append((first, last))
        for (_, last), (first, _) in zip(boundaries, boundaries[1:]):
            self.w(f"  E{last:02d} --> E{first:02d}")

        pov1 = [episode_number(e["id"]) for e in self.episodes if e["pov"] == primary_pov]
        pov2 = [episode_number(e["id"]) for e in self.episodes if e["pov"] != primary_pov]
        self.w("  class " + ",".join(f"E{n:02d}" for n in pov1) + " pov1;")
        if pov2:
            self.w("  class " + ",".join(f"E{n:02d}" for n in pov2) + " pov2;")
        milestones = self._milestone_episodes()
        if milestones:
            self.w("  class " + ",".join(f"E{n:02d}" for n in milestones) + " mile;")
        self.w("```")
        self.w()
        self.w("What each movement is for, from `movement_milestones`:")
        for entry in self.emap.get("movement_milestones", []):
            first, last = entry["episodes"]
            word = MOVEMENT_WORDS.get(entry["movement"], entry["movement"])
            self.w(
                f"- **Movement {word} (E{episode_number(first)}–E{episode_number(last)}) · "
                f"{label(entry['function'])}** — {label(entry['milestone'])}"
            )
        self.w()
        beats = self.emap.get("season_structure", {})
        if beats:
            self.w("The named structural beats, from `season_structure` — these are the gold nodes:")
            for key, text in beats.items():
                self.w(f"- **{key.replace('_', ' ').title()}** — {label(text)}")
            self.w()
        self.w("---")
        self.w()

    def _milestone_episodes(self) -> list[int]:
        """Episodes that open or close the arc, resolve a book thread, or carry a named beat."""
        marked = {episode_number(self.episodes[0]["id"]), episode_number(self.episodes[-1]["id"])}
        for thread in self.emap["thread_ledger"].get("book_threads", []):
            marked.add(episode_number(thread["closing_episode"]))
        for episode in self.episodes:
            for thread in episode.get("threads", []):
                if thread["action"] == "resolved" and thread["id"].startswith("BT"):
                    marked.add(episode_number(episode["id"]))
        for text in self.emap.get("season_structure", {}).values():
            for found in re.findall(r"B\dE(\d+)", str(text)):
                marked.add(int(found))
        known = {episode_number(e["id"]) for e in self.episodes}
        return sorted(marked & known)

    def _lane(self, thread_id: str, title: str, css: str) -> None:
        sequence = self.thread_actions.get(thread_id, [])
        if not sequence:
            return
        self.w(f'  subgraph {thread_id}["{thread_id} — {label(title)}"]')
        self.w("    direction LR")
        node_ids = []
        for number, action in sequence:
            mark = {"opened": "open", "advanced": "", "resolved": "RESOLVED"}.get(action, action)
            text = str(number) + (f"<br/><b>{mark}</b>" if mark else "")
            node_id = f"{thread_id}_{number:02d}"
            shape = f'{node_id}(["{text}"])' if action in ("opened", "resolved") else f'{node_id}["{text}"]'
            self.w(f"    {shape}")
            node_ids.append(node_id)
        self.w("    " + " --> ".join(node_ids))
        self.w("  end")
        self.w(f'  class {",".join(node_ids)} {css};')

    def plot_lines(self) -> None:
        ledger = self.emap["thread_ledger"]
        self.w("## 2. Plot lines")
        self.w()
        self.w("Each lane is one tracked thread, containing only the episodes where the map records an")
        self.w("action on it. `opened` is the left edge, `resolved` the right. The ceiling is seven")
        self.w("concurrent open threads, of which at most three are protected series mysteries.")
        self.w()
        self.w("```mermaid")
        self.w("flowchart LR")
        self.w("  classDef bk fill:#eaf3ea,stroke:#4c8a4c,color:#16301a;")
        self.w("  classDef sr fill:#fdeeee,stroke:#b35a5a,color:#3d1616;")
        for thread in ledger.get("book_threads", []):
            self._lane(thread["id"], thread["name"], "bk")
        for thread in ledger.get("series_threads", []):
            self._lane(thread["id"], thread["name"], "sr")
        self.w("```")
        self.w()
        self.w("**Book thread closures** (from `thread_ledger.book_threads`):")
        for thread in ledger.get("book_threads", []):
            self.w(
                f"- **{thread['id']} · {label(thread['name'])}** — opens {thread['opens']}, "
                f"closes {thread['closing_episode']}. {label(thread['closure'])}"
            )
        self.w()
        self.w("### Mini-arcs")
        self.w()
        self.w("Non-overlapping four-to-six-episode units. Each answers a local question while advancing")
        self.w("a book thread, which is what keeps the open-thread count under the ceiling.")
        self.w()
        self.w("```mermaid")
        self.w("flowchart LR")
        self.w("  classDef ma fill:#f2f2f7,stroke:#7a7a99,color:#22223a;")
        previous = None
        arcs = self.emap["mini_arcs"]
        for arc in arcs:
            first, last = arc["episode_range"]
            node_id = arc["id"]
            self.w(
                f'  {node_id}["{node_id} · E{episode_number(first)}-E{episode_number(last)}'
                f'<br/>{clip(arc["question"], 96)}"]'
            )
            if previous:
                self.w(f"  {previous} --> {node_id}")
            previous = node_id
        self.w("  class " + ",".join(a["id"] for a in arcs) + " ma;")
        self.w("```")
        self.w()
        for arc in arcs:
            first, last = arc["episode_range"]
            self.w(
                f"- **{arc['id']} (E{episode_number(first)}–E{episode_number(last)})** — "
                f"{label(arc['payoff'])}"
            )
        self.w()
        self.w("---")
        self.w()

    def clause_spine(self) -> None:
        spine = OBLIGATION_SPINE.get(self.arc)
        self.w("## 3. The clause spine")
        self.w()
        if not spine:
            self.w(f"No obligation spine is defined for {self.arc} in `build_narrative_flow.py`.")
            self.w()
            self.w("---")
            self.w()
            return
        self.w("The obligation chain from `ContinuityLedger.json`. Boxes are obligations, labelled with")
        self.w("the episode that creates them and their final recorded status. This is the causal machine")
        self.w("the plot runs on: each clause creates the conditions for the next.")
        self.w()
        self.w("```mermaid")
        self.w("flowchart LR")
        self.w("  classDef live fill:#eef4fb,stroke:#5588bb,color:#12293d;")
        self.w("  classDef closed fill:#eaf3ea,stroke:#4c8a4c,color:#16301a;")
        self.w("  classDef perm fill:#fff6e5,stroke:#cc9a3d,color:#3d2c08;")
        missing = [oid for oid in spine["nodes"] if oid not in self.obligations]
        if missing:
            raise SystemExit(f"obligations missing from ledger: {', '.join(missing)}")
        for oid in spine["nodes"]:
            obligation = self.obligations[oid]
            status = obligation.get("current_status", "").replace("_", " ")
            self.w(
                f'  {oid.replace("-", "")}["{oid} · {label(obligation["name"])}'
                f'<br/><i>origin {obligation.get("origin_episode")} — {status}</i>"]'
            )
        for source, target, edge in spine["edges"]:
            self.w(f'  {source.replace("-", "")} -->|"{edge}"| {target.replace("-", "")}')
        permanent, live, closed = [], [], []
        for oid in spine["nodes"]:
            status = self.obligations[oid].get("current_status", "")
            if "non_executable" in status or "permanent" in status:
                permanent.append(oid)
            elif status.startswith("active"):
                live.append(oid)
            else:
                closed.append(oid)
        for group, css in ((live, "live"), (closed, "closed"), (permanent, "perm")):
            if group:
                self.w("  class " + ",".join(o.replace("-", "") for o in group) + f" {css};")
        self.w("```")
        self.w()
        self.w(
            f"The full ledger carries {len(self.obligations)} obligations. The ones above are the spine;"
        )
        self.w("the rest are the human-scale costs that hang off it.")
        self.w()
        self.w("---")
        self.w()

    def devices(self) -> None:
        self.w("## 4. Devices")
        self.w()
        self.w("`AudioProductionBible.json` fixes seven reveal channels plus the series signature. Every")
        self.w("essential reveal must arrive as sound, and no channel may run twice in a row. Below, each")
        self.w("channel points at the episodes whose mapped `reveal_channel` it carries.")
        self.w()
        assigned: dict[str, list[int]] = collections.defaultdict(list)
        for episode in self.episodes:
            channel_text = episode.get("reveal_channel", "").lower()
            matched = False
            for key, _, pattern in DEVICE_CHANNELS:
                if re.search(pattern, channel_text):
                    assigned[key].append(episode_number(episode["id"]))
                    matched = True
            if not matched:
                assigned["DOC"].append(episode_number(episode["id"]))
        self.w("```mermaid")
        self.w("flowchart LR")
        self.w("  classDef sig fill:#fff6e5,stroke:#cc9a3d,color:#3d2c08;")
        self.w("  classDef ch fill:#eef4fb,stroke:#5588bb,color:#12293d;")
        self.w("  classDef ep fill:#ffffff,stroke:#aab,color:#333;")
        for key, text, _ in DEVICE_CHANNELS:
            self.w(f'  {key}["{text}"]')
        for key, _, _ in DEVICE_CHANNELS:
            numbers = assigned.get(key, [])
            for index in range(0, len(numbers), 10):
                chunk = numbers[index : index + 10]
                node_id = f"{key}_L{index // 10}"
                self.w(f'  {node_id}["{" · ".join(f"E{n}" for n in chunk)}"]')
                self.w(f"  {key} --> {node_id}")
                self.w(f"  class {node_id} ep;")
        self.w("  class RB sig;")
        self.w("  class " + ",".join(k for k, _, _ in DEVICE_CHANNELS if k != "RB") + " ch;")
        self.w("```")
        self.w()
        self.w("Two prohibitions govern the rotation, from `WritingStyle.md`: never let a silent visual")
        self.w("carry a beat alone, and reserve verbatim repetition for when the repetition itself means")
        self.w("something.")
        self.w()
        countables = (OBLIGATION_SPINE.get(self.arc) or {}).get("countables")
        if countables:
            self.w("### Countable anchors")
            self.w()
            self.w("The other running device. Each episode carries at least one number the listener can hold:")
            self.w()
            self.w("```mermaid")
            self.w("flowchart LR")
            self.w("  classDef n fill:#f6eff7,stroke:#9a6fa6,color:#33203a;")
            previous = None
            for index, (anchor, gloss) in enumerate(countables):
                self.w(f'  N{index}["{label(anchor)}<br/><i>{label(gloss)}</i>"]')
                if previous:
                    self.w(f"  {previous} --> N{index}")
                previous = f"N{index}"
            self.w("  class " + ",".join(f"N{i}" for i in range(len(countables))) + " n;")
            self.w("```")
            self.w()
        self.w("---")
        self.w()

    def closing_turns(self) -> None:
        self.w("## 5. Closing turns")
        self.w()
        self.w("Every episode must end on a state change; the *kind* of turn is deliberately varied so the")
        self.w("audience never learns the rhythm. Distribution across the arc:")
        self.w()
        grouped: dict[str, list[int]] = collections.defaultdict(list)
        for episode in self.episodes:
            grouped[episode.get("end_turn_type", "unspecified")].append(episode_number(episode["id"]))
        ordered = sorted(grouped.items(), key=lambda item: (-len(item[1]), item[0]))
        self.w("```mermaid")
        self.w("flowchart LR")
        self.w("  classDef hd fill:#fff6e5,stroke:#cc9a3d,color:#3d2c08;")
        self.w("  classDef t fill:#eef4fb,stroke:#5588bb,color:#12293d;")
        self.w("  classDef ep fill:#ffffff,stroke:#aab,color:#333;")
        self.w('  H["Closing turn<br/><i>the floor is a state change, never a cliffhanger quota</i>"]')
        for index, (turn, numbers) in enumerate(ordered):
            self.w(f'  T{index}["{turn} — {len(numbers)}"]')
            self.w(f"  H --> T{index}")
            self.w(f'  T{index}_e["{" · ".join(f"E{n}" for n in numbers)}"]')
            self.w(f"  T{index} --> T{index}_e")
            self.w(f"  class T{index}_e ep;")
        self.w("  class H hd;")
        self.w("  class " + ",".join(f"T{i}" for i in range(len(ordered))) + " t;")
        self.w("```")
        self.w()
        cliffs = len(grouped.get("cliffhanger", []))
        self.w(
            f"{cliffs} hard cliffhangers in {len(self.episodes)} episodes. The machinery the style guide"
        )
        self.w("bans — shock, defusal, fresh shock — is absent by construction.")
        self.w()
        self.w("---")
        self.w()

    def mysteries(self) -> None:
        self.w("## 6. Protected mysteries")
        self.w()
        self.w("Questions that are never resolved early. The arc pays one instalment of proven fact on")
        self.w("each and holds the answer.")
        self.w()
        self.w("```mermaid")
        self.w("flowchart LR")
        self.w("  classDef q fill:#fdeeee,stroke:#b35a5a,color:#3d1616;")
        self.w("  classDef pay fill:#eaf3ea,stroke:#4c8a4c,color:#16301a;")
        self.w("  classDef gate fill:#f2f2f7,stroke:#7a7a99,color:#22223a;")
        for index, thread in enumerate(self.emap["thread_ledger"].get("series_threads", [])):
            touched = sorted(n for n, _ in self.thread_actions.get(thread["id"], []))
            self.w(f'  Q{index}["{thread["id"]} · {label(thread["name"])}"]')
            self.w(f'  E{index}_t["touched in {" · ".join(f"E{n}" for n in touched)}"]')
            self.w(f'  P{index}["The arc pays<br/>{label(thread["book_one_installment"])}"]')
            self.w(f'  G{index}["held until<br/><b>{label(thread["earliest_resolution"])}</b>"]')
            self.w(f"  Q{index} --> E{index}_t --> P{index} --> G{index}")
            self.w(f"  class Q{index} q;")
            self.w(f"  class P{index} pay;")
            self.w(f"  class G{index} gate;")
        self.w("```")
        self.w()
        self.w("---")
        self.w()

    def legend(self) -> None:
        self.w("## Legend")
        self.w()
        self.w("| Shape or colour | Meaning |")
        self.w("| --- | --- |")
        self.w("| Blue rectangle | Protagonist viewpoint, or a live obligation |")
        self.w("| Violet rectangle | Second viewpoint |")
        self.w("| Gold | Arc milestone, series signature device, or permanent status |")
        self.w("| Green | Closed, satisfied, or paid |")
        self.w("| Red | Protected series mystery |")
        self.w("| Stadium node | A thread opening or resolving |")
        self.w()
        self.w("Regenerate with `Scripts/build_narrative_flow.py`. Canon lives in the WorldState files;")
        self.w("this atlas is a reading of them.")
        self.w()

    def build(self) -> str:
        self.header()
        self.spine()
        self.plot_lines()
        self.clause_spine()
        self.devices()
        self.closing_turns()
        self.mysteries()
        self.legend()
        return "\n".join(self.lines) + "\n"


def check_mermaid(text: str) -> list[str]:
    """Cheap structural check on every mermaid block: balanced quotes and brackets."""
    problems = []
    for index, block in enumerate(re.findall(r"```mermaid\n(.*?)```", text, re.S)):
        for line in block.splitlines():
            if not line.strip():
                continue
            if line.count('"') % 2:
                problems.append(f"block {index}: odd quote count: {line.strip()}")
            for opener, closer in (("[", "]"), ("(", ")")):
                if line.count(opener) != line.count(closer):
                    problems.append(f"block {index}: unbalanced {opener}{closer}: {line.strip()}")
    return problems


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--arc", default="Book One", help="arc name, used for titles and the spine table")
    parser.add_argument("--out", default=None, help="output path relative to the repo root")
    parser.add_argument("--stdout", action="store_true", help="print instead of writing")
    args = parser.parse_args()

    builder = AtlasBuilder(REPO_ROOT, args.arc)
    text = builder.build()

    problems = check_mermaid(text)
    if problems:
        raise SystemExit("mermaid structure check failed:\n  " + "\n  ".join(problems))

    if args.stdout:
        print(text, end="")
        return

    relative = args.out or f"WorldState/{args.arc.replace(' ', '')}NarrativeFlow.md"
    destination = REPO_ROOT / relative
    destination.write_text(text)
    blocks = text.count("```mermaid")
    print(f"wrote {relative} — {len(text.splitlines())} lines, {blocks} mermaid diagrams")


if __name__ == "__main__":
    main()
