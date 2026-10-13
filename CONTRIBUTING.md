# Contributing

This daily feed focuses on **efficient LLMs and visual generation**.

- Edit `config.json` to refine search phrases or add a topic. Each `groups` array
  means AND between groups and OR between phrases within a group. Searches cover
  titles and abstracts; `scope_terms` and `arxiv_categories` constrain the field.
- Submit missed papers or false positives through an issue with the arXiv URL.
- Do not edit generated README tables, `docs/papers.json`, or archive pages by hand.
- Run `python -m unittest discover -s tests -v` before changing the collector.

The collector uses only the Python 3.11+ standard library. No model API key is needed.
