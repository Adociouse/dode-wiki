# -*- coding: utf-8 -*-
"""
make_wiki.py — Bygger DoDE_Wiki.html från docs/wiki/*.md
Kör: python make_wiki.py
"""
import os, re, glob
import markdown

WIKI_DIR = "src"
OUT_FILE = os.path.join("dev", "DoDE_Wiki.html")

# Ordning på sektioner (filnamn utan .md)
SECTION_ORDER = [
    "INDEX",
    "REGLER_EGENSKAPER",
    "REGLER_STRID",
    "REGLER_FARDIGHETER",
    "RASER",
    "YRKEN",
    "MAGI",
    "UTRUSTNING",
    "HJALTAR",
    "MONSTER",
    "DEMONOLOGI",
]

SECTION_ICONS = {
    "INDEX":             "📖",
    "REGLER_EGENSKAPER": "💪",
    "REGLER_STRID":      "⚔️",
    "REGLER_FARDIGHETER":"🎯",
    "RASER":             "🧝",
    "YRKEN":             "🛡️",
    "MAGI":              "✨",
    "UTRUSTNING":        "🗡️",
    "HJALTAR":           "🌟",
    "MONSTER":           "🐉",
    "DEMONOLOGI":        "🔮",
}

CSS = """
:root {
  --dode-red:      #6B1A1A;
  --dode-red-dark: #4A0E0E;
  --dode-paper:    #FAF3F0;
  --dode-text:     #2A0808;
  --dode-gold:     #D4956B;
  --dode-border:   #C4907A;
  --dode-input-bg: #FFF5F2;
  --sidebar-w:     280px;
}
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { font-size: 16px; }
body {
  font-family: 'Palatino Linotype', Palatino, Georgia, serif;
  background: var(--dode-paper);
  color: var(--dode-text);
  display: flex;
  min-height: 100vh;
}

/* ── SIDEBAR ── */
#sidebar {
  width: var(--sidebar-w);
  min-width: var(--sidebar-w);
  background: var(--dode-red-dark);
  color: #F5E6D3;
  display: flex;
  flex-direction: column;
  position: sticky;
  top: 0;
  height: 100vh;
  overflow-y: auto;
  flex-shrink: 0;
}
#sidebar-header {
  padding: 20px 16px 12px;
  border-bottom: 1px solid rgba(212,149,107,0.3);
}
#sidebar-header h1 {
  font-size: 1.1rem;
  color: var(--dode-gold);
  line-height: 1.3;
  margin-bottom: 4px;
}
#sidebar-header p {
  font-size: 0.72rem;
  opacity: 0.7;
  font-style: italic;
}
#search-wrap {
  padding: 10px 12px;
  border-bottom: 1px solid rgba(212,149,107,0.2);
}
#search {
  width: 100%;
  padding: 7px 10px;
  border: 1px solid var(--dode-gold);
  border-radius: 4px;
  background: rgba(255,255,255,0.08);
  color: #F5E6D3;
  font-size: 0.85rem;
  outline: none;
}
#search::placeholder { opacity: 0.5; }
#search:focus { background: rgba(255,255,255,0.14); }
#nav-list {
  list-style: none;
  padding: 8px 0;
  flex: 1;
}
#nav-list li a {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 9px 16px;
  color: #F5E6D3;
  text-decoration: none;
  font-size: 0.88rem;
  border-left: 3px solid transparent;
  transition: background 0.15s, border-color 0.15s;
}
#nav-list li a:hover,
#nav-list li a.active {
  background: rgba(212,149,107,0.15);
  border-left-color: var(--dode-gold);
  color: #fff;
}
#nav-list li a .icon { font-size: 1rem; width: 22px; text-align: center; }
#nav-list li a .label { flex: 1; }
#nav-list li a.hidden { display: none; }

/* ── MAIN CONTENT ── */
#content {
  flex: 1;
  padding: 0;
  overflow-y: auto;
  scroll-behavior: smooth;
}
.wiki-section {
  padding: 36px 48px 48px;
  border-bottom: 2px solid var(--dode-border);
  max-width: 900px;
}
.wiki-section:last-child { border-bottom: none; }

/* ── TYPOGRAPHY ── */
.wiki-section h1 {
  font-size: 2rem;
  color: var(--dode-red);
  border-bottom: 3px solid var(--dode-gold);
  padding-bottom: 10px;
  margin-bottom: 24px;
}
.wiki-section h2 {
  font-size: 1.4rem;
  color: var(--dode-red-dark);
  margin: 28px 0 12px;
  padding-bottom: 4px;
  border-bottom: 1px solid var(--dode-border);
}
.wiki-section h3 {
  font-size: 1.1rem;
  color: var(--dode-red);
  margin: 20px 0 8px;
}
.wiki-section h4 {
  font-size: 1rem;
  font-weight: bold;
  color: var(--dode-text);
  margin: 16px 0 6px;
}
.wiki-section p { line-height: 1.7; margin-bottom: 12px; }
.wiki-section ul, .wiki-section ol {
  margin: 8px 0 14px 24px;
  line-height: 1.7;
}
.wiki-section li { margin-bottom: 4px; }

/* ── TABLES ── */
.wiki-section table {
  width: 100%;
  border-collapse: collapse;
  margin: 16px 0;
  font-size: 0.88rem;
  overflow-x: auto;
  display: block;
}
.wiki-section th {
  background: var(--dode-red);
  color: var(--dode-gold);
  padding: 8px 10px;
  text-align: left;
  font-weight: bold;
  white-space: nowrap;
}
.wiki-section td {
  padding: 7px 10px;
  border-bottom: 1px solid var(--dode-border);
}
.wiki-section tr:nth-child(even) td { background: rgba(196,144,122,0.08); }
.wiki-section tr:hover td { background: rgba(196,144,122,0.16); }

/* ── CODE / BLOCKQUOTE ── */
.wiki-section code {
  background: rgba(107,26,26,0.08);
  padding: 2px 6px;
  border-radius: 3px;
  font-family: monospace;
  font-size: 0.88em;
}
.wiki-section pre {
  background: rgba(107,26,26,0.06);
  border: 1px solid var(--dode-border);
  border-radius: 6px;
  padding: 14px 16px;
  overflow-x: auto;
  margin: 14px 0;
}
.wiki-section pre code { background: none; padding: 0; }
.wiki-section blockquote {
  border-left: 4px solid var(--dode-gold);
  padding: 10px 16px;
  margin: 14px 0;
  background: rgba(212,149,107,0.08);
  font-style: italic;
}

/* ── SEARCH HIGHLIGHT ── */
.search-hl { background: #FFE08A; border-radius: 2px; }

/* ── NO MATCH ── */
#no-match {
  display: none;
  padding: 40px 48px;
  color: #999;
  font-style: italic;
}

/* ── RESPONSIVE ── */
#menu-toggle {
  display: none;
  position: fixed;
  top: 12px; left: 12px;
  z-index: 200;
  background: var(--dode-red);
  color: var(--dode-gold);
  border: none;
  border-radius: 6px;
  padding: 8px 12px;
  font-size: 1.2rem;
  cursor: pointer;
}
@media (max-width: 768px) {
  #menu-toggle { display: block; }
  #sidebar {
    position: fixed;
    left: -var(--sidebar-w);
    transform: translateX(calc(-1 * var(--sidebar-w)));
    transition: transform 0.25s;
    z-index: 100;
  }
  #sidebar.open { transform: translateX(0); }
  .wiki-section { padding: 24px 20px; }
}

@media (prefers-color-scheme: dark) {
  :root {
    --dode-paper:    #1E1010;
    --dode-text:     #F0DDD5;
    --dode-input-bg: #2A1414;
    --dode-border:   #8B5A44;
  }
}
"""

JS = r"""
(function() {
  // Smooth-scroll nav
  document.querySelectorAll('#nav-list a[href^="#"]').forEach(function(a) {
    a.addEventListener('click', function(e) {
      e.preventDefault();
      var target = document.querySelector(this.getAttribute('href'));
      if (target) target.scrollIntoView({ behavior: 'smooth' });
      document.querySelectorAll('#nav-list a').forEach(function(x) { x.classList.remove('active'); });
      a.classList.add('active');
      if (window.innerWidth < 768) document.getElementById('sidebar').classList.remove('open');
    });
  });

  // Mobile toggle
  var toggle = document.getElementById('menu-toggle');
  if (toggle) toggle.addEventListener('click', function() {
    document.getElementById('sidebar').classList.toggle('open');
  });

  // Search
  var searchInput = document.getElementById('search');
  searchInput.addEventListener('input', function() {
    var q = this.value.trim().toLowerCase();
    var navItems = document.querySelectorAll('#nav-list li a');
    var sections = document.querySelectorAll('.wiki-section');
    var noMatch = document.getElementById('no-match');
    var anyVisible = false;

    sections.forEach(function(sec) {
      // Remove old highlights
      sec.querySelectorAll('.search-hl').forEach(function(el) {
        el.replaceWith(document.createTextNode(el.textContent));
      });
      sec.normalize();
    });

    if (!q) {
      sections.forEach(function(sec) { sec.style.display = ''; });
      navItems.forEach(function(a) { a.classList.remove('hidden'); });
      noMatch.style.display = 'none';
      return;
    }

    sections.forEach(function(sec, i) {
      var text = sec.textContent.toLowerCase();
      var match = text.includes(q);
      sec.style.display = match ? '' : 'none';
      navItems[i] && (match ? navItems[i].classList.remove('hidden') : navItems[i].classList.add('hidden'));
      if (match) anyVisible = true;

      // Highlight matches in visible sections
      if (match) highlightInNode(sec, q);
    });

    noMatch.style.display = anyVisible ? 'none' : 'block';
  });

  function highlightInNode(node, q) {
    if (node.nodeType === 3) { // text node
      var idx = node.textContent.toLowerCase().indexOf(q);
      if (idx < 0) return;
      var before = document.createTextNode(node.textContent.slice(0, idx));
      var mark = document.createElement('mark');
      mark.className = 'search-hl';
      mark.textContent = node.textContent.slice(idx, idx + q.length);
      var after = document.createTextNode(node.textContent.slice(idx + q.length));
      var parent = node.parentNode;
      parent.insertBefore(before, node);
      parent.insertBefore(mark, node);
      parent.insertBefore(after, node);
      parent.removeChild(node);
      // Continue after the highlight
      highlightInNode(after, q);
    } else if (node.nodeType === 1 && !['SCRIPT','STYLE','MARK'].includes(node.tagName)) {
      Array.from(node.childNodes).forEach(function(child) { highlightInNode(child, q); });
    }
  }

  // Intersection observer for active nav highlight
  var observer = new IntersectionObserver(function(entries) {
    entries.forEach(function(e) {
      if (e.isIntersecting) {
        var id = e.target.id;
        document.querySelectorAll('#nav-list a').forEach(function(a) {
          a.classList.toggle('active', a.getAttribute('href') === '#' + id);
        });
      }
    });
  }, { threshold: 0.1 });
  document.querySelectorAll('.wiki-section').forEach(function(s) { observer.observe(s); });
})();
"""

def slugify(name):
    return name.lower().replace("_", "-")

def extract_title(md_text):
    m = re.search(r'^#\s+(.+)', md_text, re.MULTILINE)
    return m.group(1).strip() if m else "Wiki"

def md_to_html(md_text):
    md = markdown.Markdown(extensions=['tables', 'fenced_code', 'toc'])
    return md.convert(md_text)

def build_wiki():
    sections = []
    found_files = {os.path.splitext(os.path.basename(f))[0]: f
                   for f in glob.glob(os.path.join(WIKI_DIR, "*.md"))}

    order = [s for s in SECTION_ORDER if s in found_files]
    # Add any extras not in the order list
    for k in sorted(found_files.keys()):
        if k not in order:
            order.append(k)

    for key in order:
        path = found_files[key]
        with open(path, encoding="utf-8") as f:
            md_text = f.read()
        title = extract_title(md_text)
        html_body = md_to_html(md_text)
        icon = SECTION_ICONS.get(key, "📄")
        sections.append({"key": key, "slug": slugify(key), "title": title, "icon": icon, "html": html_body})

    # Build nav
    nav_items = "\n".join(
        '<li><a href="#{slug}"><span class="icon">{icon}</span><span class="label">{title}</span></a></li>'.format(**s)
        for s in sections
    )

    # Build content
    content_sections = "\n".join(
        '<section class="wiki-section" id="{slug}">\n{html}\n</section>'.format(**s)
        for s in sections
    )

    html = """<!DOCTYPE html>
<html lang="sv">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Drakar och Demoner Expert — Wiki</title>
<style>{css}</style>
</head>
<body>
<button id="menu-toggle">☰</button>
<nav id="sidebar">
  <div id="sidebar-header">
    <h1>⚔ Drakar och Demoner Expert</h1>
    <p>Rollspelswiki · Ereb Altor</p>
  </div>
  <div id="search-wrap">
    <input type="text" id="search" placeholder="🔍 Sök i wikin..." autocomplete="off">
  </div>
  <ul id="nav-list">
{nav}
  </ul>
</nav>
<main id="content">
{sections}
<div id="no-match">Inga träffar. Försök med ett annat sökord.</div>
</main>
<script>{js}</script>
</body>
</html>""".format(
        css=CSS,
        nav=nav_items,
        sections=content_sections,
        js=JS
    )

    os.makedirs("dev", exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write(html)

    total_kb = os.path.getsize(OUT_FILE) // 1024
    print("Byggde %s (%d KB, %d sektioner)" % (OUT_FILE, total_kb, len(sections)))
    print("Sektioner: " + ", ".join(s["key"] for s in sections))

if __name__ == "__main__":
    build_wiki()
