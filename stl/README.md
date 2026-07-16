# Macintosh PiForma Printable Files

These are the normalized printable and editable model files used in the finished Macintosh PiForma build.

## File-format warning

The `.3mf` files in this archive were created or saved with **Microsoft 3D Builder**. They are not Bambu Studio project files and are not guaranteed to import correctly into Bambu Studio or another slicer. Assemblies, transforms, or mock-up geometry may be interpreted differently.

For normal printing:

1. Prefer the supplied `.stl` when one exists.
2. When only a `.3mf` exists, open it in Microsoft 3D Builder and export or save the printable geometry as STL before slicing.
3. Do not assume a 3MF and STL with related names contain identical geometry. The exceptions are documented below.

Bambu Studio successfully handled the printable models used for the actual build, including models that other mesh-analysis tools may describe as multi-shell or non-watertight. Do not automatically repair or simplify a model without checking that the resulting geometry still matches the installed part.

## General print guidance

- The supplied orientation is the intended starting orientation in most cases.
- Support requirements depend on printer, material, and slicer settings.
- Unless noted otherwise, print one copy of the supplied file.
- `screen-retaining-feet-four-piece.stl` already contains all four feet.
- Test-fit before final assembly. Several parts depend on the exact geometry of this modified Apple IIc Monitor shell.
- Pilot holes may need to be carefully enlarged with a drill when using thicker screws.

## File inventory

| Folder | File | Status and purpose |
|---|---|---|
| `power-rail/` | `5v-rail-enclosure.3mf`, `.stl` | Enclosure for the handmade 5V JST distribution rail mounted to the shelf. |
| `status-led/` | `apple-crt-status-led-cover.3mf`, `.stl` | Light shield around the replacement green status LED behind the original acrylic indicator area. Prevents light leakage inside the case. |
| `battery-plunger/` | `anker-battery-button-plunger.3mf` | Current spring/plunger assembly used to press the Anker battery button through an existing rear control hole. This newer geometry is kept as one assembly. The older STL was intentionally omitted because it does not match the final design. Export an STL through Microsoft 3D Builder before slicing. |
| `bezel/` | `lcd-curved-bezel-final.stl` | Known-good final curved bezel joining the flat LCD to the original curved CRT opening. |
| `bezel/` | `lcd-curved-bezel-generator.scad` | Editable OpenSCAD generator. Parameter naming is historically mixed up; read the warning in the source before changing values. |
| `bezel/` | `lcd-bezel-braces-three-piece.3mf` | Contains three shallow braces spanning the rear of the LCD and fastening into the bezel. Export through Microsoft 3D Builder before slicing. Use short, shallow screws; enlarge pilot holes only as needed. |
| `monitor-stand/` | `folding-monitor-stand.3mf`, `.stl` | Folding external monitor stand. Raises the viewing angle approximately 15–20 degrees and folds flat for transport. |
| `screen-feet/` | `screen-retaining-feet-four-piece.stl` | Four feet already arranged in one STL. The original case screws and metal frame press these against the bezel to retain it. The rejected experimental 3MF was intentionally omitted. |
| `power-switch/` | `narrow-original-power-switch.3mf`, `.stl` | Narrower replacement actuator for the original power-switch opening. Prevents binding caused by the shifted internal assembly. |
| `shelf/` | `internal-three-level-rack.3mf`, `.stl` | Internal rack for the Raspberry Pi, power rail, LCD controller, power adapter, and USB speaker. |
| `shelf/` | `rpi-elevator.3mf`, `.stl` | Raises the Raspberry Pi above the upper shelf to create an airflow gap and reduce heat transfer into the shelf. |
| `shelf/` | `rpi-shelf-spacer.3mf`, `.stl` | Small optional spacer used with the zip-tied shelf arrangement to limit movement and help keep the Pi positioned. |
| `boot-chime-switch/` | `boot-chime-board-speaker-case.3mf`, `.stl` | Case for the boot-chime soundboard and salvaged laptop speaker, attached inside the metal enclosure with double-sided adhesive. |
| `boot-chime-switch/` | `boot-chime-selector-dial.stl` | Actual printable selector-dial part for the multi-position startup-sound selector. |
| `boot-chime-switch/` | `boot-chime-selector-dial-reference-mockup.3mf` | 3D Builder mock-up containing surrounding reference geometry. It is included for design context, not as the preferred print file. Print the STL instead. |
| `usb-panel-mount/` | `usb-panel-mount.3mf`, `.stl` | Compact threaded panel mount for a solder-tab female USB receptacle installed in an enlarged original control hole. |

## Thermal and electrical safety

The Pi elevator and rack are part of the current thermal mitigation. The Raspberry Pi previously heated and warped the upper shelf, which then flexed the LCD controller board and caused display glitches and color loss.

Current mitigation includes an air gap, a zip tie supporting the shelf, and aluminum foil used as a reflective layer above and below the Pi. Aluminum foil is conductive. It must remain electrically isolated from the Pi, GPIO pins, USB shields, solder joints, display-controller board, power rail, and all exposed electronics. A nonconductive thermal barrier is preferred for a future revision.

Use PETG or another heat-tolerant material for the rack and Pi elevator when possible. A future rack revision should add a center support column or rib.

## Third-party mouse model

The Apple-style wireless mouse is not redistributed here. The build uses the third-party [Retro Wireless Computer Mouse](https://www.printables.com/model/1339297-retro-wireless-computer-mouse) shell plus the project-specific [Custom scroll wheel and axle](https://www.printables.com/model/1774131-scroll-wheel-and-axle-for-retro-wireless-computer) documented in `docs/hardware.md`.
