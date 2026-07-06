# Printed Parts

This folder is for the printable files that make Macintosh PiForma more than a Raspberry Pi tossed in a vintage shell.

Most internal parts were printed from whatever filament was available. The final visible mouse uses Retro Platinum PLA. The internal chassis/shelf ended up in brown PETG. For internal parts, darker colors are preferred mostly because they disappear inside the case.

## Suggested STL folder layout

```text
stl/
├── shelf/
├── bezel/
├── screen-feet/
├── power-rail/
├── battery-plunger/
├── boot-chime-switch/
└── monitor-stand/
```

## Printed parts table

| Part | Folder | Purpose | Installed? | Material notes |
|---|---|---|---|---|
| Three-level internal shelf | `stl/shelf/` | holds Pi, charger, LCD controller, USB speaker, power rail | yes | current part printed in brown PETG |
| Display bezel | `stl/bezel/` | aligns LCD in Apple IIc Monitor front opening | yes | PLA |
| Screen feet | `stl/screen-feet/` | lock screen position when metal chassis is screwed in | yes | PLA |
| Horizontal screen braces | `stl/screen-feet/` or `stl/bezel/` | hold LCD alignment against bezel | yes | PLA |
| 5V rail enclosure | `stl/power-rail/` | protects perfboard rail and exposes JST ports | yes | PLA/PETG |
| Battery plunger | `stl/battery-plunger/` | presses Anker battery button from rear of case | yes | PLA/PETG |
| YS-M3 boot chime mount | `stl/boot-chime-switch/` | holds MP3 board and salvaged speaker | yes | PLA/PETG |
| Boot chime selector mount | `stl/boot-chime-switch/` | mounts CK1028 selector in rear control hole | yes | PLA/PETG |
| Monitor stand | `stl/monitor-stand/` | external stand for using the monitor | yes | PLA |
| Apple-style mouse shell | external link | matching 3D printed wireless mouse | yes | Retro Platinum PLA |

## Shelf notes

The shelf is a three-level structure.

It does not hold the Anker battery.

It does hold:

- Raspberry Pi 4B
- custom 5V JST rail
- LCD controller
- internal USB power adapter
- USB speaker

Approximate placement:

```text
Top shelf:
  Raspberry Pi 4B
  custom 5V JST rail

Middle shelf:
  100W USB power adapter
  LCD controller board

Bottom shelf:
  USB speaker

Rear metal floor:
  Anker battery, friction fit
```

## Display bezel and screen feet

The LCD does not simply screw into the original case like Apple intended, because Apple did not intend this. Rude of them.

The printed display system uses:

- bezel to visually frame and align the LCD
- horizontal braces to hold LCD alignment against the bezel
- feet that become effective when the metal chassis and front shell are screwed together
- small hot glue dabs to prevent shifting during assembly

The metal chassis and original screws still matter. The printed parts and original case geometry work together.

## Power rail enclosure

The custom 5V rail is handmade, so the enclosure matters. It keeps the underside of the rail from touching things it should not touch while exposing the JST connectors for service.

The rail itself is:

- perfboard
- JST connectors
- solid-core wire bus bars
- solder

The printed enclosure turns that into an actual module instead of a cursed little strip of soldered optimism.

## Battery plunger

The Anker battery is buried tightly in the rear of the case. The plunger gives external access to the battery button.

Functions:

- wake/display battery status
- interact with Anker button without opening the case
- preserve the clean outside of the monitor

## Boot chime selector and YS-M3 mount

The boot chime selector uses a Mouser CK1028 selector switch and a YS-M3 MP3 module.

Printed parts here may include:

- rear switch mount
- YS-M3 board holder
- salvaged laptop speaker holder
- cable relief or spacer parts

## Mouse shell

The Apple-style wireless mouse shell is printed and in use, but the original model link still needs to be added.

Placeholder:

```text
references/apple-style-wireless-mouse-link.txt
```

## Print settings

Known good starting point:

| Setting | Recommendation |
|---|---|
| Material | PLA for most visible/non-heat parts, PETG okay for internal chassis |
| Layer height | 0.20mm |
| Walls | 3 |
| Infill | 15-25 percent |
| Supports | depends on part |
| Color | darker colors for hidden internals, retro/off-white for visible parts |

Add exact orientation/support notes after the final STLs are uploaded.
