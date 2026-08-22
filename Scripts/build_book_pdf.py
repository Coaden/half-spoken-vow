#!/usr/bin/env python3
"""Build professional Book One PDF or EPUB editions with Calibre.

Title, author, cover, and output names come from the constants below. Set them once
when the series is named; the parsing conventions (episode filenames, headings, and
still timeline maps) are shared across projects and should not need changes.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "The-Half-Spoken-Vow"
EPISODES_DIR = ROOT / "Assets" / "Book One" / "Episodes"
EPISODE_MAP = ROOT / "WorldState" / "BookOneEpisodeMap.json"
COVER = ROOT / "Assets" / "Covers" / "EPUBCover.jpeg"
BUILD_DIR = ROOT / "tmp" / "pdfs" / SLUG.lower()
PDF_OUTPUT = ROOT / "output" / "pdf" / f"{SLUG}-Book-One.pdf"
EPUB_OUTPUT = ROOT / "Assets" / f"{SLUG}-Book-One.epub"

TITLE = "The Half-Spoken Vow"
SUBTITLE = "Book One"
AUTHOR = "Troy Locke"
SERIES = "The Half-Spoken Vow"
SERIES_INDEX = "1"
YEAR = "2026"


CSS = r"""
@page {
  size: 6in 9in;
  margin: 0.68in 0.64in 0.72in 0.68in;
}

html, body {
  color: #172126;
  background: #ffffff;
  font-family: "Athelas", "Baskerville", serif;
  font-size: 11pt;
  line-height: 1.48;
  text-rendering: optimizeLegibility;
}

body { margin: 0; padding: 0; }

.title-page, .copyright-page {
  page-break-after: always;
}

.title-page {
  min-height: 7.3in;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.title-rule {
  width: 1.05in;
  height: 2px;
  background: #75c9da;
  margin: 0 auto 0.34in auto;
}

.book-title {
  margin: 0;
  color: #13262e;
  font-family: "Avenir Next", "Helvetica Neue", sans-serif;
  font-size: 30pt;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.book-subtitle {
  margin: 0.18in 0 0 0;
  color: #5e7b86;
  font-family: "Avenir Next", "Helvetica Neue", sans-serif;
  font-size: 12pt;
  font-weight: 500;
  letter-spacing: 0.28em;
  text-transform: uppercase;
}

.author {
  margin-top: 1.2in;
  color: #263a42;
  font-family: "Avenir Next", "Helvetica Neue", sans-serif;
  font-size: 12pt;
  letter-spacing: 0.14em;
  text-transform: uppercase;
}

.copyright-page {
  min-height: 7.3in;
  font-size: 9pt;
  color: #45545a;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
}

.copyright-page p { margin: 0.08in 0; text-indent: 0; }

.contents h1 {
  margin: 0 0 0.3in 0;
  color: #13262e;
  font-family: "Avenir Next", "Helvetica Neue", sans-serif;
  font-size: 21pt;
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

.contents ol {
  margin: 0;
  padding: 0;
  list-style: none;
}

.contents li {
  break-inside: avoid;
  margin: 0 0 0.085in 0;
  font-family: "Avenir Next", "Helvetica Neue", sans-serif;
  font-size: 8.3pt;
  line-height: 1.25;
}

.contents a { color: #314f5b; text-decoration: none; }
.contents .toc-number { color: #6b8b96; font-weight: 600; }

h1.chapter-title::before {
  content: attr(data-chapter);
  display: block;
  margin-bottom: 0.13in;
  color: #608590;
  font-family: "Avenir Next", "Helvetica Neue", sans-serif;
  font-size: 8.5pt;
  font-weight: 600;
  letter-spacing: 0.22em;
  text-transform: uppercase;
}

h1.chapter-title {
  margin: 0.72in 0 0 0;
  color: #13262e;
  font-family: "Avenir Next", "Helvetica Neue", sans-serif;
  font-size: 22pt;
  font-weight: 600;
  line-height: 1.12;
  text-align: center;
}

.chapter-ornament {
  width: 0.55in;
  height: 2px;
  margin: 0.25in auto 0.48in auto;
  background: #d7ad35;
}

h2.episode-title {
  margin: 1.6em 0 0.85em 0;
  color: #263a42;
  font-family: "Avenir Next", "Helvetica Neue", sans-serif;
  font-size: 1.28em;
  font-weight: 700;
  line-height: 1.2;
  page-break-after: avoid;
  break-after: avoid;
}

h2.episode-title.first-episode { margin-top: 0; }

.prose p {
  margin: 0;
  text-align: justify;
  text-indent: 1.2em;
  widows: 2;
  orphans: 2;
}

.prose p.first { text-indent: 0; }
.prose p.first::first-letter {
  float: left;
  color: #284b58;
  font-family: "Avenir Next", "Helvetica Neue", sans-serif;
  font-size: 3.1em;
  font-weight: 600;
  line-height: 0.82;
  padding: 0.06em 0.08em 0 0;
}

.scene-break {
  margin: 0.22in 0;
  text-align: center;
  text-indent: 0 !important;
  color: #6b9aa8;
  font-family: "Avenir Next", sans-serif;
  letter-spacing: 0.35em;
}

em { font-style: italic; }
"""


def episode_number(path: Path) -> int:
    match = re.match(r"B1E(\d{2})-", path.name)
    if not match:
        raise ValueError(f"Unexpected episode filename: {path.name}")
    return int(match.group(1))


def inline_markdown(text: str) -> str:
    escaped = html.escape(text, quote=False)
    return re.sub(r"\*([^*]+)\*", r"<em>\1</em>", escaped)


def parse_episode(path: Path) -> tuple[str, str, list[str]]:
    raw = path.read_text(encoding="utf-8").strip()
    blocks = [block.strip() for block in re.split(r"\n\s*\n", raw) if block.strip()]
    if not blocks or not blocks[0].startswith("# "):
        raise ValueError(f"Missing episode heading: {path}")
    heading = blocks.pop(0)[2:].strip()
    match = re.match(r"Episode ([^:]+):\s*(.+)", heading)
    if not match:
        raise ValueError(f"Unexpected episode heading: {heading}")
    # Episode masters repeat the spoken title for Pocket FM orientation. The
    # ebook chapter heading already carries it, so omit that duplicate line.
    if blocks and blocks[0] == heading:
        blocks.pop(0)
    return match.group(1), match.group(2), blocks


def paragraph_html(block: str, first: bool) -> str:
    if block in {"---", "***", "* * *"}:
        return '<p class="scene-break">&#9671;</p>'
    joined = " ".join(line.strip() for line in block.splitlines())
    cls = ' class="first"' if first else ""
    return f"<p{cls}>{inline_markdown(joined)}</p>"


CHAPTER_WORDS = (
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
    "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
    "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty",
    "Twenty-One", "Twenty-Two", "Twenty-Three", "Twenty-Four",
)


def load_chapter_anchors() -> list[dict[str, object]]:
    data = json.loads(EPISODE_MAP.read_text(encoding="utf-8"))
    anchors = data.get("chapter_anchors")
    if not isinstance(anchors, list) or len(anchors) != 24:
        raise ValueError("Episode map must contain exactly 24 chapter anchors")
    return anchors


def build_html(episodes: list[Path]) -> str:
    parsed = {}
    for path in episodes:
        number = episode_number(path)
        number_word, title, blocks = parse_episode(path)
        parsed[f"B1E{number:02d}"] = (number, number_word, title, blocks)

    anchors = load_chapter_anchors()
    mapped_ids = [episode_id for anchor in anchors for episode_id in anchor["episodes"]]
    expected_ids = [f"B1E{number:02d}" for number in range(1, 61)]
    if mapped_ids != expected_ids:
        raise ValueError("Chapter anchors must map B1E01 through B1E60 exactly once and in order")

    toc_items = "\n".join(
        f'<li><a href="#chapter-{index:02d}"><span class="toc-number">'
        f'{index:02d}</span>&nbsp; {html.escape(str(anchor["title"]))}</a></li>'
        for index, anchor in enumerate(anchors, 1)
    )

    chapter_sections = []
    for chapter_number, anchor in enumerate(anchors, 1):
        content = []
        first_prose = True
        for episode_position, episode_id in enumerate(anchor["episodes"]):
            number, _, episode_title, blocks = parsed[episode_id]
            first_class = " first-episode" if episode_position == 0 else ""
            content.append(
                f'<h2 class="episode-title{first_class}" id="episode-{number:02d}">'
                f'{html.escape(episode_title)}</h2>'
            )
            for block in blocks:
                content.append(paragraph_html(block, first_prose))
                if block not in {"---", "***", "* * *"}:
                    first_prose = False

        chapter_sections.append(
            f'''<section class="book-chapter">
  <h1 class="chapter-title" id="chapter-{chapter_number:02d}" data-chapter="Chapter {CHAPTER_WORDS[chapter_number - 1]}">{html.escape(str(anchor["title"]))}</h1>
  <div class="chapter-ornament"></div>
  <div class="prose">{"".join(content)}</div>
</section>'''
        )

    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>{TITLE}</title>
  <meta name="author" content="{AUTHOR}" />
  <style>{CSS}</style>
</head>
<body>
  <section class="title-page">
    <div class="title-rule"></div>
    <div class="book-title">{TITLE}</div>
    <div class="book-subtitle">{SUBTITLE}</div>
    <div class="author">{AUTHOR}</div>
  </section>
  <section class="copyright-page">
    <p><strong>{TITLE}</strong></p>
    <p>Copyright &#169; {YEAR} {AUTHOR}. All rights reserved.</p>
    <p>No part of this publication may be reproduced, distributed, or transmitted in any form or by any means without prior written permission from the copyright holder, except as permitted by law.</p>
    <p>First edition.</p>
    <p>This is a work of fiction. Names, characters, places, and incidents are products of the author’s imagination or are used fictitiously.</p>
  </section>
  <nav class="contents">
    <h1>Contents</h1>
    <ol>{toc_items}</ol>
  </nav>
  {"".join(chapter_sections)}
</body>
</html>'''


def run(command: list[str]) -> None:
    print("Running:", " ".join(command))
    subprocess.run(command, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--format", choices=("pdf", "epub"), default="pdf", help="Output edition to build")
    parser.add_argument("--keep-build", action="store_true", help="Keep generated HTML source")
    args = parser.parse_args()
    output = PDF_OUTPUT if args.format == "pdf" else EPUB_OUTPUT

    episodes = sorted(EPISODES_DIR.glob("B1E??-*.md"), key=episode_number)
    if len(episodes) != 60:
        raise RuntimeError(f"Expected 60 episode manuscripts, found {len(episodes)}")
    if not COVER.exists():
        raise FileNotFoundError(COVER)

    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)
    BUILD_DIR.mkdir(parents=True)
    output.parent.mkdir(parents=True, exist_ok=True)

    source_html = BUILD_DIR / f"{SLUG}-Book-One.html"
    source_html.write_text(build_html(episodes), encoding="utf-8")

    command = [
        "ebook-convert",
        str(source_html),
        str(output),
        "--title", TITLE,
        "--authors", AUTHOR,
        "--series", SERIES,
        "--series-index", SERIES_INDEX,
        "--language", "en",
        "--publisher", AUTHOR,
        "--cover", str(COVER),
        "--preserve-cover-aspect-ratio",
        "--chapter", "//h:h1[@class='chapter-title']",
        "--level1-toc", "//h:h1[@class='chapter-title']",
        # Calibre's HTML input otherwise inserts page breaks before generic
        # h1/h2 elements. Only the 24 mapped macro chapters should break;
        # episode h2 headings remain inline within their parent chapters.
        "--page-breaks-before", "/",
        "--toc-threshold", "0",
        "--max-toc-links", "100",
        "--pretty-print",
    ]
    if args.format == "pdf":
        command.extend([
            "--custom-size", "6x9",
            "--unit", "inch",
            "--pdf-serif-family", "Athelas",
            "--pdf-sans-family", "Avenir Next",
            "--pdf-standard-font", "serif",
            "--pdf-default-font-size", "16",
            "--pdf-page-margin-left", "48",
            "--pdf-page-margin-right", "44",
            "--pdf-page-margin-top", "46",
            "--pdf-page-margin-bottom", "48",
            "--pdf-odd-even-offset", "3",
            "--pdf-footer-template", '<div style="font-family: Avenir Next; font-size: 8pt; color: #718088; text-align: center; opacity: _PAGENUM_;">_PAGENUM_</div>',
            "--pdf-page-number-map", "if (n < 5) 0; else n - 4;",
        ])
    else:
        command.extend([
            "--epub-version", "3",
            "--output-profile", "kindle",
            "--flow-size", "0",
            "--chapter-mark", "pagebreak",
        ])
    run(command)

    if not args.keep_build:
        shutil.rmtree(BUILD_DIR)
    print(f"Created {output}")


if __name__ == "__main__":
    main()
