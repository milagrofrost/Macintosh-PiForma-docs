# Printed Parts

The `stl/` directory contains the normalized printable and editable model files used in the finished Macintosh PiForma build. These are custom mechanical parts for the Apple IIc Monitor enclosure, internal electronics, controls, display, and external stand.

Most hidden internal parts were printed from whatever filament was available. The current internal rack was printed in brown PETG. Dark colors work well inside the case because they disappear visually. PETG or another heat-tolerant material is strongly preferred for parts near the Raspberry Pi.

For file-specific warnings, original-to-normalized filename mapping, and SHA-256 hashes, see:

- [`../stl/README.md`](../stl/README.md)
- [`../stl/file-manifest.tsv`](../stl/file-manifest.tsv)

## Important 3MF warning

The `.3mf` files were created or saved with **Microsoft 3D Builder**. They are not Bambu Studio project files. Bambu Studio and other slicers may interpret their assemblies, transforms, or reference objects incorrectly.

Use this order of preference:

1. Print the supplied STL when one exists.
2. When only a 3MF exists, open it in Microsoft 3D Builder and export the printable geometry to STL.
3. Read the part notes before assuming a related 3MF and STL contain the same geometry.

The actual models printed successfully through the Bambu workflow used for this project. Some files may be described by mesh-analysis tools as multi-shell or non-watertight. Do not automatically repair or simplify them without confirming that the result still matches the installed part.

## Repository layout

```text
stl/
├── README.md
├── file-manifest.tsv
├── battery-plunger/
│   └── anker-battery-button-plunger.3mf
├── bezel/
│   ├── lcd-bezel-braces-three-piece.3mf
│   ├── lcd-curved-bezel-final.stl
│   └── lcd-curved-bezel-generator.scad
├── boot-chime-switch/
│   ├── boot-chime-board-speaker-case.3mf
│   ├── boot-chime-board-speaker-case.stl
│   ├── boot-chime-selector-dial-reference-mockup.3mf
│   └── boot-chime-selector-dial.stl
├── monitor-stand/
│   ├── folding-monitor-stand.3mf
│   └── folding-monitor-stand.stl
├── power-rail/
│   ├── 5v-rail-enclosure.3mf
│   └── 5v-rail-enclosure.stl
├── power-switch/
│   ├── narrow-original-power-switch.3mf
│   └── narrow-original-power-switch.stl
├── screen-feet/
│   └── screen-retaining-feet-four-piece.stl
├── shelf/
│   ├── internal-three-level-rack.3mf
│   ├── internal-three-level-rack.stl
│   ├── rpi-elevator.3mf
│   ├── rpi-elevator.stl
│   ├── rpi-shelf-spacer.3mf
│   └── rpi-shelf-spacer.stl
├── status-led/
│   ├── apple-crt-status-led-cover.3mf
│   └── apple-crt-status-led-cover.stl
└── usb-panel-mount/
    ├── usb-panel-mount.3mf
    └── usb-panel-mount.stl
```

## Printed parts inventory

| Part | Repository location | Purpose | Installed? | Important notes |
|---|---|---|---|---|
| Three-level internal rack | `stl/shelf/internal-three-level-rack.*` | Holds the Raspberry Pi, 5V rail, LCD controller, internal power adapter, and USB speaker | yes | Current part was printed in brown PETG |
| Raspberry Pi elevator | `stl/shelf/rpi-elevator.*` | Raises the Pi above the upper shelf to provide airflow and reduce heat transfer | yes | Part of the current thermal mitigation; PETG recommended |
| Raspberry Pi shelf spacer | `stl/shelf/rpi-shelf-spacer.*` | Small optional spacer used with the zip-tied shelf arrangement to limit lift and movement | yes | Not essential to basic operation |
| Curved LCD bezel | `stl/bezel/lcd-curved-bezel-final.stl` | Mates the flat LCD to the original curved CRT opening | yes | Known-good final print |
| Bezel generator | `stl/bezel/lcd-curved-bezel-generator.scad` | Parametric OpenSCAD source for changing curvature, thickness, and opening | source | Historical variable names are mixed up; read comments before editing |
| LCD bezel braces | `stl/bezel/lcd-bezel-braces-three-piece.3mf` | Three braces span the back of the LCD and screw into the bezel | yes | 3MF only; export to STL in 3D Builder; use short, shallow screws |
| Screen-retaining feet | `stl/screen-feet/screen-retaining-feet-four-piece.stl` | Original case screws and metal frame press the feet against the bezel to retain it | yes | STL already contains all four feet; rejected experimental 3MF omitted |
| 5V rail enclosure | `stl/power-rail/5v-rail-enclosure.*` | Protects and mounts the handmade JST power rail | yes | Keeps the soldered underside isolated while leaving connectors accessible |
| Anker battery-button plunger | `stl/battery-plunger/anker-battery-button-plunger.3mf` | Spring/plunger mechanism presses the physical Anker button through an existing rear hole | yes | Final newer geometry is kept as one assembly; older mismatched STL omitted |
| Narrow original power-switch actuator | `stl/power-switch/narrow-original-power-switch.*` | Replaces the original actuator with a narrower version that does not bind | yes | Needed because the rebuilt internal assembly shifted the original alignment |
| Boot-chime board and speaker case | `stl/boot-chime-switch/boot-chime-board-speaker-case.*` | Holds the soundboard and salvaged laptop speaker as one module | yes | Mounted inside the metal case with double-sided adhesive |
| Boot-chime selector dial | `stl/boot-chime-switch/boot-chime-selector-dial.stl` | Interfaces with the multi-position selector used to choose startup sounds | yes | STL is the actual printable part |
| Selector reference mock-up | `stl/boot-chime-switch/boot-chime-selector-dial-reference-mockup.3mf` | Shows the selector part with surrounding reference geometry | reference | Not the preferred print file; print the STL instead |
| Green status-LED cover | `stl/status-led/apple-crt-status-led-cover.*` | Surrounds the replacement green LED behind the original acrylic indicator area | yes | Prevents light from bleeding through the interior |
| USB panel mount | `stl/usb-panel-mount/usb-panel-mount.*` | Minimal threaded mount for a solder-tab female USB receptacle | yes | Installed in an original control opening that was drilled slightly larger |
| Folding monitor stand | `stl/monitor-stand/folding-monitor-stand.*` | Angles the monitor upward and folds flat for transport | yes | Approximate working angle is 15–20 degrees |
| Apple-style wireless mouse | third-party links below | Matching wireless mouse using the Bambu electronics kit | yes | Third-party shell is linked, not redistributed here |

## Shelf arrangement

The rack is a three-level structure. It does not hold the Anker battery.

Approximate placement:

```text
Top shelf:
  Raspberry Pi 4B on the Pi elevator
  custom 5V JST rail

Middle shelf:
  internal USB power adapter
  LCD controller board

Bottom shelf:
  USB speaker

Rear metal floor:
  Anker battery, friction fit
```

The small Pi shelf spacer is optional. It was added to keep the Pi and zip-tied shelf arrangement from moving farther than intended.

## Display bezel, braces, and retaining feet

The display assembly uses the original case geometry, metal chassis, screws, and several printed parts together:

- curved bezel visually frames and aligns the LCD
- three braces span the rear of the LCD and fasten into the bezel
- four retaining feet press the bezel into position when the original metal frame is screwed down
- small hot-glue dabs may be used to prevent movement during assembly

The screen-feet STL already contains all four feet. Print the file once.

Use short, shallow screws for the three bezel braces so the screws do not penetrate farther than intended. The existing holes are best treated as pilot holes. If thicker screws are used, enlarge the holes carefully in the printed parts rather than forcing the screws and splitting the plastic.

## Bezel OpenSCAD source warning

The final STL is the known-good installed bezel. The OpenSCAD source is included so the curvature and thickness can be adapted, but its historical axis naming is confusing:

- `gap_long_*` controls curvature across the 147 mm X/width axis
- `gap_short_*` controls curvature across the 197 mm Y/height axis

The names therefore do not correspond cleanly to the physical long and short dimensions. Width and height assumptions elsewhere in the file may also feel reversed. Do not casually rename or swap the variables. Compare every changed render against the known-good final STL and expect some trial and error.

## Battery-button plunger

The Anker battery is buried tightly in the rear of the enclosure. This part uses a mechanical plunger and spring to provide access to the battery's physical button through one of the original control holes.

Only the newer 3MF assembly is included. The older STL did not match the final geometry and was intentionally excluded. Open the 3MF in Microsoft 3D Builder and export the printable assembly to STL before bringing it into a slicer.

## Boot-chime selector and soundboard case

The boot-chime system uses a multi-position selector and a small soundboard connected to a salvaged laptop speaker.

Two selector files are intentionally different:

- `boot-chime-selector-dial.stl` is the actual printable part
- `boot-chime-selector-dial-reference-mockup.3mf` contains surrounding mock-up geometry for design context

The reference 3MF should not be mistaken for the preferred print file.

## Thermal and electrical warning

The Raspberry Pi previously sat directly on the upper printed shelf. Heat softened and warped the shelf, which then pressed against and flexed the LCD controller board below it. That caused graphical glitches, color loss, instability, and apparent ribbon-cable problems.

Current mitigation includes:

- Pi elevator creating an air gap
- shelf supported with a zip tie
- reflective aluminum foil below and above the Pi
- display controller checked for mechanical pressure

Aluminum foil is conductive. It must remain electrically isolated from the Raspberry Pi, GPIO pins, USB shields, solder joints, LCD controller, power rail, and all exposed electronics. A properly secured nonconductive thermal barrier is preferable in a future revision.

Use PETG or another heat-tolerant material for the rack and Pi elevator when possible. A future rack revision should add a center support column or reinforcing rib.

## Mouse shell

The matching mouse is documented in [Hardware](hardware.md#mouse). The project does not redistribute the third-party shell files.

- [Retro Wireless Computer Mouse](https://www.printables.com/model/1339297-retro-wireless-computer-mouse)
- [Custom scroll wheel and axle](https://www.printables.com/model/1774131-scroll-wheel-and-axle-for-retro-wireless-computer)

The mouse uses the Bambu wireless mouse kit electronics and was printed in Retro Platinum PLA.

## General print settings

These are starting points, not strict requirements:

| Setting | Recommendation |
|---|---|
| Material | PETG for the rack and Pi elevator; PLA or PETG for most other hidden parts |
| Layer height | approximately 0.20 mm |
| Walls | 3 |
| Infill | approximately 15–25 percent |
| Supports | choose based on slicer preview and printer capability |
| Orientation | begin with the supplied model orientation |
| Quantity | one file unless noted; the feet STL already contains four feet |
| Color | darker colors for hidden internals; retro/off-white for visible parts |

Test-fit every mechanical part before final assembly. The models reflect one heavily modified Apple IIc Monitor shell and may need adjustment for another enclosure.
