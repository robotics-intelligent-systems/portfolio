"""Build the portable GitHub Pages site from the reviewed portfolio snapshot."""
import json
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / 'data/portfolio.json').read_text())
OUT = ROOT / 'docs'
CONCEPT_COUNT = sum(len(g['concepts']) for g in DATA['gallery'])
CONCEPT_PROJECT_COUNT = len(DATA['gallery'])
BASE = 'https://robotics-intelligent-systems.github.io/portfolio/'
ORG = 'https://github.com/robotics-intelligent-systems'
PERSON = 'https://github.com/sdk2035'

def e(value):
    return escape(str(value), quote=True)

def link(url, text, cls=''):
    return f'<a class="{cls}" href="{e(url)}">{e(text)}</a>'

def page(title, description, body, section='', depth=0):
    prefix = '../' * depth or './'
    path = section + '/' if section else ''
    nav = ''.join(link(prefix + href, label, 'active' if section == key else '') for href, label, key in [('', 'Overview', ''), ('gallery/', 'Concept gallery', 'gallery'), ('management/', 'Management systems', 'management'), ('sdk2035/', 'sdk2035', 'sdk2035')])
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)} · Robotics &amp; Intelligent Systems</title>
<meta name="description" content="{e(description)}">
<meta name="theme-color" content="#152d32">
<link rel="canonical" href="{BASE}{path}">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(description)}">
<meta property="og:type" content="website"><meta property="og:url" content="{BASE}{path}">
<meta property="og:image" content="{e(DATA['gallery'][4]['concepts'][2]['thumbnail'])}">
<link rel="icon" href="{prefix}assets/mark.svg" type="image/svg+xml">
<link rel="stylesheet" href="{prefix}assets/site.css">
<script src="{prefix}assets/site.js" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><a class="brand" href="{prefix}"><span class="brand-mark" aria-hidden="true">R<span>+</span></span><span>Robotics &amp;<br>Intelligent Systems</span></a><nav aria-label="Primary">{nav}</nav>{link(ORG, 'GitHub ↗', 'github-link')}</header>
<main id="main">{body}</main>
<footer><div><strong>Robotics &amp; Intelligent Systems</strong><p>Open research. Clear interfaces. Engineering evidence.</p></div><div class="footer-links">{link(prefix + 'gallery/', 'Gallery')}{link(prefix + 'management/', 'Management systems')}{link(prefix + 'sdk2035/', 'Professional profile')}{link(ORG + '/portfolio', 'Website source ↗')}</div><p class="snapshot">Content snapshot · {e(DATA['updatedAt'])}<br>Source repositories define current project status.</p></footer>
</body></html>'''

def project_card(p):
    return f'<article class="project-card"><div class="project-card-top"><span class="eyebrow">{e(p["area"])}</span><span class="status">{e(p["status"])}</span></div><h3>{link(p["url"],p["name"] + " ↗")}</h3><p>{e(p["description"])}</p><details><summary>Next proposed AI-assisted task</summary><p>{e(p["nextTask"])}</p></details></article>'

def build_home():
    featured = DATA['gallery'][4]['concepts'][2]
    body = f'''<section class="hero overview-hero"><div class="hero-copy"><p class="eyebrow"><span class="signal"></span> THE OPEN ENGINEERING PORTFOLIO</p><h1>Ideas you can<br><em>explore.</em><br>Work you can trace.</h1><p class="lead">Robotics, digital twins and technical AI. Explore the organization's engineering concepts and meet the architect behind the connected software portfolio.</p><div class="actions">{link('gallery/', 'Explore the gallery ↗', 'button primary')}{link('management/', 'Management systems', 'button')}{link('sdk2035/', 'Meet sdk2035', 'button')}</div><div class="stats"><div><strong>{len(DATA["organization"])}</strong><span>JFX projects reviewed</span></div><div><strong>{len(DATA["organization"]) + len(DATA["personal"])}</strong><span>Global portfolio projects</span></div><div><strong>{CONCEPT_COUNT}</strong><span>Visual concepts</span></div><div><strong>{CONCEPT_PROJECT_COUNT}</strong><span>Projects with concepts</span></div></div></div><figure class="hero-visual"><a href="{e(featured['preview'])}"><img src="{e(featured['thumbnail'])}" alt="{e(featured['title'])}" fetchpriority="high"></a><figcaption><span>CONCEPT SPOTLIGHT / JFXFMIS</span><strong>Modular floating farm island</strong><span>Agriculture, structures and resource-loop interfaces.</span></figcaption><span class="visual-label">01 / ENGINEERING EXPLORATIONS</span></figure></section>
<section class="section"><div class="section-heading"><p class="eyebrow">TWO WAYS IN</p><h2>A connected portfolio.<br>Two distinct perspectives.</h2></div><div class="entry-grid"><a class="entry" href="gallery/"><span class="entry-number">01 / THE ORGANIZATION</span><h3>From concept<br>to engineering questions.</h3><p>Browse {CONCEPT_COUNT} CAD concept studies across maritime systems, aerospace, mobility, agriculture and energy. Every image links to its repository.</p><span class="entry-link">Open concept gallery <b>↗</b></span></a><a class="entry dark" href="sdk2035/"><span class="entry-number">02 / THE PROFESSIONAL</span><h3>Kevin Sanchez.<br>Software &amp; systems architecture.</h3><p>Enterprise modernization, AI integration, scientific computing and polyglot runtimes. Explore the professional profile and selected research work.</p><span class="entry-link">Meet sdk2035 <b>↗</b></span></a></div></section>
<section class="section approach"><p class="eyebrow">HOW THIS WORK IS ORGANIZED</p><h2>Make the boundaries explicit.</h2><div class="principles"><div><span>01</span><h3>Domain-owned models</h3><p>Each project owns its requirements, engineering data and acceptance decisions.</p></div><div><span>02</span><h3>Shared AI services</h3><p>Knowledge retrieval and language analysis connect through explicit integration contracts.</p></div><div><span>03</span><h3>Traceable evidence</h3><p>Visual studies introduce questions. Repository documentation and reproducible checks establish progress.</p></div></div></section>
<section class="source-note"><p><strong>A portfolio of explorations.</strong> Concept images illustrate design intent; they do not establish validated CAD geometry, certified systems or demonstrated performance. The organizational and professional portfolios have separate project scopes.</p>{link(ORG + '/.github', 'Read the organization profile ↗')}</section>'''
    (OUT / 'index.html').write_text(page('Portfolio', f'The engineering portfolio of Robotics & Intelligent Systems, with {CONCEPT_COUNT} CAD concept studies and the professional profile of sdk2035.', body))

def build_gallery():
    groups = []
    for group in DATA['gallery']:
        project = group['project']
        cards = []
        for c in group['concepts']:
            metadata = ''.join(f'<p><strong>{e(label)}:</strong> {e(c[key])}</p>' for key, label in [('category', 'Category'), ('references', 'References'), ('simulation', 'Proposed simulation'), ('status', 'Evidence status')] if c.get(key))
            technical_links = ' '.join(link(c[key], label, 'source-link') for key, label in [('requirements', 'High-level requirements ↗'), ('diagram', 'Editable Drawio ↗')] if c.get(key))
            search = ' '.join([project, c['title'], c['description']]).lower()
            cards.append(f'''<article class="concept" data-project="{e(project)}" data-search="{e(search)}"><div class="concept-copy"><span class="status">Visual concept</span><h3>{e(c['title'])}</h3><p>{e(c['description'])}</p>{metadata}{technical_links}{link(c['preview'], 'View repository source ↗', 'source-link')}</div><figure><a class="zoom" href="{e(c['preview'])}" data-image="{e(c['thumbnail'])}" data-title="{e(c['title'])}" aria-label="Preview {e(c['title'])}"><img src="{e(c['thumbnail'])}" alt="{e(c['title'])}" loading="lazy" decoding="async"><span>Enlarge ↗</span></a></figure></article>''')
        groups.append(f'<section class="concept-group" data-group="{e(project)}"><div class="group-heading"><h2>{link(ORG + "/" + project, project + " ↗")}</h2><span>{len(cards)} concept studies</span></div><div class="concept-grid">{"".join(cards)}</div></section>')
    options = ''.join(f'<option value="{e(p["project"])}">{e(p["project"])}</option>' for p in DATA['gallery'])
    no_images = [p for p in DATA['organization'] if p['name'] not in {x['project'] for x in DATA['gallery']}]
    directory = ''.join(project_card(p) for p in DATA['organization'])
    body = f'''<section class="page-intro"><p class="eyebrow">01 / ORGANIZATIONAL PORTFOLIO</p><h1>Engineering<br><em>in view.</em></h1><div class="intro-line"><p class="lead">{CONCEPT_COUNT} visual concepts. {CONCEPT_PROJECT_COUNT} projects. A source-linked window into the JFX engineering portfolio.</p>{link(ORG + '/.github', 'Organization profile ↗', 'text-link')}</div></section>
<div class="gallery-tools"><form role="search" id="gallery-search"><div class="search-field"><label for="search">Find a concept</label><input type="search" id="search" placeholder="Try hydrogen, habitat, amphibious…" autocomplete="off"></div><div class="project-field"><label for="project">Project</label><select id="project"><option value="all">All {CONCEPT_PROJECT_COUNT} projects</option>{options}</select></div><button class="button" type="reset">Reset filters</button></form><p id="result-count" role="status" aria-live="polite">Showing all {CONCEPT_COUNT} concepts</p><noscript><p>All concepts are visible below. Search and enlarged previews require JavaScript; repository links work without it.</p></noscript></div>
<p class="gallery-note">These are visual concept studies. Engineering validation is tracked separately in the source repositories.</p>
<div id="concepts">{''.join(groups)}</div><p id="no-results" class="empty" hidden>No concepts match those filters. Try another term or reset the filters.</p>
<section class="section"><div class="section-heading"><p class="eyebrow">THE BROADER CATALOG</p><h2>{len(DATA["organization"])} JFX projects.<br>One source of context.</h2><p>The {len(no_images)} projects without images in MBSE/CAD are included in this directory. Status and proposed tasks are snapshots from the organizational profile; progress estimates are editorial, not measured completion.</p></div><details class="directory"><summary>Explore all {len(DATA["organization"])} projects and their current status</summary><div class="project-grid">{directory}</div></details></section>
<dialog id="image-dialog" aria-labelledby="image-title"><div class="dialog-top"><h2 id="image-title"></h2><button type="button" id="close-dialog" aria-label="Close image preview">Close ×</button></div><img id="dialog-image" alt="Selected concept preview"><a id="dialog-source" href="{ORG}">Open the original repository image ↗</a></dialog>'''
    (OUT / 'gallery/index.html').write_text(page('Concept gallery', f'Browse {CONCEPT_COUNT} source-linked CAD concept images across {CONCEPT_PROJECT_COUNT} Robotics & Intelligent Systems projects, with search and project filters.', body, 'gallery', 1))

def build_professional():
    names = ['OpenBAP', 'GraalCOBOL', 'GraalRascal', 'jfxlegacy2modern', 'jfxengine', 'jfxmodelica']
    selected = ''.join(project_card(next(p for p in DATA['personal'] if p['name'] == n)) for n in names)
    remaining = ''.join(project_card(p) for p in DATA['personal'] if p['name'] not in names)
    body = f'''<section class="hero profile-hero"><div class="hero-copy"><p class="eyebrow">02 / PROFESSIONAL PROFILE · SDK2035</p><h1>Kevin<br><em>Sanchez.</em></h1><p class="role">Senior Software Engineer<br>&amp; Systems Architect</p><p class="lead">Enterprise modernization, AI integration and scientific computing. Modular systems with clear contracts and behavior-preserving validation.</p><div class="actions">{link('mailto:kjsanc@gmail.com', 'Start a conversation ↗', 'button primary')}{link('https://www.linkedin.com/in/kjsanc', 'LinkedIn ↗', 'button')}</div><p class="location">Lima, Peru · Open to remote opportunities, technical partnerships and collaborative R&amp;D.</p></div><aside class="profile-panel"><p class="eyebrow">EXPERIENCE &amp; FOCUS</p><div class="experience"><strong>10+</strong><span>years of experience</span></div><div class="experience"><strong>50+</strong><span>enterprise projects</span></div><p>FinTech, banking, microfinance, e-commerce, ERP and electronic invoicing.</p><p class="small">Experience figures and professional background are reported in the public sdk2035 profile.</p>{link(PERSON + '/sdk2035', 'Read the full professional profile ↗')}</aside></section>
<section class="section"><div class="section-heading"><p class="eyebrow">ENGINEERING FOCUS</p><h2>Modernize carefully.<br>Connect deliberately.</h2></div><div class="principles"><div><span>01</span><h3>Enterprise modernization</h3><p>Legacy integration, transaction-oriented systems and gradual migration across Java, .NET and cloud platforms.</p></div><div><span>02</span><h3>AI &amp; knowledge systems</h3><p>Source-linked retrieval, MCP and agent integration, private and hybrid inference, and explicit evaluation boundaries.</p></div><div><span>03</span><h3>Languages &amp; simulation</h3><p>GraalVM/Truffle, JVM/.NET interoperability, Modelica, scientific computing and 3D engineering workflows.</p></div></div></section>
<section class="section"><div class="section-heading"><p class="eyebrow">SELECTED PROJECTS</p><h2>Research with<br>a visible next step.</h2><p>These projects are architecture and research workstreams. Their source repositories define implementation status; proposed tasks do not establish completed integrations.</p></div><div class="project-grid">{selected}</div><details class="directory"><summary>Explore the other 23 personal portfolio projects</summary><div class="project-grid">{remaining}</div></details></section>
<section class="section stack"><p class="eyebrow">TECHNOLOGIES &amp; PRACTICES</p><h2>A toolset chosen<br>for each workload.</h2><div class="stack-grid"><div><h3>Software &amp; integration</h3><p>Java · C#/.NET · Python · TypeScript · Spring Boot · ASP.NET Core · REST · SOAP · OData · ETL</p></div><div><h3>Cloud &amp; delivery</h3><p>Azure · AWS · Docker · Kubernetes · Linux · CI/CD · RabbitMQ</p></div><div><h3>AI, languages &amp; science</h3><p>RAG · MCP · Ollama · GraalVM · Truffle · IKVM.NET · Modelica · Julia · SciPy · GNAT Ada</p></div><div><h3>Data &amp; business</h3><p>PostgreSQL · SQL Server · Oracle · MySQL · Payments · Microfinance · ERP interoperability</p></div></div></section>
<section class="contact-block"><div><p class="eyebrow">LET'S WORK TOGETHER</p><h2>Bring a concrete<br>engineering challenge.</h2><p>Remote engineering roles, enterprise modernization, research partnerships and technical co-founding.</p></div><div class="contact-links">{link('mailto:kjsanc@gmail.com', 'kjsanc@gmail.com ↗')}{link('https://www.linkedin.com/in/kjsanc', 'Connect on LinkedIn ↗')}{link(PERSON, 'Explore personal repositories ↗')}{link('../gallery/', 'Explore the organizational gallery ↗')}</div></section>'''
    (OUT / 'sdk2035/index.html').write_text(page('Kevin Sanchez · sdk2035', 'Senior Software Engineer & Systems Architect in Lima, Peru. Enterprise modernization, AI integration, scientific computing and polyglot runtimes.', body, 'sdk2035', 1))

def build_management():
    projects = {p['name']: p for p in DATA['organization']}
    cards = ''.join(project_card(projects[name]) for name in DATA['managementSystems'])
    body = f'''<section class="page-intro"><p class="eyebrow">03 / MANAGEMENT SYSTEMS</p><h1>Operations with<br><em>clear interfaces.</em></h1><div class="intro-line"><p class="lead">{len(DATA['managementSystems'])} domain projects for parking, farms, healthcare, business workflows, commerce, learning and industrial operations.</p>{link(ORG + '/.github', 'Organization profile ↗', 'text-link')}</div></section>
<section class="section"><div class="section-heading"><h2>Management across the portfolio.</h2><p>These projects are a selected subset of the {len(DATA['organization'])} organizational projects. Together with {len(DATA['personal'])} personal projects, the global catalog totals {len(DATA['organization']) + len(DATA['personal'])}; this tab adds no duplicate projects to that count.</p><p>Status and next tasks are documented snapshots. Architecture proposals require implementation and domain validation before deployment.</p></div><div class="project-grid">{cards}</div></section>
<section class="section"><article class="project-card"><h3>JFOXPMS · Parking management.</h3><p>Its current scope is a documentary compendium and integration proposal for spaces, reservations, occupancy, video supervision and free-software AI. The proposed camera/sensor, MQTT, PostgreSQL and identity interfaces are pending implementation.</p>{link(ORG + '/jfoxpms', 'Read the parking architecture ↗')}</article></section>'''
    (OUT / 'management/index.html').write_text(page('Management systems', 'Domain management systems in the JFX portfolio, including JFOXPMS parking management.', body, 'management', 1))

OUT.mkdir(exist_ok=True)
for folder in ['gallery', 'sdk2035', 'management', 'assets']:
    (OUT / folder).mkdir(exist_ok=True)
build_home()
build_gallery()
build_professional()
build_management()
(OUT / '.nojekyll').write_text('')
(OUT / 'assets/portfolio.json').write_text(json.dumps(DATA, indent=2) + '\n')
(OUT / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n')
(OUT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ''.join(f'<url><loc>{BASE}{p}</loc></url>' for p in ['', 'gallery/', 'management/', 'sdk2035/']) + '</urlset>\n')
print(f'Built 4 pages, {len(DATA["organization"])} organizational projects, {len(DATA["personal"])} personal projects and {sum(len(p["concepts"]) for p in DATA["gallery"])} concepts.')


