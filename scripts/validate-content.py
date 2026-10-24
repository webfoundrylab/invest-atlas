#!/usr/bin/env python3
"""Validate the Invest Atlas editorial registry and generated internal links."""
import json
import re
import sys
from pathlib import Path
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
BASE_URL = "https://webfoundrylab.github.io/invest-atlas/"
errors = []
try:
    registry = json.loads((ROOT / "article-index.json").read_text(encoding="utf-8"))
except Exception as exc:
    print(f"ERROR: cannot parse article-index.json: {exc}")
    sys.exit(1)

categories = {item["id"]: item for item in registry.get("categories", [])}
articles = registry.get("articles", [])

def taxonomy_paths(items, prefix=()):
    paths = {}
    for node in items:
        path = prefix + (node["id"],)
        paths[path] = node
        paths.update(taxonomy_paths(node.get("children", []), path))
    return paths

taxonomy = taxonomy_paths(registry.get("categories", []))
category_base = BASE_URL + "categories/"
def article_category_path(item):
    return tuple(value for value in (item.get("category"), item.get("subcategory"), item.get("topic")) if value)
by_slug = {}
for item in articles:
    slug = item.get("slug", "")
    if not slug:
        errors.append("article entry is missing slug")
        continue
    if "/" in slug or "\\" in slug or slug in {".", ".."}:
        errors.append(f"unsafe article slug: {slug!r}")
    if slug in by_slug:
        errors.append(f"duplicate slug: {slug}")
    by_slug[slug] = item
    if item.get("category") not in categories:
        errors.append(f"{slug}: unknown category {item.get('category')!r}")
    path = article_category_path(item)
    if path and path not in taxonomy:
        errors.append(f"{slug}: unknown category hierarchy path {path!r}")
    elif path and path[0] != item.get("category"):
        errors.append(f"{slug}: hierarchy path does not begin with category")
    if not (ROOT / slug).is_file():
        errors.append(f"{slug}: article file does not exist")
    tags = item.get("tags", [])
    if not isinstance(tags, list) or any(not isinstance(tag, str) or not tag.strip() for tag in tags):
        errors.append(f"{slug}: tags must be an array of non-empty strings")
    elif len(tags) != len(set(tags)):
        errors.append(f"{slug}: duplicate tags")
    if item.get("status") == "published":
        for field in ("title", "summary"):
            if not item.get(field):
                errors.append(f"{slug}: published article missing {field}")

for item in articles:
    slug = item.get("slug", "")
    for related in item.get("related", []):
        if related not in by_slug:
            errors.append(f"{slug}: related article not in registry: {related}")
        elif related == slug:
            errors.append(f"{slug}: article cannot relate to itself")
        elif by_slug[related].get("status") != "published":
            errors.append(f"{slug}: related article is not published: {related}")
        elif not (ROOT / related).is_file():
            errors.append(f"{slug}: related article file missing: {related}")

try:
    sitemap_root = ElementTree.fromstring((ROOT / "sitemap.xml").read_text(encoding="utf-8"))
    published = [item for item in articles if item.get("status") == "published"]
    expected_urls = {BASE_URL} | {BASE_URL + item["slug"] for item in published}
    for path in taxonomy:
        if any(article_category_path(article)[:len(path)] == path for article in published):
            expected_urls.add(category_base + "/".join(path) + "/")
    actual_urls = {node.text for node in sitemap_root.iter() if node.tag.endswith("loc")}
    for url in sorted(expected_urls - actual_urls):
        errors.append(f"sitemap missing URL: {url}")
    for url in sorted(actual_urls - expected_urls):
        errors.append(f"sitemap contains unregistered URL: {url}")
except Exception as exc:
    errors.append(f"cannot parse sitemap.xml: {exc}")

for item in articles:
    if item.get("status") != "published":
        continue
    try:
        page = (ROOT / item["slug"]).read_text(encoding="utf-8")
        has_generated = "<!-- GENERATED RELATED ARTICLES: START -->" in page and "<!-- GENERATED RELATED ARTICLES: END -->" in page
        existing_links = set(re.findall(r"""href=["']([^"']+)["']""", page, flags=re.IGNORECASE))
        has_registry_related = any(link in by_slug and link != item["slug"] for link in existing_links)
        if not has_generated and not has_registry_related:
            errors.append(f"{item['slug']}: no generated or existing internal related links found")
    except Exception as exc:
        errors.append(f"{item['slug']}: cannot read article HTML: {exc}")

if errors:
    print("Content validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"Content validation passed: {len(articles)} registered articles, {sum(a.get('status') == 'published' for a in articles)} published; hierarchical categories checked.")
