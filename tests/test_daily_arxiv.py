import copy
import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

from daily_arxiv import ROOT, build_query, collect, contains_phrase, merge, parse_feed, relevant, run

CONFIG = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))
NOW = datetime(2026, 10, 13, 2, tzinfo=timezone.utc)
FEED = b'''<feed xmlns="http://www.w3.org/2005/Atom" xmlns:os="http://a9.com/-/spec/opensearch/1.1/">
<os:totalResults>1</os:totalResults><entry><id>http://arxiv.org/abs/2610.00001v2</id>
<title>Fast &amp; Low-Bit LLM Quantization</title><summary>A language model with quantization.
Code: https://github.com/example/model.</summary><published>2026-10-01T00:00:00Z</published>
<updated>2026-10-12T00:00:00Z</updated><author><name>Example Author</name></author>
<category term="cs.LG"/></entry></feed>'''


class CollectorTests(unittest.TestCase):
    def paper(self):
        return parse_feed(FEED)[0][0]

    def test_parse_versions_code_and_original_date(self):
        papers, total = parse_feed(FEED)
        self.assertEqual(total, 1)
        self.assertEqual(papers[0]["id"], "2610.00001")
        self.assertEqual(papers[0]["versioned_id"], "2610.00001v2")
        self.assertEqual(papers[0]["published"], "2026-10-01T00:00:00Z")
        self.assertEqual(papers[0]["code_urls"], ["https://github.com/example/model"])

    def test_invalid_feed_is_not_a_successful_empty_search(self):
        for payload in (b"<html>maintenance</html>", b'<feed xmlns="http://www.w3.org/2005/Atom"/>'):
            with self.assertRaises(ValueError):
                parse_feed(payload)

    def test_domain_and_word_boundaries(self):
        p = self.paper()
        self.assertTrue(relevant(p, CONFIG["topics"][0], CONFIG))
        p.update(title="Quantization of lattice gauge fields", abstract="A study of credit market quantization.")
        self.assertFalse(relevant(p, CONFIG["topics"][0], CONFIG))
        self.assertFalse(contains_phrase("credit", "DiT"))
        self.assertTrue(contains_phrase("key–value cache", "key-value cache"))

    def test_visual_generation_needs_an_efficiency_signal(self):
        p = self.paper()
        p.update(title="Better video generation", abstract="We study video generation and realism.")
        self.assertFalse(relevant(p, CONFIG["topics"][-1], CONFIG))
        p["abstract"] += " We propose sparse attention for efficient video generation."
        self.assertTrue(relevant(p, CONFIG["topics"][-1], CONFIG))

    def test_application_only_mention_does_not_make_efficiency_paper(self):
        p = self.paper()
        p.update(title="A language model for relation extraction",
                 abstract="We study relation extraction using a language model. LoRA is used for fine-tuning.")
        self.assertFalse(relevant(p, CONFIG["topics"][3], CONFIG))
        p["title"] = "Memory-efficient LoRA for language models"
        self.assertTrue(relevant(p, CONFIG["topics"][3], CONFIG))

    def test_non_target_generative_domains_excluded(self):
        p = self.paper()
        p.update(title="Accelerated MRI reconstruction with diffusion",
                 abstract="We introduce caching for diffusion acceleration.")
        self.assertFalse(relevant(p, CONFIG["topics"][-2], CONFIG))

    def test_dedup_preserves_first_seen_and_latest_version(self):
        p = self.paper()
        first = merge({"papers": []}, {p["id"]: p}, NOW, CONFIG, [])
        newer = copy.deepcopy(p)
        newer.update(versioned_id="2610.00001v3", updated="2026-10-14T00:00:00Z")
        next_day = datetime(2026, 10, 14, 2, tzinfo=timezone.utc)
        second = merge(first, {p["id"]: newer}, next_day, CONFIG, [])
        self.assertEqual(len(second["papers"]), 1)
        self.assertEqual(second["papers"][0]["first_seen"], "2026-10-13")
        stale = merge(second, {p["id"]: p}, next_day, CONFIG, [])
        self.assertEqual(stale["papers"][0]["versioned_id"], "2610.00001v3")
        self.assertEqual(stale["papers"][0]["published"], p["published"])

    def test_empty_search_preserves_archive(self):
        p = self.paper()
        old = merge({"papers": []}, {p["id"]: p}, NOW, CONFIG, [])
        self.assertEqual(merge(old, {}, NOW, CONFIG, [])["papers"], old["papers"])

    def test_pagination_and_result_cap(self):
        config = copy.deepcopy(CONFIG)
        config["topics"] = config["topics"][:1]
        config["page_size"] = 1
        p = self.paper()
        class TwoPages:
            def fetch(self, query, start, count):
                return [{**p, "id": "2610.0000" + str(start + 1)}], 2
        found, stats = collect(config, TwoPages(), NOW, NOW)
        self.assertEqual(len(found), 2)
        config["max_results_per_topic"] = 1
        with self.assertRaisesRegex(RuntimeError, "exceed"):
            collect(config, TwoPages(), NOW, NOW)

    def test_failed_topic_does_not_modify_any_published_file(self):
        class Broken:
            def fetch(self, *args):
                raise RuntimeError("temporary API failure")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "config.json").write_text(json.dumps(CONFIG), encoding="utf-8")
            (root / "data").mkdir()
            (root / "data/papers.json").write_text('{"papers": []}', encoding="utf-8")
            (root / "README.md").write_text("existing archive", encoding="utf-8")
            before = {p: p.read_bytes() for p in root.rglob("*") if p.is_file()}
            with self.assertRaises(RuntimeError):
                run(root, client=Broken(), now=NOW)
            for path, contents in before.items():
                self.assertEqual(path.read_bytes(), contents)

    def test_incomplete_pagination_fails(self):
        class MissingPage:
            def fetch(self, *args):
                return [], 100
        with self.assertRaisesRegex(RuntimeError, "incomplete"):
            collect(CONFIG, MissingPage(), NOW, NOW)

    def test_incremental_query_includes_scope_and_updated_range(self):
        q = build_query(CONFIG["topics"][0], CONFIG, NOW, NOW)
        self.assertIn("lastUpdatedDate:[202610130200 TO 202610130200]", q)
        self.assertIn('abs:"language model"', q)
        self.assertIn("cat:cs.CV", q)


if __name__ == "__main__":
    unittest.main()
