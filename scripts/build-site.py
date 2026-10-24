#!/usr/bin/env python3
"""Build generated Invest Atlas metadata from article-index.json."""
import json
import sys
from pathlib import Path
from xml.etree.ElementTree import Element, SubElement, register_namespace, tostring

ROOT = Path(__file__).resolve().parents[1]
BASE_URL = "https://webfoundrylab.github.io/invest-atlas/"
REGISTRY_PATH = ROOT / "article-index.json"
SITEMAP_PATH = ROOT / "sitemap.xml"
RELATED_PATH = ROOT / "related-articles.json"
NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
register_namespace("", NS)


def main():
    try:
        registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"ERROR: cannot parse article-index.json: {exc}", file=sys.stderr)
        return 1

    articles = registry.get("articles", [])
    by_slug = {}
    for article in articles:
        slug = article.get("slug", "")
        if not slug or "/" in slug or "\\" in slug or slug in {".", ".."}:
            print(f"ERROR: unsafe or missing article slug: {slug!r}", file=sys.stderr)
            return 1
        if slug in by_slug:
            print(f"ERROR: duplicate article slug: {slug}", file=sys.stderr)
            return 1
        by_slug[slug] = article

    published = [a for a in articles if a.get("status") == "published"]
    urls = [BASE_URL] + [BASE_URL + a["slug"] for a in published]
    urlset = Element(f"{{{NS}}}urlset")
    for url in urls:
        node = SubElement(urlset, f"{{{NS}}}url")
        SubElement(node, f"{{{NS}}}loc").text = url
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n' + tostring(urlset, encoding="unicode") + "\n"
    SITEMAP_PATH.write_text(xml, encoding="utf-8")

    related_data = {}
    for article in published:
        related = []
        for slug in article.get("related", []):
            target = by_slug.get(slug)
            if target and target.get("status") == "published":
                related.append({
                    "slug": target["slug"],
                    "title": target["title"],
                    "category": target["category"],
                    "summary": target.get("summary", "")
                })
        related_data[article["slug"]] = related
    RELATED_PATH.write_text(
        json.dumps({"generatedFrom": "article-index.json", "articles": related_data},
                   ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8"
    )
    print(f"Generated sitemap.xml ({len(urls)} URLs) and related-articles.json ({len(published)} articles).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
