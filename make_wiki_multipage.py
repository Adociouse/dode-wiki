# -*- coding: utf-8 -*-
"""
make_wiki_multipage.py — Bygger en flersidig wiki till docs/wiki-html/
  - En HTML-sida per wikisida
  - index.html med alfabetiskt nyckelordsindex
  - Korsreferenser: viktiga termer länkas automatiskt (första förekomsten per sida)

Kör: python make_wiki_multipage.py
"""
import os, re, glob, datetime, zipfile
import markdown as mdlib
from html import escape

# ── Källkatalog ───────────────────────────────────────────
WIKI_MD_DIR = "src"

# ── Spelarwiki-config ─────────────────────────────────────
PLAYER_MD_OVERRIDES = {
    # Ersätt statblock-sidor med folklore-versioner
    "MONSTER_FOLKLORE": os.path.join("src", "MONSTER_FOLKLORE.md"),
    "DRAKAR_FOLKLORE":  os.path.join("src", "DRAKAR_FOLKLORE.md"),
}
PLAYER_PAGE_MAP = {
    "INDEX":              "index.html",
    "REGLER_EGENSKAPER":  "grundegenskaper.html",
    "REGLER_STRID":       "strid.html",
    "REGLER_FARDIGHETER": "fardigheter.html",
    "RASER":              "raser.html",
    "YRKEN":              "yrken.html",
    "MAGI":               "magi.html",
    "UTRUSTNING":         "utrustning.html",
    "HJALTAR":            "hjaltar.html",
    "MONSTER_FOLKLORE":   "monster.html",
    "DRAKAR_FOLKLORE":    "drakar.html",
    "DEMONOLOGI":         "demonologi.html",
}
PLAYER_NAV_ITEMS = [
    ("index.html",          "📖", "Index"),
    ("grundegenskaper.html","💪", "Grundegenskaper"),
    ("strid.html",          "⚔️", "Strid & Vapen"),
    ("fardigheter.html",    "🎯", "Färdigheter"),
    ("raser.html",          "🧝", "Raser"),
    ("yrken.html",          "🛡️", "Yrken"),
    ("magi.html",           "✨", "Magi"),
    ("utrustning.html",     "🗡️", "Utrustning"),
    ("hjaltar.html",        "🌟", "Hjältar"),
    ("monster.html",        "🐉", "Varelser"),
    ("drakar.html",         "🔥", "Drakar"),
    ("demonologi.html",     "🔮", "Demonologi"),
]
PLAYER_INDEX_TITLE = "⚔ Drakar och Demoner Expert — Spelarviki"
PLAYER_INDEX_SUBTITLE = "Regelreferens och världsinformation för spelare. Baserad på originalböckerna."
PLAYER_OUT_DIR = "docs"
PLAYER_ZIP_PREFIX = "DoDE_Wiki"

# ── Nyckelord → (sida, ankar) ─────────────────────────────
# Längre fraser måste komma FÖRE kortare (longest-match)
KEYWORDS = {
    # Grundegenskaper
    "Grundegenskaper":   ("grundegenskaper.html", None),
    "Skadebonus":        ("grundegenskaper.html", "skadebonus"),
    "Förflyttning":      ("grundegenskaper.html", "forflyttning"),
    "Grupp":             ("grundegenskaper.html", "grupp"),
    # Strid
    "Stridssystemet":    ("strid.html", None),
    "Initiativ":         ("strid.html", "initiativ"),
    "Parering":          ("strid.html", "parering"),
    "Fummel":            ("strid.html", "fummel"),
    "Perfekt":           ("strid.html", "perfekt"),
    "Bärsärk":           ("strid.html", "barsark"),
    # Färdigheter
    "Färdighetssystemet":("fardigheter.html", None),
    "Baschans":          ("fardigheter.html", "bc"),
    "Erfarenhetspoäng":  ("fardigheter.html", "ep"),
    # Raser
    "Halvlängdsman":     ("raser.html", "halvlangdsman"),
    "Halvalv":           ("raser.html", "halvalv"),
    "Halvorch":          ("raser.html", "halvorch"),
    "Svartfolk":         ("raser.html", "svartfolk"),
    "Människa":          ("raser.html", "manniska"),
    "Dvärg":             ("raser.html", "dvarg"),
    "Alver":             ("raser.html", "alv"),
    "Alv":               ("raser.html", "alv"),
    "Anka":              ("raser.html", "anka"),
    # Yrken
    "Lönnmördare":       ("yrken.html", "lonnmordare"),
    "Krigare":           ("yrken.html", "krigare"),
    "Magiker":           ("yrken.html", "magiker"),
    "Paladin":           ("yrken.html", "paladin"),
    "Barbar":            ("yrken.html", "barbar"),
    "Bard":              ("yrken.html", "bard"),
    "Tjuv":              ("yrken.html", "tjuv"),
    "Prisjägare":        ("yrken.html", "prisjagare"),
    "Gladiator":         ("yrken.html", "gladiator"),
    "Soldat":            ("yrken.html", "soldat"),
    "Sprätthök":         ("yrken.html", "sprattok"),
    "Vapenmästare":      ("yrken.html", "vapenmastare"),
    "Krigarmunk":        ("yrken.html", "krigarmunk"),
    # Magi — skolor
    "Elementarmagi":     ("magi.html", "elementarmagi"),
    "Häxkonster":        ("magi.html", "haxkonster"),
    "Illusionism":       ("magi.html", "illusionism"),
    "Nekromanti":        ("magi.html", "nekromanti"),
    "Demonologi":        ("demonologi.html", None),
    "Harmonism":         ("magi.html", "harmonism"),
    "Mentalism":         ("magi.html", "mentalism"),
    "Spiritism":         ("magi.html", "spiritism"),
    "Stavmagi":          ("magi.html", "stavmagi"),
    "Symbolism":         ("magi.html", "symbolism"),
    "Röstmagi":          ("magi.html", "rostmagi"),
    "Minibesvärjelser":  ("magi.html", "minibesvarjelser"),
    "Animism":           ("magi.html", "animism"),
    "Alkemi":            ("magi.html", "alkemi"),
    # Hjältar
    "Hjältedåd":         ("hjaltar.html", "hjaltedad"),
    "Hjältenivå":        ("hjaltar.html", "hjaltenivaer"),
    "Hjälte":            ("hjaltar.html", None),
    # Monster/drakar
    "Drakar":            ("drakar.html", None),
    "Drake":             ("drakar.html", None),
    # Nya avsnitt
    "Bärförmåga":        ("grundegenskaper.html", "barformaga"),
    "Belastning":        ("grundegenskaper.html", "barformaga"),
    "Magiska föremål":   ("magi.html", "magiska-foremal"),
    "SIGILL":            ("magi.html", "magiska-foremal"),
    "Första Hjälpen":    ("strid.html", "helande"),
    "Läkekonst":         ("strid.html", "helande"),
    "Mörkersyn":         ("strid.html", "strid-i-morker"),
    "Mörkerseende":      ("strid.html", "strid-i-morker"),
    "Gift":              ("strid.html", "gift"),
    "Motgift":           ("strid.html", "gift"),
}

# ── CSS ────────────────────────────────────────────────────
CSS = """
:root {
  --red:      #6B1A1A;
  --red-dark: #4A0E0E;
  --paper:    #FAF3F0;
  --text:     #2A0808;
  --gold:     #D4956B;
  --border:   #C4907A;
  --link:     #6B1A1A;
}
@media (prefers-color-scheme: dark) {
  :root {
    --red:      #C05050;
    --red-dark: #8B2020;
    --paper:    #1E1010;
    --text:     #F0DDD5;
    --gold:     #D4956B;
    --border:   #6B3A2A;
    --link:     #E07070;
  }
}
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: 'Palatino Linotype', Palatino, Georgia, serif;
  background: var(--paper);
  color: var(--text);
  min-height: 100vh;
}

/* ── TOPPNAV ── */
#topnav {
  background: var(--red-dark);
  padding: 0 16px;
  display: flex;
  align-items: center;
  gap: 0;
  flex-wrap: wrap;
  position: sticky;
  top: 0;
  z-index: 50;
  border-bottom: 2px solid var(--gold);
}
#topnav .site-title {
  color: var(--gold);
  font-size: 0.9rem;
  font-weight: bold;
  padding: 10px 16px 10px 0;
  white-space: nowrap;
  border-right: 1px solid rgba(212,149,107,0.3);
  margin-right: 8px;
}
#topnav a {
  color: #F5E6D3;
  text-decoration: none;
  padding: 10px 10px;
  font-size: 0.8rem;
  white-space: nowrap;
  border-bottom: 2px solid transparent;
  transition: color 0.15s, border-color 0.15s;
}
#topnav a:hover { color: #fff; border-bottom-color: var(--gold); }
#topnav a.active { color: var(--gold); border-bottom-color: var(--gold); }
.nav-section {
  color: rgba(212,149,107,0.55);
  font-size: 0.65rem;
  font-weight: bold;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 10px 6px 10px 10px;
  white-space: nowrap;
  border-left: 1px solid rgba(212,149,107,0.25);
  margin-left: 4px;
}

/* ── MAIN ── */
main {
  max-width: 860px;
  margin: 0 auto;
  padding: 40px 32px 80px;
}

/* ── TYPOGRAFI ── */
h1 { font-size: 2rem; color: var(--red); border-bottom: 3px solid var(--gold); padding-bottom: 10px; margin-bottom: 28px; }
h2 { font-size: 1.4rem; color: var(--red-dark); margin: 32px 0 12px; padding-bottom: 4px; border-bottom: 1px solid var(--border); }
h3 { font-size: 1.1rem; color: var(--red); margin: 22px 0 8px; }
h4 { font-size: 1rem; font-weight: bold; margin: 16px 0 6px; }
p  { line-height: 1.75; margin-bottom: 12px; }
ul, ol { margin: 8px 0 14px 24px; line-height: 1.75; }
li { margin-bottom: 4px; }

/* ── WIKILÄNKAR ── */
a { color: var(--link); }
a:hover { text-decoration: underline; }
a.wikilink { border-bottom: 1px dotted var(--gold); text-decoration: none; color: var(--link); }
a.wikilink:hover { border-bottom-style: solid; }

/* ── TABELLER ── */
.table-wrap { overflow-x: auto; margin: 16px 0; }
table { width: 100%; border-collapse: collapse; font-size: 0.88rem; min-width: 400px; }
th { background: var(--red); color: var(--gold); padding: 8px 10px; text-align: left; white-space: nowrap; }
td { padding: 7px 10px; border-bottom: 1px solid var(--border); }
tr:nth-child(even) td { background: rgba(196,144,122,0.08); }
tr:hover td { background: rgba(196,144,122,0.16); }

/* ── KAMPANJRUTA ── */
.kampanj-ruta { background: rgba(107,26,26,0.07); border: 1px solid rgba(107,26,26,0.35); border-left: 4px solid var(--red); border-radius: 6px; padding: 18px 20px; margin: 24px 0 32px; }
.kampanj-ruta .kr-rubrik { font-size: 0.72rem; font-weight: bold; letter-spacing: 0.1em; text-transform: uppercase; color: var(--red); margin-bottom: 12px; }
.kampanj-ruta p { font-size: 0.92rem; line-height: 1.65; margin: 0 0 10px; }
.kampanj-ruta p:last-child { margin-bottom: 0; }
.kampanj-ruta ul { margin: 8px 0 10px 18px; padding: 0; }
.kampanj-ruta li { font-size: 0.92rem; line-height: 1.6; margin-bottom: 4px; }

/* ── KOD / BLOCKQUOTE ── */
code { background: rgba(107,26,26,0.08); padding: 2px 6px; border-radius: 3px; font-family: monospace; font-size: 0.88em; }
pre  { background: rgba(107,26,26,0.06); border: 1px solid var(--border); border-radius: 6px; padding: 14px 16px; overflow-x: auto; margin: 14px 0; }
pre code { background: none; padding: 0; }
blockquote { border-left: 4px solid var(--gold); padding: 10px 16px; margin: 14px 0; background: rgba(212,149,107,0.08); font-style: italic; }

/* ── FOOTER ── */
footer { margin-top: 60px; padding-top: 16px; border-top: 1px solid var(--border); font-size: 0.8rem; color: var(--border); display: flex; justify-content: space-between; flex-wrap: wrap; gap: 8px; }
.footer-meta { font-style: italic; }
main img { max-width: 100%; height: auto; border: 1px solid var(--border); border-radius: 4px; margin: 16px 0; }

/* ── NYCKELORDSINDEX ── */
.kw-index { column-count: 3; column-gap: 32px; }
@media (max-width: 600px) { .kw-index { column-count: 1; } main { padding: 24px 16px; } }
.kw-entry { break-inside: avoid; margin-bottom: 10px; font-size: 0.9rem; line-height: 1.5; }
.kw-entry .kw-term { font-weight: bold; color: var(--red); }
.kw-entry .kw-pages a { font-size: 0.82rem; color: var(--link); margin-right: 6px; }
"""

# ── HTML-mall ─────────────────────────────────────────────
_current_nav_items = []  # sätts av build() före sidgenerering

def page_html(title, body, current_file, extra_head="", last_updated=None, version=None):
    nav_links = ""
    for fname, icon, label in _current_nav_items:
        if fname is None:
            nav_links += f'<span class="nav-section">{label}</span>\n'
        else:
            active = ' class="active"' if fname == current_file else ''
            nav_links += f'<a href="{fname}"{active}>{icon} {label}</a>\n'

    footer_left = "Drakar och Demoner Expert Wiki · Baserad på originalreglerna"
    footer_right = ""
    if last_updated or version:
        parts = []
        if version:
            parts.append(f"v{escape(version)}")
        if last_updated:
            parts.append(f"Uppdaterad {escape(last_updated)}")
        footer_right = f'<span class="footer-meta">{" · ".join(parts)}</span>'

    return f"""<!DOCTYPE html>
<html lang="sv">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{escape(title)} — DoDE Wiki</title>
<style>{CSS}</style>
{extra_head}
</head>
<body>
<nav id="topnav">
  <span class="site-title">⚔ DoDE Expert</span>
  {nav_links}
</nav>
<main>
{body}
</main>
<footer><span>{footer_left}</span>{footer_right}</footer>
</body>
</html>"""

# ── Markdown → HTML ────────────────────────────────────────
def slugify(text):
    """Skapar ett URL-säkert ankare från en rubriktext."""
    text = text.lower()
    text = text.replace('å','a').replace('ä','a').replace('ö','o')
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def add_heading_ids(html):
    """Lägger till id="slug" på alla h2/h3/h4-rubriker."""
    def replace_heading(m):
        tag = m.group(1)
        content = m.group(2)
        # Strippa eventuella inre HTML-taggar för att få ren text
        plain = re.sub(r'<[^>]+>', '', content)
        slug = slugify(plain)
        return f'<{tag} id="{slug}">{content}</{tag}>'
    return re.sub(r'<(h[2-4])>(.*?)</\1>', replace_heading, html, flags=re.DOTALL)

def md_to_html(md_text):
    md = mdlib.Markdown(extensions=["tables", "fenced_code"])
    html = md.convert(md_text)
    html = add_heading_ids(html)
    # Slå in tabeller i scrollbar-wrapper
    html = re.sub(r'<table>', '<div class="table-wrap"><table>', html)
    html = re.sub(r'</table>', '</table></div>', html)
    return html

# ── Korsreferenslänkning ──────────────────────────────────
# Längst nyckelord först för longest-match
SORTED_KW = sorted(KEYWORDS.keys(), key=len, reverse=True)

def add_wiki_links(html_body, current_file):
    """Ersätt första förekomsten av varje nyckelord med en wikilänk.
    Hoppar över innehåll inuti <h1-4>, <a>, <th>, <code>, <pre>."""
    linked = set()

    def replace_in_text(text, skip_page):
        for kw in SORTED_KW:
            if kw in linked:
                continue
            target_page, anchor = KEYWORDS[kw]
            if target_page == skip_page:
                continue  # Länka inte till den egna sidan
            # Matcha hela ord, skiftlägesokänsligt för första bokstav
            pattern = re.compile(
                r'(?<![a-zA-ZåäöÅÄÖ])' + re.escape(kw) + r'(?![a-zA-ZåäöÅÄÖ])'
            )
            def make_link(m, _kw=kw, _tp=target_page, _a=anchor):
                href = _tp + (f"#{_a}" if _a else "")
                return f'<a class="wikilink" href="{href}">{m.group(0)}</a>'
            new_text, count = pattern.subn(make_link, text, count=1)
            if count:
                linked.add(kw)
                return new_text
        return text

    # Tokenisera HTML och bearbeta bara textnoder utanför skip-taggar
    SKIP_TAGS = {'h1','h2','h3','h4','a','th','code','pre','script','style'}
    result = []
    skip_depth = 0
    pos = 0
    tag_re = re.compile(r'<(/?)(\w+)[^>]*>', re.IGNORECASE)

    for m in tag_re.finditer(html_body):
        start, end = m.span()
        closing = m.group(1) == '/'
        tag = m.group(2).lower()

        # Text innan denna tagg
        text_before = html_body[pos:start]
        if text_before and skip_depth == 0:
            text_before = replace_in_text(text_before, current_file)
        result.append(text_before)
        result.append(m.group(0))
        pos = end

        if tag in SKIP_TAGS:
            if closing:
                skip_depth = max(0, skip_depth - 1)
            else:
                skip_depth += 1

    # Rest
    tail = html_body[pos:]
    if tail and skip_depth == 0:
        tail = replace_in_text(tail, current_file)
    result.append(tail)

    return ''.join(result)

# ── Extrahera H2/H3-ankare (för nyckelordsindex) ──────────
def extract_title(md_text):
    m = re.search(r'^#\s+(.+)', md_text, re.MULTILINE)
    return m.group(1).strip() if m else "Sida"

# ── Nyckelordsindex ───────────────────────────────────────
def nearest_heading_anchor(html_body, kw):
    """Hitta id på närmaste h2/h3/h4 ovanför första förekomsten av kw."""
    pattern = r'(?<![a-zA-ZåäöÅÄÖ])' + re.escape(kw) + r'(?![a-zA-ZåäöÅÄÖ])'
    m = re.search(pattern, html_body, re.IGNORECASE)
    if not m:
        return None
    before = html_body[:m.start()]
    heading_re = re.compile(r'<h[2-4]\s+id="([^"]+)">', re.IGNORECASE)
    last = None
    for hm in heading_re.finditer(before):
        last = hm.group(1)
    return last

def build_keyword_index(page_contents):
    """Bygg {kw: [(page_file, page_title, anchor), ...]} med närmaste rubrik per sida."""
    index = {kw: [] for kw in KEYWORDS}
    for page_file, title, html_body in page_contents:
        plain = re.sub(r'<[^>]+>', '', html_body)
        for kw in KEYWORDS:
            pattern = r'(?<![a-zA-ZåäöÅÄÖ])' + re.escape(kw) + r'(?![a-zA-ZåäöÅÄÖ])'
            if re.search(pattern, plain, re.IGNORECASE):
                anchor = nearest_heading_anchor(html_body, kw)
                index[kw].append((page_file, title, anchor))
    return index

def render_keyword_index(kw_index, page_labels):
    """Rendera alfabetisk nyckelordslista som HTML."""
    items = sorted(kw_index.items(), key=lambda x: x[0].lower())
    parts = ['<div class="kw-index">']
    for kw, pages in items:
        if not pages:
            continue
        home_page, home_anchor = KEYWORDS[kw]
        link_parts = []
        seen = set()
        for pf, pt, page_anchor in sorted(pages, key=lambda x: x[1]):
            if pf in seen:
                continue
            seen.add(pf)
            if pf == home_page:
                # Hemsida: använd det definierade ankaret (mest exakt)
                anchor = home_anchor or page_anchor
            else:
                # Annan sida: använd närmaste rubrik där ordet nämns
                anchor = page_anchor
            href = f"{pf}#{anchor}" if anchor else pf
            link_parts.append(f'<a href="{href}">{escape(pt)}</a>')
        links = " ".join(link_parts)
        parts.append(
            f'<div class="kw-entry">'
            f'<span class="kw-term">{escape(kw)}</span><br>'
            f'<span class="kw-pages">{links}</span>'
            f'</div>'
        )
    parts.append('</div>')
    return '\n'.join(parts)

# ── Bygger en wiki ────────────────────────────────────────
def build(page_map, nav_items, out_dir, zip_prefix,
          index_title, index_subtitle, md_overrides=None):
    global _current_nav_items
    _current_nav_items = nav_items
    os.makedirs(out_dir, exist_ok=True)
    if out_dir != WIKI_MD_DIR:
        img_dst = os.path.join(out_dir, "images")
        img_src = os.path.join(os.path.join("docs", "wiki-html"), "images")
        if os.path.isdir(img_src) and not os.path.isdir(img_dst):
            import shutil
            shutil.copytree(img_src, img_dst)

    # Bygg md_files: bas från WIKI_MD_DIR, override med extra kataloger
    md_files = {}
    for path in glob.glob(os.path.join(WIKI_MD_DIR, "*.md")):
        key = os.path.splitext(os.path.basename(path))[0]
        md_files[key] = path
    if md_overrides:
        for key, path in md_overrides.items():
            if os.path.exists(path):
                md_files[key] = path

    pages = []  # (out_file, title, html_body_raw)
    for key, out_file in page_map.items():
        if key not in md_files:
            continue
        if key == "INDEX":
            continue
        with open(md_files[key], encoding="utf-8") as f:
            md_text = f.read()
        title = extract_title(md_text)
        html_body = md_to_html(md_text)
        pages.append((out_file, title, html_body))

    kw_index = build_keyword_index(pages)
    page_labels = {pf: pt for pf, pt, _ in pages}
    out_to_md = {page_map[k]: md_files[k] for k in page_map if k in md_files and k != "INDEX"}

    for out_file, title, html_body in pages:
        linked_body = add_wiki_links(html_body, out_file)
        mtime = os.path.getmtime(out_to_md[out_file])
        dt = datetime.datetime.fromtimestamp(mtime)
        full_html = page_html(title, linked_body, out_file,
                              last_updated=dt.strftime("%Y-%m-%d"),
                              version=dt.strftime("%Y.%m.%d"))
        out_path = os.path.join(out_dir, out_file)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(full_html)
        size = os.path.getsize(out_path) // 1024
        print(f"  {out_file} ({size} KB) — {title}")

    # Bygg index.html
    kw_html = render_keyword_index(kw_index, page_labels)
    valid_pages = {pf for pf, _, _ in pages}
    sections_html = ""
    current_section_cards = ""
    current_section_label = None

    def flush_section(label, cards):
        if not cards:
            return ""
        header = (
            f'<h2 style="margin-top:32px;margin-bottom:12px">{escape(label)}</h2>\n'
            if label else
            '<h2 style="margin-top:0;margin-bottom:12px">Sidor</h2>\n'
        )
        return (
            header +
            '<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:8px;margin-bottom:8px;">\n' +
            cards +
            '</div>\n'
        )

    for fname, icon, label in nav_items:
        if fname == "index.html":
            continue
        if fname is None:
            # Sektion-avdelare: spara ihop föregående sektion och starta ny
            sections_html += flush_section(current_section_label, current_section_cards)
            current_section_label = label
            current_section_cards = ""
            continue
        if fname not in valid_pages:
            continue
        current_section_cards += (
            f'<a href="{fname}" style="display:block;padding:12px 16px;'
            f'border:1px solid var(--border);border-radius:6px;'
            f'text-decoration:none;color:var(--text);'
            f'transition:background 0.1s;"'
            f' onmouseover="this.style.background=\'rgba(196,144,122,0.12)\'"'
            f' onmouseout="this.style.background=\'\'">'
            f'<span style="font-size:1.2rem;margin-right:8px">{icon}</span>'
            f'<strong style="color:var(--red)">{escape(label)}</strong>'
            f'</a>\n'
        )
    sections_html += flush_section(current_section_label, current_section_cards)

    index_body = f"""
<h1>{index_title}</h1>
<p>{index_subtitle}</p>

{sections_html}

<h2>Nyckelordsindex</h2>
<p style="font-size:0.88rem;color:var(--border);margin-bottom:16px;">
  Klicka på en sida för att hoppa direkt dit.
</p>
{kw_html}
"""
    latest_mtime = max(os.path.getmtime(p) for p in md_files.values()
                       if p in out_to_md.values() or p == md_files.get("INDEX"))
    latest_dt = datetime.datetime.fromtimestamp(latest_mtime)
    index_html = page_html(
        index_title, index_body, "index.html",
        last_updated=latest_dt.strftime("%Y-%m-%d"),
        version=latest_dt.strftime("%Y.%m.%d"),
    )
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)
    print(f"  index.html — Startsida + {len([k for k,v in kw_index.items() if v])} nyckelord")

    print(f"\nKlart! Filer i {out_dir}/")

    version_str = datetime.datetime.now().strftime("%Y.%m.%d_%H%M")
    os.makedirs("export", exist_ok=True)
    zip_path = os.path.join("export", f"{zip_prefix}_{version_str}.zip")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, _, files in os.walk(out_dir):
            for fname in files:
                fpath = os.path.join(root, fname)
                zf.write(fpath, os.path.relpath(fpath))
    zip_kb = os.path.getsize(zip_path) // 1024
    print(f"Uppdaterade {zip_path} ({zip_kb} KB)")


if __name__ == "__main__":
    print("\n=== Spelarwiki ===")
    build(
        page_map=PLAYER_PAGE_MAP,
        nav_items=PLAYER_NAV_ITEMS,
        out_dir=PLAYER_OUT_DIR,
        zip_prefix=PLAYER_ZIP_PREFIX,
        index_title=PLAYER_INDEX_TITLE,
        index_subtitle=PLAYER_INDEX_SUBTITLE,
        md_overrides=PLAYER_MD_OVERRIDES,
    )
