#!/usr/bin/env python3
"""Generate sitemap, related-article candidate data, and category navigation."""
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
TEXT_SITEMAP_PATH = ROOT / "sitemap.txt"
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



def render_site_header(current_page=None):
    """Return the shared site header used on article and category pages."""
    compass_current = ' aria-current="page"' if current_page == "compass" else ''
    return ('<header class="ia-site-header"><div class="ia-header-inner">'
            '<a class="ia-brand" href="' + BASE_URL + '"><img src="' + BASE_URL + 'favicon.svg" alt="" width="42" height="42"><span>Invest Atlas</span></a>'
            '<nav class="ia-header-nav" aria-label="主要メニュー"><a href="' + BASE_URL + 'categories/"' + (' aria-current="page"' if current_page == "categories" else '') + '>カテゴリ</a><a href="' + BASE_URL + '#welcome">初めての方へ</a><a href="' + BASE_URL + 'investment-compass.html"' + compass_current + '>投資の羅針盤</a></nav>'
            '</div></header>')


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




def generate_category_index_page(registry, published):
    """Generate the category landing page at /categories/."""
    categories = registry.get("categories", [])
    descriptions = {
        "basics": "投資の仕組み、リスク、分散など、判断の土台になる知識",
        "nisa": "NISA・iDeCoなどの制度や、投資に関係する税金",
        "funds": "投資信託・ETFの仕組み、選び方、費用、商品比較",
        "strategy": "積立・長期運用・複利など、資産形成の考え方",
        "markets": "株式市場、経済・金融、AI・半導体などの注目テーマ",
        "companies": "企業の決算・財務、銘柄分析、配当・株主還元"
    }
    cards = []
    for category in categories:
        category_id = category["id"]
        count = sum(1 for article in published if article_category_path(article)[:1] == (category_id,))
        child_links = []
        for child in category.get("children", []):
            child_ids = (category_id, child["id"])
            child_count = sum(1 for article in published if article_category_path(article)[:2] == child_ids)
            if child_count:
                child_links.append(
                    '<li><a href="' + html.escape(category_url(child_ids), quote=True) + '">' +
                    html.escape(child["label"]) + '</a><span>' + str(child_count) + '件</span></li>'
                )
        child_html = ('<ul class="category-index-children">' + ''.join(child_links) + '</ul>') if child_links else ''
        cards.append(
            '<article class="category-index-card"><div class="category-index-card-head">'
            '<h2><a href="' + html.escape(category_url((category_id,)), quote=True) + '">' +
            html.escape(category["label"]) + '</a></h2><span class="category-index-count">' + str(count) + '記事</span></div>'
            '<p>' + html.escape(descriptions.get(category_id, "この分野の投資解説記事をまとめています。")) + '</p>' +
            child_html + '<a class="category-index-more" href="' + html.escape(category_url((category_id,)), quote=True) +
            '">このカテゴリの記事を見る →</a></article>'
        )
    page = '''<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" type="image/svg+xml" href="''' + BASE_URL + '''favicon.svg">
<script src="''' + BASE_URL + '''assets/display-mode.js"></script>
<title>カテゴリから探す｜Invest Atlas</title>
<meta name="description" content="投資の基礎、投資制度・税制、投資信託・ETF、市場、企業分析など、Invest Atlasの記事をカテゴリから探せます。">
<meta name="robots" content="index,follow">
<link rel="canonical" href="''' + html.escape(category_url(()), quote=True) + '''">
<link rel="stylesheet" href="''' + BASE_URL + '''assets/site-layout.css">
<link rel="stylesheet" href="''' + BASE_URL + '''assets/site-header.css">
<style>
body{margin:0;background:#f5f7f8;color:#172b3d;font:16px/1.7 system-ui,-apple-system,"Segoe UI",sans-serif}
a{color:#176d65;text-underline-offset:3px}a:hover{color:#0b4843}
.category-index-wrap{width:min(1160px,calc(100% - 32px));margin:28px auto 56px}
.category-index-panel{background:#fff;border:1px solid #dce4e8;border-radius:16px;padding:clamp(22px,4vw,42px)}
.category-index-eyebrow{font-size:.8rem;font-weight:800;letter-spacing:.08em;color:#087f75}
.category-index-panel h1{font-size:clamp(1.8rem,4vw,2.6rem);line-height:1.25;margin:.35em 0}
.category-index-lead{margin:0;color:#536879;max-width:48em}
.category-index-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px;margin-top:28px}
.category-index-card{min-width:0;border:1px solid #dce4e8;border-radius:14px;padding:18px;background:#fff;display:flex;flex-direction:column}
.category-index-card-head{display:flex;align-items:center;justify-content:space-between;gap:10px}
.category-index-card h2{font-size:1.2rem;line-height:1.4;margin:0}
.category-index-card h2 a{color:#173b4b;text-decoration:none}
.category-index-count{flex:0 0 auto;border-radius:999px;background:#e8f5f5;color:#075f59;padding:3px 10px;font-size:.78rem;font-weight:800}
.category-index-card>p{margin:10px 0;color:#536879;font-size:.92rem}
.category-index-children{list-style:none;padding:10px 0 0;margin:0 0 14px;border-top:1px solid #edf1f3;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:7px 12px}
.category-index-children li{display:flex;justify-content:space-between;align-items:baseline;gap:8px;font-size:.84rem}
.category-index-children li span{color:#71818d;font-size:.75rem;white-space:nowrap}
.category-index-more{margin-top:auto;padding-top:10px;font-size:.88rem;font-weight:800;text-decoration:none}
.category-index-back{display:inline-block;margin-bottom:14px;font-size:.88rem;font-weight:700}
.category-index-footer-inner{width:min(1160px,calc(100% - 32px));margin:0 auto}
footer{margin-top:40px;background:#0c1c2b;color:#d7e1e8;padding:22px 0}
@media(max-width:700px){.category-index-wrap{margin:16px auto 40px}.category-index-grid{grid-template-columns:1fr;gap:12px}.category-index-card{padding:16px}.category-index-children{grid-template-columns:1fr}}
</style>
</head>
<body>''' + render_site_header("categories") + '''
<main class="category-index-wrap">
<a class="category-index-back" href="''' + BASE_URL + '''">← トップページ</a>
<section class="category-index-panel" aria-labelledby="category-index-title">
<div class="category-index-eyebrow">EXPLORE BY CATEGORY</div>
<h1 id="category-index-title">カテゴリから探す</h1>
<p class="category-index-lead">Invest Atlasの記事を6つの分野に整理しています。気になるカテゴリや下位カテゴリから、知りたいテーマを探せます。</p>
<div class="category-index-grid">''' + ''.join(cards) + '''</div>
</section>
</main>
<footer><div class="category-index-footer-inner">Invest Atlas｜投資を理解するための解説・比較ガイド</div></footer>
</body>
</html>
'''
    page_dir = ROOT / "categories"
    page_dir.mkdir(parents=True, exist_ok=True)
    (page_dir / "index.html").write_text(page, encoding="utf-8")
    return category_url(())


def generate_category_pages(registry, published):
    categories = registry.get("categories", [])
    nodes = taxonomy_nodes(categories)
    populated_urls = []
    tree_css = """<style>
body{margin:0;background:#f5f7f8;color:#172b3d;font:16px/1.7 system-ui,-apple-system,'Segoe UI',sans-serif}a{color:#176d65;text-underline-offset:3px}a:hover{color:#0b4843}.wrap{width:min(1160px,calc(100% - 32px));margin:auto}header{background:#10243a;padding:17px 0}header a{color:#fff;text-decoration:none;font-weight:800}.crumbs{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 14px;font-size:.9rem}.layout{display:grid;grid-template-columns:245px minmax(0,1fr);gap:26px;align-items:start}.category-tree{background:#fff;border:1px solid #dce4e8;border-radius:14px;padding:14px;position:sticky;top:18px;max-height:calc(100vh - 36px);overflow:auto}.category-tree ul{list-style:none;padding-left:14px;margin:8px 0}.category-tree>ul{padding:0}.category-tree li{margin:5px 0}.category-tree summary{cursor:pointer}.category-tree a{font-size:.9rem}.category-tree .active>a,.category-tree .active>details>summary>a{font-weight:800;color:#075f59}.content{background:white;border:1px solid #dce4e8;border-radius:14px;padding:clamp(22px,4vw,42px);min-width:0}.content h1{font-size:clamp(1.8rem,4vw,2.7rem);line-height:1.25;margin:.35em 0}.lead{color:#536879}h2{font-size:1.25rem;margin:2rem 0 .7rem}.children{list-style:none;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}.children li{border:1px solid #dce4e8;border-radius:12px;padding:12px;display:flex;flex-direction:column}.children span{font-size:.8rem;color:#536879}.articles{display:grid;gap:12px}.article-card{border:1px solid #dce4e8;border-radius:13px;padding:15px}.article-card[hidden]{display:none}.article-card strong{font-size:1.05rem}.article-card-title-main,.article-card-title-subtitle{display:block}.article-card-title-subtitle{font-size:.82em;font-weight:600;color:#536879;line-height:1.45;margin-top:.18em}.article-card p{color:#536879;margin:5px 0 8px}.empty{padding:16px;background:#f5f7f8;border-radius:12px}.category-results-toolbar{display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;margin:12px 0;padding:10px 12px;background:#e8f5f5;border:1px solid #d2e8e8;border-radius:10px}.category-results-count{margin:0;color:#123653;font-size:.88rem;font-weight:800}.category-page-size{display:flex;align-items:center;gap:7px;color:#31505f;font-size:.82rem;font-weight:750}.category-page-size select{border:1px solid #b8d8d9;background:#fff;color:#172b3d;border-radius:8px;padding:6px 8px;font:inherit}.category-pagination{display:flex;justify-content:center;align-items:center;flex-wrap:wrap;gap:6px;margin:12px 0}.category-pagination[hidden]{display:none}.category-page-button{min-width:36px;min-height:36px;padding:6px 10px;border:1px solid #b8d8d9;border-radius:8px;background:#fff;color:#075e58;font:inherit;font-size:.85rem;font-weight:750;cursor:pointer}.category-page-button[aria-current="page"]{background:#087f75;border-color:#087f75;color:#fff}.category-page-button:disabled{opacity:.4;cursor:not-allowed}.category-page-status{padding:0 5px;color:#536879;font-size:.82rem;white-space:nowrap}.mobile-tree{display:none}footer{margin-top:40px;background:#0c1c2b;color:#d7e1e8;padding:22px 0}@media(max-width:850px){.layout{grid-template-columns:1fr}.layout>.category-tree{display:none}.mobile-tree{display:block;margin:0 0 18px}.mobile-tree .category-tree{display:block;position:static;max-height:none}.children{grid-template-columns:1fr}.category-results-toolbar{align-items:flex-start}.category-page-size{font-size:.78rem}.category-page-button{min-width:34px;min-height:34px;padding:5px 8px}}
</style>"""
    for node in nodes:
        ids = node["ids"]
        matches = sorted([a for a in published if article_category_path(a)[:len(ids)] == ids], key=lambda a: (-(int(a.get("publishOrder", 0) or 0)), a.get("title", "")))
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
        cards = ''.join(
            '<article class="article-card"><strong><a href="' + html.escape(BASE_URL + a["slug"], quote=True) + '">'
            '<span class="article-card-title-main">' + html.escape(a.get("mainTitle", a["title"])) + '</span>'
            + ('<span class="article-card-title-subtitle">' + html.escape(a["subtitle"]) + '</span>' if a.get("subtitle") else '')
            + '</a></strong><p>' + html.escape(a.get("summary", "")) + '</p></article>'
            for a in matches
        )
        if not cards:
            cards = '<p class="empty">このカテゴリの記事は準備中です。上位・下位カテゴリや他のテーマもご覧ください。</p>'
        canonical = category_url(ids)
        title = html.escape(node["item"]["label"] + "の記事一覧｜Invest Atlas")
        tree = render_category_tree(categories, ids)
        page = '<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><link rel="icon" type="image/svg+xml" href="' + BASE_URL + 'favicon.svg"><script src="' + BASE_URL + 'assets/display-mode.js"></script><title>' + title + '</title><meta name="description" content="' + html.escape(node["item"]["label"] + "に関する投資解説記事をまとめています。", quote=True) + '"><meta name="robots" content="' + ('index,follow' if is_populated else 'noindex,follow') + '"><link rel="canonical" href="' + html.escape(canonical, quote=True) + '">' + tree_css + '<link rel="stylesheet" href="' + BASE_URL + 'assets/site-layout.css"><link rel="stylesheet" href="' + BASE_URL + 'assets/site-header.css"></head><body>' + render_site_header() + '<main class="wrap"><div class="layout">' + tree + '<div class="content"><nav class="crumbs" aria-label="パンくずリスト">' + ' › '.join(crumbs) + '</nav><div class="mobile-tree"><details><summary>カテゴリツリーを開く</summary>' + tree + '</details></div><div style="font-size:.8rem;font-weight:800;color:#087f75">CATEGORY GUIDE</div><h1>' + html.escape(node["item"]["label"]) + '</h1><p class="lead">カテゴリから記事を探せます。公開記事の内容に応じて分類しています。</p>' + ('<section><h2>下位カテゴリ</h2><ul class="children">' + ''.join(child_html) + '</ul></section>' if child_html else '') + ('<section><h2>記事一覧</h2><div class="category-results-toolbar"><p class="category-results-count" id="category-result-count" aria-live="polite">記事一覧</p><label class="category-page-size" for="category-page-size">表示件数<select id="category-page-size"><option value="10" selected>10件</option><option value="20">20件</option><option value="50">50件</option><option value="100">100件</option></select></label></div><nav class="category-pagination" id="category-pagination-top" aria-label="記事一覧の上部ページ切り替え" hidden></nav><div class="articles" id="category-articles">' + cards + '</div><nav class="category-pagination" id="category-pagination-bottom" aria-label="記事一覧の下部ページ切り替え" hidden></nav><script src="' + BASE_URL + 'assets/category-pagination.js" defer></script></section>' if matches else '') + '</div></div></main><footer><div class="wrap">Invest Atlas｜投資を理解するための解説・比較ガイド</div></footer></body></html>'
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


def clean_page_layout_styles(page):
    """Remove per-article width and card spacing; these belong to site-layout.css."""
    def strip_layout_rules(match):
        css = match.group(2)
        css = re.sub(r"\.wrap\s*\{[^{}]*\}", "", css)
        css = re.sub(r"\.article\s*\{[^{}]*\}", "", css)
        return match.group(1) + css + match.group(3)
    return re.sub(r"(<style\b[^>]*>)([\s\S]*?)(</style>)", strip_layout_rules, page, flags=re.I)


def clean_article_layout(page):
    page = clean_category_block(page)
    page = clean_page_layout_styles(page)
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
main.wrap{width:min(1160px,calc(100% - 32px))}header .wrap{width:min(1160px,calc(100% - 32px))}
.article-page-layout{display:grid;grid-template-columns:245px minmax(0,1fr);gap:26px;align-items:start;margin:22px 0 52px}
.article-sidebar .category-tree{background:#fff;border:1px solid #dce4e8;border-radius:14px;padding:14px;position:sticky;top:18px;max-height:calc(100vh - 36px);overflow:auto}
.article-sidebar .category-tree ul{list-style:none;padding-left:14px;margin:8px 0}.article-sidebar .category-tree>ul{padding:0}.article-sidebar .category-tree li{margin:5px 0}.article-sidebar .category-tree summary{cursor:pointer}.article-sidebar .category-tree a{font-size:.9rem}.article-sidebar .category-tree .active>a,.article-sidebar .category-tree .active>details>summary>a{font-weight:800;color:#075f59}
.article-page-content{min-width:0}
.article-category-crumbs{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 14px;font-size:.9rem}.article-mobile-tree{display:none}
@media(max-width:850px){.article-page-layout{grid-template-columns:1fr;gap:0;margin-top:14px}.article-sidebar{display:none}.article-mobile-tree{display:block;margin:0 0 16px;padding:12px 14px;background:#fff;border:1px solid #d5e6eb;border-radius:12px}.article-mobile-tree summary{cursor:pointer;font-weight:750}.article-mobile-tree .category-tree{margin-top:10px;max-height:320px;overflow:auto}.article-mobile-tree .category-tree ul{list-style:none;padding-left:14px;margin:8px 0}.article-mobile-tree .category-tree>ul{padding:0}}
</style>"""
    opening = (ARTICLE_OPEN_START + '<div class="article-page-layout"><aside class="article-sidebar">' + tree + '</aside><div class="article-page-content">' +
        ARTICLE_OPEN_END)
    closing = ARTICLE_CLOSE_START + '</div></div>' + ARTICLE_CLOSE_END
    page, header_count = re.subn(r'<header\b[^>]*>.*?</header>', lambda _m: render_site_header(), page, count=1, flags=re.I | re.S)
    main_match = re.search(r'<main\b[^>]*>', page, flags=re.I)
    main_close = page.lower().rfind("</main>")
    if not main_match or main_close < 0:
        return page
    style_block = ARTICLE_STYLE_START + css + ARTICLE_STYLE_END
    head_close = page.lower().find("</head>")
    if head_close >= 0:
        page = page[:head_close] + style_block + '<link rel="stylesheet" href="' + BASE_URL + 'assets/site-layout.css"><link rel="stylesheet" href="' + BASE_URL + 'assets/site-header.css"><script src="' + BASE_URL + 'assets/display-mode.js"></script>' + page[head_close:]
    main_match = re.search(r'<main\b[^>]*>', page, flags=re.I)
    if not main_match:
        return page
    page = page[:main_match.end()] + opening + page[main_match.end():]
    # Place breadcrumbs and mobile navigation inside the same white card as category pages.
    article_match = re.search(r'<article\b[^>]*class="[^"]*\barticle\b[^"]*"[^>]*>', page, flags=re.I)
    if article_match:
        crumb_html = '<nav class="article-category-crumbs" aria-label="パンくずリスト">' + ' › '.join(crumbs) + '</nav>'
        mobile_tree = '<div class="article-mobile-tree"><details><summary>カテゴリツリーを開く</summary>' + tree + '</details></div>'
        page = page[:article_match.end()] + crumb_html + mobile_tree + page[article_match.end():]
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
    category_index_url = generate_category_index_page(registry, published)
    category_urls = [category_index_url] + generate_category_pages(registry, published)
    static_pages = [page for page in registry.get("pages", []) if page.get("status", "published") == "published"]
    urls = [BASE_URL] + [BASE_URL + a["slug"] for a in published] + category_urls + [BASE_URL + page["slug"] for page in static_pages]
    urlset = Element(f"{{{NS}}}urlset")
    for url in urls:
        node = SubElement(urlset, f"{{{NS}}}url")
        SubElement(node, f"{{{NS}}}loc").text = url
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n' + tostring(urlset, encoding="unicode") + "\n"
    SITEMAP_PATH.write_text(xml, encoding="utf-8")
    TEXT_SITEMAP_PATH.write_text("\n".join(urls) + "\n", encoding="utf-8")

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
        # Related links are placed contextually in article HTML by editorial review.
        # Keep the candidate data in related-articles.json without appending a footer list.
        page_path.write_text(page, encoding="utf-8")

    RELATED_PATH.write_text(
        json.dumps({"generatedFrom": "article-index.json", "articles": related_data},
                   ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8"
    )
    print(f"Generated sitemap.xml and sitemap.txt ({len(urls)} URLs each), plus related-articles.json ({len(published)} articles).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
