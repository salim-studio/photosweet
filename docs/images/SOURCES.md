# Image sources

| File | Content | Source / licence |
|---|---|---|
| `photosweet-hero.jpg` | PhotoSweet UI screenshot (offscreen snapshot) — the mark drawn entirely in the app on the deep Pro theme | No external artwork; UI and vector composition made in the app. |
| `photosweet-adjustments.jpg` | PhotoSweet UI screenshot (offscreen snapshot) with *Wanderer above the Sea of Fog*, Caspar David Friedrich, c. 1818 — gradient map / photo filter / curves stack, Adjustments + Histogram panels | Artwork: public domain, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Caspar_David_Friedrich_-_Wanderer_above_the_sea_of_fog.jpg). UI: this project. |
| `photosweet-mask.jpg` | PhotoSweet UI screenshot (offscreen snapshot) with *The Birth of Venus*, Sandro Botticelli, c. 1485 — alpha channel from an elliptical selection, Channels panel | Artwork: public domain, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Sandro_Botticelli_-_La_nascita_di_Venere_-_Google_Art_Project.jpg). UI: this project. |
| `photosweet-type.jpg` | PhotoSweet UI screenshot (offscreen snapshot) — editorial quote card with box text, Character panel, all drawn in the app | No external artwork; UI and typographic composition made in the app. |
| `photosweet-layer-style.jpg` | PhotoSweet UI screenshot (offscreen snapshot) — neon "SPARKLE" with drop shadow / outer glow / stroke, Layer Style dialog open | No external artwork; UI and effects showcase made in the app. |
| `photosweet-vector.jpg` | PhotoSweet UI screenshot (offscreen snapshot) — hex badge + star + arrow, gradient fills, dashed strokes, Paths panel with Pen tool | No external artwork; vector illustration made in the app. |
| `photosweet-filter.jpg` | PhotoSweet UI screenshot (offscreen snapshot) with *Brig upon the Water*, Gustave Le Gray, 1856 — Blur Gallery (iris blur) on an early photograph | Artwork: public domain, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Gustave_Le_Gray_-_Brig_upon_the_Water_-_Google_Art_Project.jpg). UI: this project. |
| `photosweet-transform.jpg` | PhotoSweet UI screenshot (offscreen snapshot) with *A Sunday on La Grande Jatte*, Georges Seurat, 1884 — Free Transform handles, History panel | Artwork: public domain, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:A_Sunday_on_La_Grande_Jatte,_Georges_Seurat,_1884.jpg). UI: this project. |
| `photosweet-export.jpg` | PhotoSweet UI screenshot (offscreen snapshot) with *The Fighting Temeraire*, J. M. W. Turner, 1839 — Vibrance adjustment, Export As dialog on dark theme | Artwork: public domain, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:The_Fighting_Temeraire,_JMW_Turner,_National_Gallery.jpg). UI: this project. |

Every screenshot is the real app rendered offscreen through its control channel (the snapshot
example above, or `ui.screenshot` over `--control`). No image is a mockup, and the offscreen
capture was made with an embedded ICC profile stripped from the artwork so the run is
non-interactive.

Screenshots must use famous public-domain artwork (or content made in the app), never personal photos.

# Other bundled data

| File | Content | Source / licence |
|---|---|---|
| `assets/dict/en_US-scowl-50.txt.gz` | English word list (72,403 words, American spelling) for Edit › Check Spelling | [SCOWL](http://wordlist.aspell.net/) 2020.12.07, size 50, by Kevin Atkinson: permissive licence (use, copy, modify, distribute and sell, keeping the notice); full text and build recipe in `assets/dict/LICENSE-SCOWL.txt`. |