# Portfolio

Professional profile of **Kevin Sanchez (sdk2035)** and the **Robotics & Intelligent Systems** engineering concept gallery. A portable, dependency-free website in English, published with GitHub Pages.

- [Website](https://robotics-intelligent-systems.github.io/portfolio/)
- [Concept gallery](https://robotics-intelligent-systems.github.io/portfolio/gallery/)
- [Management systems](https://robotics-intelligent-systems.github.io/portfolio/management/)
- [Professional profile](https://robotics-intelligent-systems.github.io/portfolio/sdk2035/)
- [Carapace-Nereida H₂ · hybrid submarine superyacht concept](https://robotics-intelligent-systems.github.io/portfolio/twins/submarine-hotel/)

## Structure

```text
data/portfolio.json       Reviewed content and source blob references
scripts/build.py         Static page generator (Python standard library)
docs/index.html          Portfolio overview
docs/gallery/index.html  70 concepts, search, project filters and image previews
docs/management/index.html  Management systems, including JFOXPMS
docs/twins/submarine-hotel/index.html  Carapace-Nereida H₂ concept board and fusion overview
docs/sdk2035/index.html   Professional profile and 29 personal projects
docs/assets/             Styles, progressive enhancement and exported data
```

## Local preview

```sh
python3 scripts/build.py
python3 -m http.server 8000 --directory docs
```

Open `http://localhost:8000/`. Relative links support both this preview and the `/portfolio/` GitHub Pages path. All content and source links remain available without JavaScript; search and enlarged previews use JavaScript.

## Publication

In **Settings → Pages**, select **Deploy from a branch**, **main**, **/docs**, then save. The `.nojekyll` file keeps this a static site. No custom domain or CNAME is configured.

## Content maintenance

Edit `data/portfolio.json`, regenerate with `python3 scripts/build.py`, validate the four pages and commit both the source data and generated pages. The generated `docs/assets/portfolio.json` mirrors the reviewed content. The submarine concept page is standalone Spanish HTML and references its illustration in `docs/assets/`; it is separate from the portfolio data generator. GitHub Pages publishes updates to `main` automatically.

The original content baseline is dated **2026-10-11**, with scoped JFXOSMS infrastructure and JFXAI4MOMS NEREO/LUMEN-3 additions on **2026-10-12** and sourced from:

- [sdk2035's professional profile](https://github.com/sdk2035/sdk2035)
- [Organizational profile and current project catalog](https://github.com/robotics-intelligent-systems/.github)
- [CAD catalog](https://github.com/robotics-intelligent-systems/.github/blob/main/profile/cad-catalog.json)

The gallery includes **70 images in 23 projects**, within the **48-project JFX catalog**. Three JFXAI4RPCS agricultural concepts were added on **2026-10-13** from its `MBSE/CAD` JPG assets, with visual-completion and pending-validation status. Images load directly from source repositories and retain original source links. Their rights and licenses are governed by those sources; this repository does not relicense third-party images. Remote image availability depends on the source repositories.

Professional experience figures come from the public profile. Project statuses and next AI-assisted tasks are dated snapshots. Visual concepts do not establish validated CAD geometry or demonstrated performance.


Scoped update · 2026-10-13: the protected truck and hydrogen-hybrid amphibious transport now belong to JFXAI4RFFS. Original assets, requirements and editable Draw.io links point to the destination; the image count remains 70.


Scoped update · 2026-10-13: JFOXPMS joins the organizational catalog (48 projects), bringing the global catalog to 77 (29 personal + 48 organizational). The Management systems tab groups existing domain projects without double counting. JFOXPMS remains an architecture proposal with implementation pending.
