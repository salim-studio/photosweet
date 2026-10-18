<p align="center">
  <a href="https://salim-studio.github.io/photosweet/">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="docs/brand/photosweet-logo-white.svg">
      <img alt="PhotoSweet" src="docs/brand/photosweet-logo.svg" width="220">
    </picture>
  </a>
</p>

<h1 align="center">PhotoSweet</h1>

<p align="center">
  <b>A real image editor that never asks you to sign in.</b><br>
  Layers, masks, adjustment layers, layer styles, type, vectors, brushes and real PSD files,<br>
  native on macOS, Windows, Linux and FreeBSD, and running in your browser. Offline, and yours.
</p>

<p align="center">
  <img alt="100% Rust" src="https://img.shields.io/badge/100%25-Rust-b7410e?style=flat-square&logo=rust">
  <img alt="macOS · Windows · Linux · FreeBSD · Web" src="https://img.shields.io/badge/macOS%20%C2%B7%20Windows%20%C2%B7%20Linux%20%C2%B7%20FreeBSD%20%C2%B7%20Web-native-8b5cf6?style=flat-square">
  <img alt="License: MIT OR Apache-2.0" src="https://img.shields.io/badge/license-MIT%20%2F%20Apache--2.0-3a3a3a?style=flat-square">
  <img alt="Status: early alpha" src="https://img.shields.io/badge/status-early%20alpha-d69e2e?style=flat-square">
</p>

<p align="center">
  <a href="https://salim-studio.github.io/photosweet/"><b>Open PhotoSweet in your browser</b></a> ·
  <a href="https://github.com/salim-studio/photosweet">GitHub</a> ·
  <a href="https://github.com/salim-studio/photosweet/issues">Issues</a>
</p>

<br>

<p align="center">
  <img src="docs/images/photosweet-hero.jpg" alt="PhotoSweet editing Hokusai's The Great Wave: a white caption card with a drop shadow, Title and Credit type layers, and Vibrance and Curves adjustment layers in the Layers panel" width="100%">
</p>

## Lens and sparkle

The mark is a lens and a sparkle, and that is the whole idea. A **lens**, because a photograph
deserves the real thing: layers, masks, channels, curves, colour management, PSD. A **sparkle**,
because editing should feel like a quiet pleasure rather than a subscription — no account, no
cloud, no telemetry, nothing uploaded, nothing switched off next year.

PhotoSweet is that lens and that sparkle in one window, written in Rust, with a GPU compositor
and a CPU oracle behind it. It opens your files, keeps them yours, and stays fast on a laptop.

<br>

<p align="center">
  <a href="#a-walk-through-one-photograph">A walk through one photograph</a> ·
  <a href="#everything-in-the-box">Everything in the box</a> ·
  <a href="#psd-without-compromise">PSD</a> ·
  <a href="#built-for-agents">Agents</a> ·
  <a href="#under-the-hood">Under the hood</a> ·
  <a href="#get-started">Get started</a> ·
  <a href="#downloads">Downloads</a>
</p>

<br>

<table>
  <tr>
    <td width="25%" valign="top">
      <h3>🎛️ Familiar by design</h3>
      The menus, shortcuts, panels and tools are where your hands expect them, from ⌘J to ⇧⌘D. If you know Photoshop, you already know PhotoSweet.
    </td>
    <td width="25%" valign="top">
      <h3>⚡ Native and fast</h3>
      A GPU compositor on wgpu (Metal, Vulkan, DX12, WebGPU), copy-on-write tiles and multithreaded filters. No Electron, no web view, no waiting.
    </td>
    <td width="25%" valign="top">
      <h3>🗂️ Real PSD files</h3>
      Open, edit and save layered Photoshop documents. Re-saving keeps the render of 307 of the 309 psd-tools test files.
    </td>
    <td width="25%" valign="top">
      <h3>🤖 Agent-ready</h3>
      Every action is a command, so you can drive the same engine from the UI, the CLI, a JSON control channel or an MCP server.
    </td>
  </tr>
</table>

<br>

## A walk through one photograph

Every image below is the real app, working on public-domain art, rendered offscreen through its
own control channel — the same commands a script or an agent would send. Nothing is a mockup.

<h3>1. Open it</h3>

<p>
  <img src="docs/images/photosweet-hero.jpg" alt="The Great Wave in PhotoSweet: a caption card with a drop shadow, live type, and a Curves layer selected in the Layers panel" width="100%">
</p>

Hokusai's wave, 1831, straight into a window with a real Layers panel. Double-click a layer to
rename it, drag it to restack it, click the eye to hide it. PSD, PSB, TIFF, PDN, OpenRaster,
Krita, SVG, Affinity documents and every flat format you own open the same way — and the app never
touches the original until you say so.

<h3>2. Tune the light</h3>

<p>
  <img src="docs/images/photosweet-adjustments.jpg" alt="Monet's Impression, Sunrise with Levels and Vibrance adjustment layers and the Curves editor open over the live histogram" width="100%">
</p>

Adjustment layers keep every edit live: Levels with its histogram, Curves with per-channel
editing, Vibrance, Hue/Saturation and a dozen more. Stack them, mask them, reorder them, turn them
off and on again. Your pixels are never baked, so you can always walk back to the beginning.

<h3>3. Change only what you mean to change</h3>



An elliptical selection becomes the mask of a Hue/Saturation layer, so the face keeps its colour
and the room behind her goes quiet. Marquees, lassos, the Magic Wand, Quick Selection, Object
Selection, Select Subject and Select and Mask all feed the same idea: a selection is not a special
mode, it is the start of a mask, a path or a shape.

<h3>4. Set the words</h3>

<p>
  <img src="docs/images/photosweet-type.jpg" alt="Bierstadt's Among the Sierra Nevada with a headline, a byline and a caption set as live type, and the Character and Paragraph controls docked on the right" width="100%">
</p>

Point and paragraph text, edited right on the canvas, with the full Character and Paragraph
controls: font, weight, size, leading, tracking, alignment, and the <a href="docs/color-picker.md">Type
Color Picker</a> with its pixel loupe for sampling from the image. Type layers stay editable, take
layer styles, and round-trip through PSD.

<h3>5. Dress it up</h3>

<p>
  <img src="docs/images/photosweet-layer-style.jpg" alt="The Layer Style dialog editing an Outer Glow on the EARTHRISE type layer, with Stroke also enabled, over Apollo 8's Earthrise" width="100%">
</p>

Drop Shadow, Inner Shadow, Outer and Inner Glow, Bevel &amp; Emboss, Satin, Stroke, and Color,
Gradient and Pattern Overlay — live on any layer, including type. Copy and paste styles between
layers, hide them all at once, and open the styles that came in a PSD, rendered to match
Photoshop.

<h3>6. Draw something sharp</h3>

<p>
  <img src="docs/images/photosweet-vector.jpg" alt="A badge built from shape layers in the brand's violet, rose and amber over Monet's Water Lilies, with the Shape properties on the right" width="100%">
</p>

Rectangle, Ellipse, Triangle, Polygon, Line and the Pen, Freeform Pen and Curvature Pen tools make
resolution-independent shape layers with gradient fills and dashed, aligned strokes. Combine them,
keep them in the Paths panel, use them as vector masks, or stroke and fill them. 116 of 116 shape
layers in our PSD corpus match Photoshop's pixels.

<h3>7. See it before you commit</h3>

<p>
  <img src="docs/images/photosweet-filter.jpg" alt="The Twirl filter previewing live inside an elliptical selection on Van Gogh's The Starry Night" width="100%">
</p>

Every filter dialog previews on the canvas, through your selection. Blurs (Gaussian, Box, Motion,
Radial, Surface, Smart, Lens, Shape and the Blur Gallery), sharpening, Reduce Noise, distortions,
Pixelate, Stylize, Render and more. Put a filter on a smart object and it stays editable: change,
hide, reorder or mask it at any time.

<h3>8. Reshape it</h3>

<p>
  <img src="docs/images/photosweet-transform.jpg" alt="A Free Transform box around Ansel Adams' The Tetons and the Snake River, with the steps listed in the History panel" width="100%">
</p>

Free Transform with scale, rotate, skew, distort and perspective; exact 90° and 180° rotations and
flips; Transform Again. Layers, type, shapes, masks and selections transform together — and every
step sits in the History panel, one brush stroke at a time.

<h3>9. Ship it</h3>

<p>
  <img src="docs/images/photosweet-export.jpg" alt="The Export As dialog over Klimt's The Kiss: PNG at 50 percent scale, with a preview and an estimated file size" width="100%">
</p>

Export As with format, quality, transparency and scale, a preview and an instant size estimate, or
Quick Export to PNG in one click. Choose the dark Pro themes, the airy Studio themes, or a Classic
look — the interface is yours too.

<br>

## Everything in the box

<table>
  <tr>
    <td width="33%" valign="top">
      <h4>🧰 67 tools</h4>
      Move · Artboard · Rectangular and Elliptical Marquee · Single Row Marquee · Single Column Marquee · Lasso · Polygonal Lasso · Magnetic Lasso · Object Selection · Quick Selection · Magic Wand · Crop · Perspective Crop · Slice · Slice Select · Frame · Eyedropper · Color Sampler · Ruler · Note · Count · Remove · Spot Healing Brush · Healing Brush · Patch · Content-Aware Move · Red Eye · Brush · Pencil · Mixer Brush · Color Replacement · Clone Stamp · Pattern Stamp · History Brush · Eraser · Background Eraser · Magic Eraser · Gradient · Paint Bucket · Blur · Sharpen · Smudge · Dodge · Burn · Sponge · Pen · Freeform Pen · Curvature Pen · Add Anchor Point · Delete Anchor Point · Convert Point · Horizontal and Vertical Type · Horizontal and Vertical Type Mask · Path Selection · Direct Selection · Rectangle · Ellipse · Triangle · Polygon · Line · Custom Shape · Hand · Rotate View · Zoom
    </td>
    <td width="33%" valign="top">
      <h4>🖌️ A real brush engine</h4>
      Shape Dynamics, Scattering, Texture, Dual Brush, Color Dynamics, Transfer, Brush Pose, Wet Edges, Build-up and Smoothing (including Pulled String), driven by pen pressure, tilt, rotation and direction. Brush presets, Define Brush from Selection, and deterministic, replayable strokes.
    </td>
    <td width="33%" valign="top">
      <h4>🗃️ Layers, done properly</h4>
      Groups, clipping masks, pixel and vector masks, fill layers (solid, gradient and pattern), adjustment layers, live smart objects with smart filters and lossless transforms and warps, multi-layer selection with align, distribute and link, alpha channels and Quick Mask, 27 Photoshop blend modes plus six Paint.NET variants, opacity and fill, locks, colour labels, a layer kind filter, merge, flatten, rasterize, Layer via Copy/Cut, Paste Into.
    </td>
  </tr>
  <tr>
    <td width="33%" valign="top">
      <h4>🎨 Any colour, any depth</h4>
      RGB, Grayscale, CMYK and Lab documents at 8, 16 and 32 bits per channel. Bit depth and colour model are runtime data, so every tool works at every depth.
      <br><br>
      Real ICC colour management in pure Rust: embedded profiles, Assign and Convert to Profile with all four rendering intents and black point compensation, soft proofing (⌘Y) and Gamut Warning (⇧⌘Y) on the GPU.
    </td>
    <td width="33%" valign="top">
      <h4>🗂️ Formats</h4>
      PSD and PSB, layered TIFF (Photoshop's layer data in the TIFF, read and written in either byte order), <a href="docs/pdn.md">Paint.NET PDN3 (read, with editable layers and all 14 blend modes)</a>, <a href="docs/ora.md">OpenRaster (read and write, with layers, groups and blend modes, for Krita, MyPaint and GIMP)</a>, <a href="docs/kra.md">Krita .kra (read, with paint layers, groups, blend modes and transparency masks)</a>, SVG (opens as shape layers, places as a vector Smart Object), plus flat PNG, JPEG, TIFF, WebP (lossy and lossless), GIF, BMP, TGA, ICO, QOI, PNM, OpenEXR, Radiance HDR and FITS (astronomy images: 8/16-bit and 32-bit float, gray or RGB, header kept), and the native <code>.psweet</code> format. Flat formats retain the depths they support: PNG keeps 8/16-bit samples, TIFF keeps 8/16-bit and 32-bit float samples, and OpenEXR keeps half/float samples; JPEG, WebP and the other 8-bit formats reduce higher-depth samples with an export warning. See the <a href="crates/codecs/README.md#capability-matrix-default-build">codec capability matrix</a> for each format. HEIC photos from iPhone and Mac are read-only (included in official builds; optional <code>--features heif</code> for source builds). AVIF is write-only with the optional <code>avif</code> build feature; AVIF decoding and JPEG XL are unavailable. Affinity documents (<code>.af</code>, <code>.afdesign</code>, <code>.afphoto</code>, <code>.afpub</code>) open natively, read only, with artboards, layers, vectors, text, images and masks; effects, adjustments and other unsupported parts are listed in a warning, and Affinity export is unavailable.
    </td>
    <td width="33%" valign="top">
      <h4>🪄 The everyday essentials</h4>
      Auto Tone, Contrast and Color · Equalize · Image and Canvas Size · Crop and Trim · Reveal All · Edit › Fill and Stroke · Copy Merged · Paste in Place · guides, rulers, grid and snapping · Actions record and replay · a command palette (⌘F).
    </td>
  </tr>
</table>

<br>

## PSD without compromise

PhotoSweet's PSD support is a standalone crate written from Adobe's public specification and tested against a corpus of real-world files.

- **Faithful round trips:** opening and re-saving a document renders the same for 307 of the 309 files in the psd-tools test set and 169 of 170 in our mixed ag-psd/psd-tools set (`crates/io/tests/corpus.rs`; fetch the psd-tools set with `cargo xtask corpus --psd-tools`), and anything we don't model yet (raw blocks, descriptors, extras) is carried over instead of being dropped. A re-saved file is not byte-identical to its source: PhotoSweet rewrites image resources, layer records and the composite. Only the standalone `photosweet-psd` crate, parsing and writing a file without the document model, reproduces every parseable corpus file byte for byte (`crates/psd/tests/corpus.rs`).
- **Pixels that match:** a composite oracle compares our render with Photoshop's own merged image, covering gradient interpolation (Classic, Perceptual and Linear), layer effects, shape strokes, clipping and fill opacity.
- **Large documents:** PSB, 16 and 32-bit files, and CMYK and Lab documents open natively.

## Built for agents

Every menu item, tool and dialog runs a command from one registry of 500+ commands. The UI, the CLI, the JSON control channel and the MCP server all call the same commands, so anything you can click, a script or an AI agent can do too.

```sh
# Headless: open, edit, save
photosweet-cli run wave.psd \
  --cmd filter.sharpen.smartSharpen     --params '{"amount":80}' \
  --cmd layer.newAdjustmentLayer.curves --params '{"points":[[0,0],[64,48],[192,212],[255,255]]}' \
  --out wave-final.png

# Apply one action list to a folder of images
photosweet-cli batch --actions grade.json --in ./raw --out ./graded

# Every subcommand explains itself
photosweet-cli batch --help

# Let an agent drive it over MCP (headless, or bridged to the running app)
photosweet-cli mcp
```

The desktop app also offers an authenticated, loopback-only control channel (`photosweet --control`) for inspecting UI state, driving tools with pointer events, and taking offscreen screenshots. Every image in this README was rendered that way. See [`docs/control-protocol.md`](docs/control-protocol.md).

## Under the hood

- **Engine first:** a pure-data document model and a command engine, with a thin egui UI on top. Layering is enforced at build time across 24 crates.
- **Two compositors:** a CPU compositor serves as the reference oracle, and a wgpu compositor puts the canvas on the GPU. They are tested against each other.
- **Copy-on-write tiles:** 256² sparse tiles make undo cheap and huge canvases light, and effect maps are cached per layer state.
- **Runs in the browser:** the whole engine and UI compile to WebAssembly.
- **Clean-room:** implemented from public specs and observed behaviour only. No proprietary code, shaders or assets.
- **Tested:** more than 1,700 tests, including PSD round trips, synthetic generators, compositor oracles and multi-depth checks.

## Get started

```sh
git clone https://github.com/salim-studio/photosweet
cd photosweet
cargo run --release -p photosweet -- image.psd   # the desktop app
cargo test --workspace                           # the test suite
```

Japanese fonts for the UI and Type tool come from [craft-fonts](https://github.com/storytold/craft-fonts), an optional build input (desktop release builds always include it). Without it PhotoSweet uses your system's CJK fonts:

```sh
git clone https://github.com/storytold/craft-fonts ../craft-fonts
CRAFT_FONTS_DIR="$PWD/../craft-fonts" cargo run --release -p photosweet
```

New contributors and AI agents: start with [`AGENTS.md`](AGENTS.md), then [`docs/`](docs/).

### Run it in the browser

The web build is the same engine and UI compiled to WebAssembly. The published build lives at
[**salim-studio.github.io/photosweet**](https://salim-studio.github.io/photosweet/). To build a
self-contained static site yourself (needs `trunk` and the `wasm32-unknown-unknown` target):

```sh
packaging/web/package.sh            # writes dist/release/photosweet-web-<version>.zip
```

Host the unpacked folder on any static server; there is no server-side code. To self-host with
Docker, see [Docker web hosting](packaging/web/README.md#docker).

> [!IMPORTANT]
> **Status:** PhotoSweet is in early alpha, and we want to be straight about where it stands: much of Photoshop's feature surface exists in some form, but **it is not yet a Photoshop replacement for daily professional work**. The biggest gaps are AI/generative features, 15 missing tools, depth in typography and pro workflows, and plug-in compatibility. Every Photoshop menu item is wired to a command ([`docs/parity-checklist.md`](docs/parity-checklist.md)), but that measures wiring, not behaviour. The honest, dimension-by-dimension picture and where we're going next are in the [roadmap](ROADMAP.md) and [parity assessment](docs/target-app-parity.md). Expect rough edges, and please file [issues](https://github.com/salim-studio/photosweet/issues) (include your OS, document size, layer count and a screenshot).

## Downloads

**The quickest way to try PhotoSweet is the [web build](https://salim-studio.github.io/photosweet/)** — it runs in a modern browser with nothing to install.

Native builds for Windows, macOS, Linux and FreeBSD are produced by the release workflow
(`.github/workflows/release.yml`). Tag a release to generate installers and archives; the file
names below are what the packaging scripts emit (`<ver>` is the version number, and
`SHA256SUMS.txt` lists a checksum for every file).

### Windows

| Build | Installer | Portable |
|---|---|---|
| x64 (64-bit Intel/AMD) | `photosweet-<ver>-windows-x64.msi` | `photosweet-<ver>-windows-x64-portable.zip` |
| arm64 (Snapdragon and other ARM PCs) | `photosweet-<ver>-windows-arm64.msi` | `photosweet-<ver>-windows-arm64-portable.zip` |
| x86 (32-bit) | `photosweet-<ver>-windows-x86.msi` | `photosweet-<ver>-windows-x86-portable.zip` |

### macOS

| Build | File | Notes |
|---|---|---|
| App, universal (Apple silicon + Intel) | `photosweet-<ver>-macos-universal.dmg` | Signed and notarized |
| Command-line tool, universal | `photosweet-cli-<ver>-macos-universal.zip` | Signed and notarized |

### Linux

| Format | x86_64 | aarch64 (ARM64) | Notes |
|---|---|---|---|
| AppImage | `photosweet-<ver>-linux-x86_64.AppImage` | `photosweet-<ver>-linux-aarch64.AppImage` | Runs anywhere; updates itself with [AppImageUpdate](https://github.com/AppImageCommunity/AppImageUpdate) (`.zsync` files) |
| Flatpak | `photosweet-<ver>-linux-x86_64.flatpak` | `photosweet-<ver>-linux-aarch64.flatpak` | Sandboxed; `flatpak install --user <file>` |
| Debian/Ubuntu | `photosweet-<ver>-linux-x86_64.deb` | `photosweet-<ver>-linux-aarch64.deb` | |
| Fedora/RHEL/openSUSE | `photosweet-<ver>-linux-x86_64.rpm` | `photosweet-<ver>-linux-aarch64.rpm` | |
| Tarball | `photosweet-<ver>-linux-x86_64.tar.gz` | `photosweet-<ver>-linux-aarch64.tar.gz` | Unpack anywhere |

RISC-V (riscv64): `photosweet-<ver>-linux-riscv64.tar.gz` only, built against Ubuntu 24.04 (needs glibc 2.39+).

On Linux, the AppImage needs no install: the first run registers its launcher icon and menu entry
in `~/.local/share`. Set `PHOTOSWEET_NO_DESKTOP_INTEGRATION=1` to skip that. The Flatpak bundle
needs the freedesktop runtime from [Flathub](https://flathub.org/setup):

```sh
flatpak install --user photosweet-<ver>-linux-x86_64.flatpak   # or -linux-aarch64
flatpak run studio.salim.photosweet
```

### FreeBSD

| Build | File |
|---|---|
| x86_64 | `photosweet-<ver>-freebsd-x86_64.tar.gz` |

### Web (WebAssembly)

| Build | File | Notes |
|---|---|---|
| Static site | `photosweet-web-<ver>.zip` | Runs in a modern browser; host it on any static server |

Maintainers: [`docs/releasing.md`](docs/releasing.md) explains how releases are built, signed and published.

## Documentation

Developer, architecture, automation, format, and security documentation is maintained in the [PhotoSweet documentation book](book/).

## Security

Security architecture, threat modeling, parser hardening, fuzzing, and vulnerability reporting are covered in the [security documentation](book/src/security/) and the repository [security policy](SECURITY.md).

## Test corpora

PhotoSweet is tested against real files: our own Photoshop-authored oracle PSDs in
[photosweet-corpus](https://github.com/salim-studio/photosweet-corpus) plus the psd-tools, ag-psd and PngSuite sets, pinned and
sha256-verified. Fetch them with `cargo xtask corpus --all` and run the tests with
`cargo xtask test-corpus` (details in [docs/development.md](docs/development.md#test-corpora)).

---

## License and credits

PhotoSweet is dual-licensed under [MIT](LICENSE-MIT) or [Apache-2.0](LICENSE-APACHE), at your option.
Copyright (c) 2026 salim-slimani. Required notices are in [NOTICE](NOTICE).

Bundled fonts, icons, images and other assets keep their own open licenses; each one is listed
with its author, source and license in [ATTRIBUTION.md](ATTRIBUTION.md).

Every artwork shown is in the public domain (Wikimedia Commons, NASA, U.S. National Archives); sources are listed in [`docs/images/SOURCES.md`](docs/images/SOURCES.md).

The PhotoSweet name, mark and wordmark live in [`docs/brand/`](docs/brand/) and are covered by the
same license as the source code ([`docs/brand/LICENSE-brand.txt`](docs/brand/LICENSE-brand.txt)).

<sub>Adobe, Photoshop, Illustrator, Premiere Pro, Lightroom, Acrobat, After Effects and InDesign are trademarks or registered trademarks of Adobe Inc. in the United States and/or other countries. PhotoSweet is an independent, open-source project and is not affiliated with, sponsored by or endorsed by Adobe Inc.; these names are used only to describe the workflows it is compatible with.</sub>

<p align="center">
  <a href="https://salim-studio.github.io/photosweet/"><img alt="PhotoSweet" src="docs/brand/photosweet-mark.svg" width="28"></a><br>
  <sub>Made by <a href="https://github.com/salim-slimani">salim-slimani</a>.</sub>
</p>

<p align="center">
  <a href="https://salim-studio.github.io/photosweet/"><img alt="PhotoSweet" src="docs/brand/photosweet-logo.svg" width="150"></a>
</p>
