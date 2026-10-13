#!/usr/bin/env python3
"""Collect efficient LLM / visual generation papers using the official arXiv API.

All topics must succeed before any generated file is replaced. Paper identities
are version-independent, and historical entries survive empty API results.
"""
from __future__ import annotations

import argparse
import copy
import html
import json
import logging
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent
API = "https://export.arxiv.org/api/query"
NS = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom",
      "os": "http://a9.com/-/spec/opensearch/1.1/"}
LOG = logging.getLogger("arxiv-daily")


def read_json(path: Path, default=None):
    if not path.exists():
        return copy.deepcopy(default)
    return json.loads(path.read_text(encoding="utf-8"))


def atomic_write(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(content, encoding="utf-8", newline="\n")
    os.replace(tmp, path)


def normalized(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def contains_phrase(text: str, phrase: str) -> bool:
    # Boundary checks keep "DiT" from matching "credit" and "LLM" from "allman".
    return f" {normalized(phrase)} " in f" {normalized(text)} "


def relevant(paper: dict, topic: dict, config: dict) -> bool:
    text = paper["title"] + " " + paper["abstract"]
    if any(contains_phrase(paper["title"], p) for p in config.get("exclude_title_terms", [])):
        return False
    in_scope = (any(contains_phrase(text, p) for p in config["scope_terms"])
                and all(any(contains_phrase(text, p) for p in group)
                        for group in topic["groups"]))
    if not in_scope:
        return False
    # The final group contains method/efficiency phrases; earlier groups are
    # model domains. A passing mention of LoRA in an application is insufficient.
    methods = topic["groups"][-1]
    title_focus = any(contains_phrase(paper["title"], p)
                      for p in methods + config.get("focus_terms", []))
    if title_focus:
        return True
    # Keep method papers with an opaque title when a contribution sentence
    # explicitly connects the method to computational efficiency.
    sentences = re.split(r"(?<=[.!?])\s+", paper["abstract"])
    for sentence in sentences:
        contribution = re.search(r"\b(we (propose|introduce|present|develop)|this (paper|work) (proposes|introduces|presents))\b", sentence, re.I)
        if (contribution and any(contains_phrase(sentence, p) for p in methods)
                and any(contains_phrase(sentence, p) for p in config.get("focus_terms", []))):
            return True
    return False


def phrase_query(terms: list[str]) -> str:
    parts = []
    for term in terms:
        if '"' in term or "\n" in term:
            raise ValueError("Search phrases must not contain quotes or newlines")
        parts.extend([f'ti:"{term}"', f'abs:"{term}"'])
    return "(" + " OR ".join(parts) + ")"


def build_query(topic: dict, config: dict, start: datetime, end: datetime) -> str:
    parts = ["(" + " OR ".join("cat:" + c for c in config["arxiv_categories"]) + ")",
             phrase_query(config["scope_terms"])]
    parts.extend(phrase_query(group) for group in topic["groups"])
    # updatedDate retrieves newly submitted AND revised papers. A seven-day
    # overlap also recovers records indexed late by arXiv.
    parts.append(f"lastUpdatedDate:[{start:%Y%m%d%H%M} TO {end:%Y%m%d%H%M}]")
    return " AND ".join(parts)


def parse_feed(payload: bytes) -> tuple[list[dict], int]:
    feed = ET.fromstring(payload)
    if feed.tag != f"{{{NS['atom']}}}feed":
        raise ValueError("arXiv returned a non-Atom response")
    total_text = feed.findtext("os:totalResults", namespaces=NS)
    if total_text is None:
        raise ValueError("arXiv response has no totalResults (possibly an API error)")
    records = []
    for entry in feed.findall("atom:entry", NS):
        raw_id = entry.findtext("atom:id", "", NS)
        if "/abs/" not in raw_id:
            raise ValueError("arXiv returned an error or invalid paper ID")
        versioned = raw_id.split("/abs/", 1)[1]
        paper_id = re.sub(r"v\d+$", "", versioned)
        title = " ".join(entry.findtext("atom:title", "", NS).split())
        abstract = " ".join(entry.findtext("atom:summary", "", NS).split())
        published = entry.findtext("atom:published", "", NS)
        updated = entry.findtext("atom:updated", "", NS)
        if not title or not abstract or not published or not updated:
            raise ValueError(f"Incomplete paper metadata: {paper_id}")
        comment = entry.findtext("arxiv:comment", "", NS)
        links = re.findall(r"https?://[^\s<>\"{}\\]+", abstract + " " + comment)
        code = sorted({url.rstrip(".,;:)") for url in links
                       if urllib.parse.urlsplit(url).hostname in {"github.com", "gitlab.com", "huggingface.co"}})
        records.append({
            "id": paper_id, "versioned_id": versioned, "title": title,
            "authors": [" ".join(a.findtext("atom:name", "", NS).split())
                        for a in entry.findall("atom:author", NS)],
            "published": published, "updated": updated, "abstract": abstract,
            "arxiv_categories": [c.attrib["term"] for c in entry.findall("atom:category", NS)],
            "url": f"https://arxiv.org/abs/{paper_id}",
            "pdf_url": f"https://arxiv.org/pdf/{paper_id}", "code_urls": code,
            "comment": comment, "journal_ref": entry.findtext("arxiv:journal_ref", "", NS),
        })
    return records, int(total_text)


class ArxivClient:
    def __init__(self, repository: str):
        self.user_agent = f"EfficientAIArxivDaily/1.0 (https://github.com/{repository})"
        self.last_request = 0.0

    def fetch(self, query: str, start: int, count: int) -> tuple[list[dict], int]:
        params = urllib.parse.urlencode({"search_query": query, "start": start,
                                       "max_results": count, "sortBy": "lastUpdatedDate",
                                       "sortOrder": "descending"})
        request = urllib.request.Request(API + "?" + params,
                                         headers={"User-Agent": self.user_agent})
        for attempt in range(5):
            time.sleep(max(0, 3.2 - (time.monotonic() - self.last_request)))
            self.last_request = time.monotonic()
            try:
                with urllib.request.urlopen(request, timeout=60) as response:
                    return parse_feed(response.read())
            except urllib.error.HTTPError as exc:
                if exc.code not in {429, 500, 502, 503, 504}:
                    raise
                retry_after = exc.headers.get("Retry-After", "")
                delay = min(60, int(retry_after)) if retry_after.isdigit() else 5 * 2**attempt
                LOG.warning("arXiv HTTP %s; attempt %s/5", exc.code, attempt + 1)
            except (urllib.error.URLError, TimeoutError, ET.ParseError) as exc:
                LOG.warning("arXiv request failed (%s); attempt %s/5", type(exc).__name__, attempt + 1)
                delay = 5 * 2**attempt
            if attempt < 4:
                time.sleep(min(delay, 60))
        raise RuntimeError("arXiv unavailable after retries; existing data was preserved")


def collect(config: dict, client, start: datetime, end: datetime) -> tuple[dict, list[dict]]:
    found, stats = {}, []
    for topic in config["topics"]:
        query = build_query(topic, config, start, end)
        offset, accepted, total = 0, set(), 0
        while True:
            records, total = client.fetch(query, offset, config["page_size"])
            if total > config["max_results_per_topic"]:
                raise RuntimeError(f"{topic['id']}: {total} results exceed the configured cap; "
                                   "use a shorter backfill window or increase max_results_per_topic")
            if not records and offset < total:
                raise RuntimeError(f"{topic['id']}: incomplete API pagination; preserving archive")
            for paper in records:
                if relevant(paper, topic, config):
                    existing = found.get(paper["id"])
                    categories = set(existing.get("topics", [])) if existing else set()
                    categories.add(topic["id"])
                    if existing and existing["updated"] > paper["updated"]:
                        paper = existing
                    found[paper["id"]] = {**paper, "topics": sorted(categories)}
                    accepted.add(paper["id"])
            offset += len(records)
            if offset >= total:
                break
        stats.append({"topic": topic["id"], "api_results": total, "accepted": len(accepted)})
        LOG.info("%-24s %4d results / %4d in scope", topic["id"], total, len(accepted))
    return found, stats


def merge(old: dict, found: dict, now: datetime, config: dict, stats: list) -> dict:
    today = now.astimezone(ZoneInfo(config["timezone"])).date().isoformat()
    papers = {p["id"]: copy.deepcopy(p) for p in old.get("papers", [])}
    for paper_id, item in found.items():
        previous = papers.get(paper_id)
        if previous and previous["updated"] > item["updated"]:
            continue  # A stale API page must not downgrade a newer version.
        paper = copy.deepcopy(item)
        paper["first_seen"] = previous["first_seen"] if previous else today
        papers[paper_id] = paper
    # Reclassify the entire archive when search rules change; preserve metadata.
    for paper in papers.values():
        paper["topics"] = [t["id"] for t in config["topics"] if relevant(paper, t, config)]
    active = sorted(papers.values(), key=lambda p: (p["published"], p["id"]), reverse=True)
    return {"schema_version": 1, "last_success_utc": now.isoformat(),
            "last_scan_date": today, "last_scan_stats": stats, "papers": active}


def escaped(value: str) -> str:
    return html.escape(value, quote=True).replace("|", "&#124;").replace("\n", " ")


def paper_table(papers: list[dict]) -> str:
    rows = ["| Published | Paper & authors | Links |", "|:---|:---|:---|"]
    for p in papers:
        authors = ", ".join(p["authors"][:3]) + (" et al." if len(p["authors"]) > 3 else "")
        links = f"[arXiv]({p['url']}) · [PDF]({p['pdf_url']})"
        if p["code_urls"]:
            safe = urllib.parse.quote(p["code_urls"][0], safe=":/?=&%#@-._~+")
            links += f" · [Code]({safe})"
        rows.append(f"| {p['published'][:10]} | **{escaped(p['title'])}**<br><sub>{escaped(authors)}</sub> | {links} |")
    return "\n".join(rows)


def render(state: dict, config: dict, root: Path):
    papers = [p for p in state["papers"] if p["topics"]]
    today = state["last_scan_date"]
    new = [p for p in papers if p["first_seen"] == today]
    repo = config["repository"]
    owner, name = repo.split("/")
    site = f"https://{owner}.github.io/{name}/"
    stamp = datetime.fromisoformat(state["last_success_utc"]).astimezone(ZoneInfo(config["timezone"])).strftime("%Y-%m-%d %H:%M %Z")
    newest = max((p["published"][:10] for p in papers), default="—")
    content = [f"# ⚡ {config['title']}", "",
               "**Efficient LLMs · Efficient Visual Generation**", "",
               "自动追踪 LLM 与图像/视频生成的加速、压缩和高效训练论文。", "",
               f"[![Daily update](https://github.com/{repo}/actions/workflows/daily.yml/badge.svg)](https://github.com/{repo}/actions/workflows/daily.yml) "
               "[![License: MIT](https://img.shields.io/badge/License-MIT-45b8a0.svg)](LICENSE)", "",
               f"**[Browse & search papers ↗]({site})** · [Atom feed]({site}feed.xml) · [Search configuration](config.json) · [All paper metadata](data/papers.json)", "",
               f"Last successful scan: **{stamp}** · **{len(papers)} unique papers** · Newest submission: **{newest}**", "",
               "> Dates below are original arXiv submission dates. The scan time is shown separately. "
               "A paper can belong to multiple topics; topic counts overlap.", "",
               "## Topics", "", "| Topic | Scope | Papers |", "|:---|:---|---:|"]
    for topic in config["topics"]:
        subset = [p for p in papers if topic["id"] in p["topics"]]
        content.append(f"| [{topic['name']}](#{topic['id']}) | {topic['description']} | {len(subset)} |")
        archive = f"# {topic['name']}\n\n{topic['description']}\n\n[← Home](../README.md) · [Search online]({site}?topic={topic['id']})\n\n{len(subset)} papers · newest submission first\n\n" + paper_table(subset) + "\n"
        atomic_write(root / "papers" / f"{topic['id']}.md", archive)
    content.extend(["", f"## Newly indexed · {today}", "",
                    "These papers were first added to this repository today. The initial import includes older papers within the backfill window.", "",
                    paper_table(new[:20]) if new else "No newly indexed papers in this scan."])
    if len(new) > 20:
        content.append(f"\n[View all {len(new)} newly indexed papers]({site}?new=1).")
    for topic in config["topics"]:
        subset = [p for p in papers if topic["id"] in p["topics"]]
        content.extend(["", f'<a id="{topic["id"]}"></a>', "", f"## {topic['name']}", "",
                        f"{topic['description']} · **{len(subset)} papers** · [Full archive](papers/{topic['id']}.md)", "",
                        paper_table(subset[:config["readme_per_topic"]]) if subset else "No matching papers indexed yet."])
    content.extend(["", "## How it works", "",
                    "- Runs daily at **09:17 Asia/Shanghai (01:17 UTC)** using GitHub Actions. Scheduled starts can be delayed by GitHub.",
                    "- Queries the official arXiv API across titles and abstracts, then applies domain and efficiency-focus filters. A method or efficiency signal must appear in the title, or a contribution sentence must connect the method to efficiency. No paid AI API is used.",
                    "- Initial import: the last **30 days** of new or revised records. Later runs catch up from the previous successful scan, with a **7-day overlap** for delayed indexing.",
                    "- Deduplicates arXiv versions, preserves original submission dates, keeps history, and extracts code links when present in abstracts/comments.",
                    "- Any failed topic, malformed response, or truncated pagination fails the run before publishing. Empty successful searches do not erase the archive.",
                    "- **Automatic discovery, not a completeness or quality guarantee.** Keywords can miss papers or include weak matches. Summaries on the website are original arXiv abstracts.", "",
                    "## Customize or run locally", "", "Requires **Python 3.11+**, with no third-party dependencies.", "",
                    "```bash", "python -m unittest discover -s tests -v", "python daily_arxiv.py", "python daily_arxiv.py --days 60  # explicit backfill", "python daily_arxiv.py --render-only  # rebuild from saved data", "```", "",
                    "Edit `config.json` to change topic phrases. Within each topic, groups are joined with AND; phrases within a group are joined with OR. "
                    "The **Actions → Update papers → Run workflow** button also supports a custom backfill window. "
                    "If the result cap is reached, use a shorter window or raise the configured cap; the collector never silently truncates results.", "",
                    "GitHub may disable scheduled workflows in public repositories after 60 days without repository activity. If disabled, re-enable the workflow in Actions.", "",
                    "## Credits", "",
                    "Inspired by [cv-arxiv-daily](https://github.com/Vincentqyw/cv-arxiv-daily) and "
                    "[Watermarking-arxiv-daily](https://github.com/ai-kunkun/Watermarking-arxiv-daily). "
                    "Collector and website implemented independently. Thank you to arXiv for its open metadata API.", ""])
    atomic_write(root / "README.md", "\n".join(content))
    public = {"title": config["title"], "repository": repo, "updated": stamp,
              "scan_date": today, "newest_submission": newest,
              "topics": [{k: t[k] for k in ("id", "name", "description")} for t in config["topics"]],
              "papers": papers}
    atomic_write(root / "docs" / "papers.json", json.dumps(public, ensure_ascii=False, indent=2) + "\n")
    ET.register_namespace("", NS["atom"])
    tag = lambda name: f"{{{NS['atom']}}}{name}"
    feed = ET.Element(tag("feed"))
    for key, value in [("title", config["title"]), ("id", site), ("updated", state["last_success_utc"])]:
        ET.SubElement(feed, tag(key)).text = value
    ET.SubElement(feed, tag("link"), {"href": site})
    ET.SubElement(feed, tag("link"), {"href": site + "feed.xml", "rel": "self"})
    author = ET.SubElement(feed, tag("author"))
    ET.SubElement(author, tag("name")).text = owner
    for p in papers[:50]:
        item = ET.SubElement(feed, tag("entry"))
        for key, value in [("id", p["url"]), ("title", p["title"]), ("updated", p["updated"]),
                           ("published", p["published"]), ("summary", p["abstract"])]:
            ET.SubElement(item, tag(key)).text = value
        ET.SubElement(item, tag("link"), {"href": p["url"]})
    atomic_write(root / "docs" / "feed.xml", ET.tostring(feed, encoding="unicode", xml_declaration=True) + "\n")


def run(root: Path, days: int | None = None, render_only: bool = False, client=None, now=None):
    config = read_json(root / "config.json")
    old = read_json(root / "data" / "papers.json", {"papers": []})
    if render_only:
        if not old.get("last_success_utc"):
            raise ValueError("No successful collection to render")
        render(old, config, root)
        return old
    now = now or datetime.now(timezone.utc)
    if days is not None:
        if not 1 <= days <= 3660:
            raise ValueError("days must be between 1 and 3660")
        start = now - timedelta(days=days)
    elif old.get("last_success_utc"):
        start = datetime.fromisoformat(old["last_success_utc"]) - timedelta(days=config["overlap_days"])
    else:
        start = now - timedelta(days=config["bootstrap_days"])
    LOG.info("Scanning %s through %s", start.isoformat(), now.isoformat())
    found, stats = collect(config, client or ArxivClient(config["repository"]), start, now)
    if not found and not old["papers"]:
        raise RuntimeError("Initial import returned no in-scope papers; refusing to publish an empty feed")
    state = merge(old, found, now, config, stats)
    render(state, config, root)
    atomic_write(root / "data" / "papers.json", json.dumps(state, ensure_ascii=False, indent=2) + "\n")
    active = [p for p in state["papers"] if p["topics"]]
    new_count = sum(p["first_seen"] == state["last_scan_date"] for p in active)
    LOG.info("Saved %s papers; %s first indexed today", len(active), new_count)
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as out:
            out.write(f"## Efficient AI arXiv Daily\n\n{len(active)} indexed papers · {new_count} newly indexed today.\n\n")
            out.write("| Topic | API records | In scope |\n|---|---:|---:|\n")
            for s in stats:
                out.write(f"| {s['topic']} | {s['api_results']} | {s['accepted']} |\n")
    return state


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--days", type=int, help="Override the incremental window for an explicit backfill")
    parser.add_argument("--render-only", action="store_true")
    args = parser.parse_args()
    run(ROOT, days=args.days, render_only=args.render_only)
