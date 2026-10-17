# PhotoSweet app icon

A **six-blade aperture** with a sparkle: the opening of a lens, opening onto a violet-to-rose
gradient field. A clean, geometric mark, legible from 16 px to 1024 px.

## Palette

| Colour | Hex | Used for |
|---|---|---|
| Violet | `#8B5CF6` | gradient start (top-left) |
| Rose | `#F43F5E` | gradient end (bottom-right) |
| White | `#FFFFFF` | aperture blades and sparkle |

## Geometry

A 512-unit tile (`viewBox="0 0 512 512"`), rounded square with `rx=112`. The aperture is centred
at (256, 256): a 168-unit outer radius and a 92-unit hexagonal opening, cut into six blades with a
1.7° gap between them. A four-point sparkle sits at (392, 122). The macOS renders pad the tile
onto Apple's 824/1024 icon grid; the Windows and Linux renders crop 22 units off each side so the
mark reads at 16–48 px.

## Provenance

Original artwork made for this project. No third-party material. License: see `LICENSE.txt`.

## Files

- `photosweet.svg`: canonical master (also the hicolor scalable icon).
- `photosweet-small.svg`: lighter variant for the scalable theme.
- `photosweet-1024.png`: 1024 px render on the macOS grid.
- `photosweet.icns`: macOS bundle icon (`CFBundleIconFile`).
- `photosweet.ico`: Windows icon, 16–256 px, embedded in the `.exe` by `apps/photosweet/build.rs`.
- `hicolor/<size>/apps/studio.salim.photosweet.png` (16–512) and `hicolor/scalable/...svg`:
  Linux icon theme.

The app also sets the window icon and Wayland app ID at runtime (`apps/photosweet/src/app_icon.rs`,
`main.rs`). On Windows the taskbar shows the icon of the Start Menu shortcut that launches the
exe, so the MSI's `<Icon Id>` keeps the `.exe` extension (ICE50); `app_icon.rs` documents the
details and tests the `.ico` sizes and the WiX icon references.

## Regenerate

Run `python3 packaging/gen_icons.py` to write the SVG masters and every raster/`.ico`/`.icns`
render from the geometry in that script. `packaging/icons.sh` is the alternative path when `resvg`
(and `iconutil` on macOS) are available.
