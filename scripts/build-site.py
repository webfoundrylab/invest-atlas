#!/usr/bin/env python3
"""Generate sitemap, related-article data, and article-page related sections."""
import html
import json
import re
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



CATEGORY_START = "<!-- GENERATED CATEGORY NAV: START -->"
CATEGORY_END = "<!-- GENERATED CATEGORY NAV: END -->"


def taxonomy_nodes(categories):
    result = []
    def walk(items, ids=(), labels=()):
        for item in items:
            path = ids + (item["id"],)
            names = labels + (item["label"],)
            result.append({"item": item, "ids": path, "labels": names})
            walk(item.get("children", []), path, names)
    walk(categories)
    return result


def category_url(ids):
    return BASE_URL + "categories/" + "/".join(ids) + "/"


def article_category_path(article):
    return tuple(article.get(k) for k in ("category", "subcategory", "topic") if article.get(k))


def render_category_tree(categories, active=()):
    out = ['<nav class="category-tree" aria-label="カテゴリツリー"><strong>カテゴリから探す</strong><ul>']
    def walk(items, prefix=()):
        for item in items:
            ids = prefix + (item["id"],)
            url = category_url(ids)
            out.append('<li' + (' class="active"' if ids == active else '') + '>')
            children = item.get("children", [])
            if children:
                out.append('<details' + (' open' if active[:len(ids)] == ids else '') + '><summary><a href="' + html.escape(url, quote=True) + '">' + html.escape(item["label"]) + '</a></summary><ul>')
                walk(children, ids)
                out.append('</ul></details>')
            else:
                out.append('<a href="' + html.escape(url, quote=True) + '">' + html.escape(item["label"]) + '</a>')
            out.append('</li>')
    walk(categories)
    out.append('</ul></nav>')
    return ''.join(out)


def generate_category_pages(registry, published):
    categories = registry.get("categories", [])
    nodes = taxonomy_nodes(categories)
    populated_urls = []
    tree_css = """<style>
body{margin:0;background:#f1f8fa;color:#172b3d;font:16px/1.7 system-ui,-apple-system,'Segoe UI',sans-serif}a{color:#12665f;text-underline-offset:3px}.wrap{width:min(1160px,calc(100% - 32px));margin:auto}header{background:#10243a;padding:17px 0}header a{color:#fff;text-decoration:none;font-weight:800}.crumbs{display:flex;flex-wrap:wrap;gap:8px;margin:22px 0;font-size:.9rem}.layout{display:grid;grid-template-columns:245px minmax(0,1fr);gap:26px;align-items:start}.category-tree{background:#fff;border:1px solid #d5e6eb;border-radius:14px;padding:14px;position:sticky;top:18px;max-height:calc(100vh - 36px);overflow:auto}.category-tree ul{list-style:none;padding-left:14px;margin:8px 0}.category-tree>ul{padding:0}.category-tree li{margin:5px 0}.category-tree summary{cursor:pointer}.category-tree a{font-size:.9rem}.category-tree .active>a,.category-tree .active>details>summary>a{font-weight:800;color:#075f59}.content{background:white;border:1px solid #d5e6eb;border-radius:18px;padding:clamp(20px,4vw,40px);min-width:0}.content h1{font-size:clamp(1.8rem,4vw,2.7rem);line-height:1.25;margin:.35em 0}.lead{color:#536879}h2{font-size:1.25rem;margin:2rem 0 .7rem}.children{list-style:none;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}.children li{border:1px solid #d5e6eb;border-radius:12px;padding:12px;display:flex;flex-direction:column}.children span{font-size:.8rem;color:#536879}.articles{display:grid;gap:12px}.article-card{border:1px solid #d5e6eb;border-radius:13px;padding:15px}.article-card strong{font-size:1.05rem}.article-card p{color:#536879;margin:5px 0 8px}.empty{padding:16px;background:#f4f8f9;border-radius:12px}.mobile-tree{display:none}footer{margin-top:40px;background:#0c1c2b;color:#d7e1e8;padding:22px 0}@media(max-width:850px){.layout{grid-template-columns:1fr}.layout>.category-tree{display:none}.mobile-tree{display:block;margin:0 0 18px}.mobile-tree .category-tree{display:block;position:static;max-height:none}.children{grid-template-columns:1fr}}
</style>"""
    for node in nodes:
        ids = node["ids"]
        matches = [a for a in published if article_category_path(a)[:len(ids)] == ids]
        is_populated = bool(matches)
        page_dir = ROOT / "categories"
        for part in ids:
            page_dir = page_dir / part
        page_dir.mkdir(parents=True, exist_ok=True)
        crumbs = ['<a href="' + BASE_URL + '">トップ</a>']
        for depth, label in enumerate(node["labels"], 1):
            crumbs.append('<a href="' + html.escape(category_url(ids[:depth]), quote=True) + '">' + html.escape(label) + '</a>')
        child_html = []
        for child in node["item"].get("children", []):
            child_ids = ids + (child["id"],)
            count = sum(1 for a in published if article_category_path(a)[:len(child_ids)] == child_ids)
            child_html.append('<li><a href="' + html.escape(category_url(child_ids), quote=True) + '">' + html.escape(child["label"]) + '</a><span>' + (str(count) + '件の記事' if count else '記事準備中') + '</span></li>')
        cards = ''.join('<article class="article-card"><strong><a href="' + html.escape(BASE_URL + a["slug"], quote=True) + '">' + html.escape(a["title"]) + '</a></strong><p>' + html.escape(a.get("summary", "")) + '</p></article>' for a in matches)
        if not cards:
            cards = '<p class="empty">このカテゴリの記事は準備中です。上位・下位カテゴリや他のテーマもご覧ください。</p>'
        canonical = category_url(ids)
        title = html.escape(node["item"]["label"] + "の記事一覧｜Invest Atlas")
        tree = render_category_tree(categories, ids)
        page = '<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>' + title + '</title><meta name="description" content="' + html.escape(node["item"]["label"] + "に関する投資解説記事をまとめています。", quote=True) + '"><meta name="robots" content="' + ('index,follow' if is_populated else 'noindex,follow') + '"><link rel="canonical" href="' + html.escape(canonical, quote=True) + '">' + tree_css + '</head><body><header><div class="wrap"><a href="' + BASE_URL + '">← INVEST ATLAS</a></div></header><main class="wrap"><nav class="crumbs" aria-label="パンくずリスト">' + ' › '.join(crumbs) + '</nav><div class="mobile-tree"><details><summary>カテゴリツリーを開く</summary>' + tree + '</details></div><div class="layout">' + tree + '<div class="content"><div style="font-size:.8rem;font-weight:800;color:#087f75">CATEGORY GUIDE</div><h1>' + html.escape(node["item"]["label"]) + '</h1><p class="lead">カテゴリから記事を探せます。公開記事の内容に応じて分類しています。</p>' + ('<section><h2>下位カテゴリ</h2><ul class="children">' + ''.join(child_html) + '</ul></section>' if child_html else '') + '<section><h2>記事一覧（' + str(len(matches)) + '件）</h2><div class="articles">' + cards + '</div></section></div></div></main><footer><div class="wrap">Invest Atlas｜投資を理解するための解説・比較ガイド</div></footer></body></html>'
        (page_dir / "index.html").write_text(page, encoding="utf-8")
        if is_populated:
            populated_urls.append(canonical)
    return populated_urls


def clean_category_block(content):
    start = content.find(CATEGORY_START)
    end = content.find(CATEGORY_END)
    if start >= 0 and end >= start:
        return content[:start] + content[end + len(CATEGORY_END):]
    return content


ARTICLE_OPEN_START = "<!-- GENERATED ARTICLE LAYOUT OPEN: START -->"
ARTICLE_OPEN_END = "<!-- GENERATED ARTICLE LAYOUT OPEN: END -->"
ARTICLE_CLOSE_START = "<!-- GENERATED ARTICLE LAYOUT CLOSE: START -->"
ARTICLE_CLOSE_END = "<!-- GENERATED ARTICLE LAYOUT CLOSE: END -->"


ARTICLE_STYLE_START = "<!-- GENERATED ARTICLE LAYOUT STYLE: START -->"
ARTICLE_STYLE_END = "<!-- GENERATED ARTICLE LAYOUT STYLE: END -->"


def clean_article_layout(page):
    page = clean_category_block(page)
    page = re.sub(re.escape(ARTICLE_OPEN_START) + r".*?" + re.escape(ARTICLE_OPEN_END), "", page, flags=re.S)
    page = re.sub(re.escape(ARTICLE_CLOSE_START) + r".*?" + re.escape(ARTICLE_CLOSE_END), "", page, flags=re.S)
    page = re.sub(re.escape(ARTICLE_STYLE_START) + r".*?" + re.escape(ARTICLE_STYLE_END), "", page, flags=re.S)
    return page


def inject_article_category_nav(page, article, registry):
    page = clean_article_layout(page)
    cats = registry.get("categories", [])
    cat = next((x for x in cats if x["id"] == article.get("category")), None)
    if not cat:
        return page
    ids = [cat["id"]]
    labels = [cat["label"]]
    current = cat
    for key in ("subcategory", "topic"):
        val = article.get(key)
        if not val:
            break
        current = next((x for x in current.get("children", []) if x["id"] == val), None)
        if not current:
            break
        ids.append(current["id"])
        labels.append(current["label"])
    crumbs = ['<a href="' + BASE_URL + '">トップ</a>']
    crumbs += ['<a href="' + html.escape(category_url(tuple(ids[:i])), quote=True) + '">' + html.escape(label) + '</a>' for i, label in enumerate(labels, 1)]
    tree = render_category_tree(cats, tuple(ids))
    css = """<style>
main.wrap{width:min(1160px,calc(100% - 32px))}
.article-page-layout{display:grid;grid-template-columns:245px minmax(0,1fr);gap:26px;align-items:start;margin:22px 0 52px}
.article-sidebar .category-tree{background:#fff;border:1px solid #d5e6eb;border-radius:14px;padding:14px;position:sticky;top:18px;max-height:calc(100vh - 36px);overflow:auto}
.article-sidebar .category-tree ul{list-style:none;padding-left:14px;margin:8px 0}.article-sidebar .category-tree>ul{padding:0}.article-sidebar .category-tree li{margin:5px 0}.article-sidebar .category-tree summary{cursor:pointer}.article-sidebar .category-tree a{font-size:.9rem}.article-sidebar .category-tree .active>a,.article-sidebar .category-tree .active>details>summary>a{font-weight:800;color:#075f59}
.article-page-content{min-width:0}.article-page-content .article{max-width:none;width:100%;margin:0;padding:clamp(20px,3.5vw,42px)}
.article-category-crumbs{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 14px;font-size:.9rem}.article-mobile-tree{display:none}
@media(max-width:850px){.article-page-layout{grid-template-columns:1fr;gap:0;margin-top:14px}.article-sidebar{display:none}.article-mobile-tree{display:block;margin:0 0 16px;padding:12px 14px;background:#fff;border:1px solid #d5e6eb;border-radius:12px}.article-mobile-tree summary{cursor:pointer;font-weight:750}.article-mobile-tree .category-tree{margin-top:10px;max-height:320px;overflow:auto}.article-mobile-tree .category-tree ul{list-style:none;padding-left:14px;margin:8px 0}.article-mobile-tree .category-tree>ul{padding:0}.article-page-content .article{padding:clamp(18px,5vw,28px)}}
</style>"""
    opening = (ARTICLE_OPEN_START + '<div class="article-page-layout"><aside class="article-sidebar">' + tree + '</aside><div class="article-page-content">' +
        '<div class="article-mobile-tree"><details><summary>カテゴリツリーを開く</summary>' + tree + '</details></div>' +
        '<nav class="article-category-crumbs" aria-label="パンくずリスト">' + ' › '.join(crumbs) + '</nav>' +
        ARTICLE_OPEN_END)
    closing = ARTICLE_CLOSE_START + '</div></div>' + ARTICLE_CLOSE_END
    main_match = re.search(r'<main\b[^>]*>', page, flags=re.I)
    main_close = page.lower().rfind("</main>")
    if not main_match or main_close < 0:
        return page
    style_block = ARTICLE_STYLE_START + css + ARTICLE_STYLE_END
    head_close = page.lower().find("</head>")
    if head_close >= 0:
        page = page[:head_close] + style_block + page[head_close:]
    main_match = re.search(r'<main\\b[^>]*>', page, flags=re.I)
    if not main_match:
        return page
    page = page[:main_match.end()] + opening + page[main_match.end():]
    main_close = page.lower().rfind("</main>")
    page = page[:main_close] + closing + page[main_close:]
    return page


def render_home_category_tree(categories):
    def walk(items, prefix=()):
        out = ['<ul>']
        for item in items:
            path = prefix + (item["id"],)
            href = "categories/" + "/".join(path) + "/"
            children = item.get("children", [])
            out.append("<li>")
            link = '<a href="' + html.escape(href, quote=True) + '">' + html.escape(item["label"]) + "</a>"
            if children:
                out.append("<details><summary>" + link + "</summary>" + walk(children, path) + "</details>")
            else:
                out.append(link)
            out.append("</li>")
        out.append("</ul>")
        return "".join(out)
    return walk(categories)


def inject_home_category_tree(registry):
    path = ROOT / "index.html"
    if not path.is_file():
        return
    page = path.read_text(encoding="utf-8")
    tree = render_home_category_tree(registry.get("categories", []))
    pattern = r'(<div id="category-tree-home" class="category-tree-home"[^>]*>).*?(</div>)'
    updated, count = re.subn(pattern, lambda m: m.group(1) + tree + m.group(2), page, count=1, flags=re.S)
    if count:
        path.write_text(updated, encoding="utf-8")


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
    inject_home_category_tree(registry)
    category_urls = generate_category_pages(registry, published)
    urls = [BASE_URL] + [BASE_URL + a["slug"] for a in published] + category_urls
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
        page = inject_article_category_nav(page, article, registry)
        existing_hrefs = set(re.findall(r"""href=["']([^"']+)["']""", page, flags=re.IGNORECASE))
        entries = [entry for entry in related_data[article["slug"]] if entry["slug"] not in existing_hrefs]
        entries = entries[:4]
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
