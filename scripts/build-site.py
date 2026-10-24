#!/usr/bin/env python3
"""Generate sitemap, related-article data, and article-page related sections."""
import html
import json
import sys
from pathlib import Path
from xml.etree.ElementTree import Element, SubElement, register_namespace, tostring

ROOT = Path(__file__).resolve().parents[1]
BASE_URL = "https://webfoundrylab.github.io/invest-atlas/"
REGISTRY_PATH = ROOT / "article-index.json"
SITEMAP_PATH = ROOT / "sitemap.xml"
RELATED_PATH = ROOT / "related-articles.json"
START_MARKER = "<!-- GENERATED RELATED ARTICLES: START -->"
END_MARKER = "<!-- GENERATED RELATED ARTICLES: END -->"
NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
register_namespace("", NS)


def clean_existing_block(content):
    start = content.find(START_MARKER)
    end = content.find(END_MARKER)
    if start >= 0 and end >= start:
        return content[:start] + content[end + len(END_MARKER):]
    return content


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
        explicit = [slug for slug in article.get("related", [])
                    if slug in by_slug and by_slug[slug].get("status") == "published" and slug != article["slug"]]
        ranked = []
        own_tags = set(article.get("tags", []))
        for candidate in published:
            slug = candidate["slug"]
            if slug == article["slug"] or slug in explicit:
                continue
            overlap = own_tags.intersection(candidate.get("tags", []))
            if overlap:
                ranked.append((len(overlap), slug, candidate))
        ranked.sort(key=lambda row: (-row[0], row[1]))
        selected = explicit[:4]
        for _, slug, candidate in ranked:
            if len(selected) >= 4:
                break
            selected.append(slug)
        related_data[article["slug"]] = []
        for slug in selected:
            target = by_slug[slug]
            related_data[article["slug"]].append({
                "slug": target["slug"], "title": target["title"],
                "category": target["category"], "summary": target.get("summary", ""),
                "tags": target.get("tags", [])
            })

        page_path = ROOT / article["slug"]
        if not page_path.is_file():
            print(f"ERROR: article file missing: {article['slug']}", file=sys.stderr)
            return 1
        page = clean_existing_block(page_path.read_text(encoding="utf-8"))
        entries = related_data[article["slug"]]
        if entries:
            links = "\n".join(
                '      <li><a href="' + html.escape(item["slug"], quote=True) + '">' +
                html.escape(item["title"]) + '</a><p>' + html.escape(item["summary"]) + '</p></li>'
                for item in entries
            )
            block = (
                START_MARKER + '\n'
                '<section class="generated-related" aria-labelledby="generated-related-title">\n'
                '  <h2 id="generated-related-title">関連記事</h2>\n'
                '  <ul>\n' + links + '\n  </ul>\n'
                '  <style>.generated-related{margin:2.5rem 0;padding:1.25rem;border:1px solid #d5e6eb;border-radius:16px;background:#f7fbfc}.generated-related h2{margin-top:0}.generated-related ul{padding-left:1.25rem}.generated-related li{margin:0 0 1rem}.generated-related li:last-child{margin-bottom:0}.generated-related p{margin:.2rem 0;color:#536879;font-size:.92rem}.generated-related a{font-weight:750}</style>\n'
                '</section>\n' + END_MARKER
            )
            if "</body>" not in page.lower():
                print(f"ERROR: no closing body tag in {article['slug']}", file=sys.stderr)
                return 1
            pos = page.lower().rfind("</body>")
            page = page[:pos] + block + "\n" + page[pos:]
        page_path.write_text(page, encoding="utf-8")

    RELATED_PATH.write_text(
        json.dumps({"generatedFrom": "article-index.json", "articles": related_data},
                   ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8"
    )
    print(f"Generated sitemap.xml ({len(urls)} URLs), related-articles.json ({len(published)} articles), and article-page related sections.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
