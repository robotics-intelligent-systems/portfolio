# Portfolio

Professional profile of **Kevin Sanchez (sdk2035)** and the **Robotics & Intelligent Systems** engineering concept gallery. A portable, dependency-free website in English, published with GitHub Pages.

- [Website](https://robotics-intelligent-systems.github.io/portfolio/)
- [Concept gallery](https://robotics-intelligent-systems.github.io/portfolio/gallery/)
- [Professional profile](https://robotics-intelligent-systems.github.io/portfolio/sdk2035/)

## Structure

```text
data/portfolio.json       Reviewed content and source blob references
scripts/build.py         Static page generator (Python standard library)
docs/index.html          Portfolio overview
docs/gallery/index.html  67 concepts, search, project filters and image previews
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

Edit `data/portfolio.json`, regenerate with `python3 scripts/build.py`, validate the three pages and commit both the source data and generated pages. The generated `docs/assets/portfolio.json` mirrors the reviewed content. GitHub Pages publishes updates to `main` automatically.

The original content baseline is dated **2026-10-11**, with scoped JFXOSMS infrastructure and JFXAI4MOMS NEREO/LUMEN-3 additions on **2026-10-12** and sourced from:

- [sdk2035's professional profile](https://github.com/sdk2035/sdk2035)
- [Organizational profile and current project catalog](https://github.com/robotics-intelligent-systems/.github)
- [CAD catalog](https://github.com/robotics-intelligent-systems/.github/blob/main/profile/cad-catalog.json)

The gallery includes **67 images in 21 projects**, within the **47-project JFX catalog**. Images load directly from source repositories and retain original source links. Their rights and licenses are governed by those sources; this repository does not relicense third-party images. Remote image availability depends on the source repositories.

Professional experience figures come from the public profile. Project statuses and next AI-assisted tasks are dated snapshots. Visual concepts do not establish validated CAD geometry or demonstrated performance.

