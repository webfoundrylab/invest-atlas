#!/usr/bin/env python3
"""Validate the Invest Atlas editorial registry and published internal links."""
import json
import sys
from pathlib import Path
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
registry_path = ROOT / "article-index.json"
errors = []
try:
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
except Exception as exc:
    print(f"ERROR: cannot parse article-index.json: {exc}")
    sys.exit(1)

categories = {item["id"] for item in registry.get("categories", [])}
articles = registry.get("articles", [])
by_slug = {}
for item in articles:
    slug = item.get("slug", "")
    if not slug:
        errors.append("article entry is missing slug")
        continue
    if slug in by_slug:
        errors.append(f"duplicate slug: {slug}")
    by_slug[slug] = item
    if item.get("category") not in categories:
        errors.append(f"{slug}: unknown category {item.get('category')!r}")
    if not (ROOT / slug).is_file():
        errors.append(f"{slug}: article file does not exist")
    if item.get("status") == "published":
        for field in ("title", "summary"):
            if not item.get(field):
                errors.append(f"{slug}: published article missing {field}")

for item in articles:
    slug = item.get("slug", "")
    for related in item.get("related", []):
        if related not in by_slug:
            errors.append(f"{slug}: related article not in registry: {related}")
        elif not (ROOT / related).is_file():
            errors.append(f"{slug}: related article file missing: {related}")

try:
    sitemap_text = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    for item in articles:
        if item.get("status") == "published":
            url = "https://webfoundrylab.github.io/invest-atlas/" + item["slug"]
            if url not in sitemap_text:
                errors.append(f"{item['slug']}: published article missing from sitemap.xml")
except Exception as exc:
    errors.append(f"cannot read sitemap.xml: {exc}")

if errors:
    print("Content validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"Content validation passed: {len(articles)} registered articles, {sum(a.get('status') == 'published' for a in articles)} published.")
