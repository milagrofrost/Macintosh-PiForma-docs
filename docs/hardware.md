# Hardware

This document describes the physical Macintosh PiForma build from the final working state.

## Donor shell

- Donor: Apple IIc Monitor
- Model: A2M4090
- Manufacture date: February 1985
- Original CRT: removed years ago
- Final use: Raspberry Pi-powered Macintosh-inspired portable computer

This is not a restoration. The CRT was discolored, flickering, and not worth saving for this project. The case, original power switch, original AC inlet, rear openings, metal chassis, and monitor shape were reused because the shell still had life in it.

## Internal layout

The build has four main physical zones:

1. Front display area
2. Three-level printed shelf
3. Rear battery area
4. Rear controls and ports

The shelf does not hold the Anker battery. The Anker battery sits separately toward the rear of the monitor on the metal chassis floor. It is installed lengthwise and held by friction between the sides of the case.

## Three-level shelf

The custom 3D printed shelf is the main internal component carrier.

### Top shelf

- Raspberry Pi 4B, 4GB RAM
- Custom 5V JST power rail
- Power rail enclosure
- Related wiring

The Raspberry Pi is mounted with zip ties.

### Middle shelf

- Internal 100W USB power adapter
- LCD controller board

The LCD controller slides into printed notches like a tray, which makes it serviceable instead of permanently buried.

### Bottom shelf

- Internal USB speaker

The USB speaker is connected directly to the Raspberry Pi and handles normal system audio.

## Rear battery area

The Anker Prime 26K 300W battery sits lengthwise across the rear metal chassis floor. It is a very tight fit and is held by friction rather than a printed mount.

A custom 3D printed plunger reaches the Anker's physical button. From the outside rear of the case, pressing the plunger lets the user wake the battery display or interact with the battery without opening the case.

## Display system

The final installed display is the 9-inch HDMI/VGA/AV LCD kit purchased on May 16, 2026. The current working mode is:

- Resolution: 800x480
- Inputs used: HDMI and RCA composite
- VGA: available on the controller but unused

Earlier experiments included 1024x600-class 9-inch panels, PCB800099-style boards, and multiple HDMI ribbon cable orientations. Those are part of the build history, but the final working display is the May 16 display kit running at 800x480.

## LCD mounting

The LCD is mounted with:

- 3D printed bezel
- 3D printed screen feet
- 3D printed horizontal braces
- small hot glue dabs for alignment during assembly
- original chassis screws that pull the metal chassis and front case together

The screen rests into the printed bezel. The bezel aligns it. The horizontal braces help keep it registered. The feet really do their job once the metal chassis is screwed into the front shell.

## Display ribbon

The current LCD ribbon is about 150mm. It is longer than needed, but it works.

Known behavior:

- the connection is sensitive
- the ribbon is taped down to reduce movement
- shorter 80mm or 50mm cable may be a future improvement
- once it works, do not mess with it just because you are bored

## Video paths

### Raspberry Pi video

The Raspberry Pi connects to the LCD controller over HDMI using angled and ribbon-style adapters. A normal HDMI connector would protrude too far and contact the back of the LCD, causing distortion.

### Composite video

A rear RCA panel jack replaces one of the original brightness/contrast control openings. It connects to the composite input on the LCD controller.

### Source select

The LCD controller's button daughterboard is mounted inside the case. The IR receiver is unused. The source button was soldered to wires and routed to a rear physical switch.

The source switch cycles:

```text
HDMI -> RCA -> VGA -> RCA2 -> repeat
```

Only HDMI and RCA are normally useful.

## Power system

The Anker battery is the heart of the power system.

Final power path:

```text
Original AC inlet
  -> internal 100W USB power adapter
  -> Anker Prime 26K 300W battery
  -> original Apple monitor power switch
  -> custom 5V JST power rail
  -> Raspberry Pi, LCD controller, boot chime module, touch sensor
```

The original monitor power switch interrupts battery output to the 5V rail. It does not interrupt AC input to the internal charger. That means the battery can still charge while the monitor is off.

The final internal charger is the 100W USB power adapter from eBay. A different Amazon power adapter caused noise and EMI weirdness, including false triggers from sensors and relay instability, so it was not used.

## Custom 5V JST rail

The rail is handmade from:

- through-hole perfboard
- about six small 2-pin JST outputs
- stripped solid-core wire used as bus bars
- soldered underside connections
- 3D printed enclosure

Connected loads include:

- Raspberry Pi 4B
- LCD controller
- YS-M3 boot chime module
- TTP223 Apple logo touch sensor

The USB speaker is powered through the Raspberry Pi USB port, not from the JST rail.

There are no relays in the final build and no fuses on the custom rail. The build relies on the Anker and connected devices for protection.

## Boot chime system

Parts:

- YS-M3 MP3 sound module
- Mouser CK1028 selector switch
- salvaged laptop speaker
- custom 3D printed sound module and speaker housing
- rear-mounted boot chime selector

Behavior:

- YS-M3 is powered from the 5V rail
- it plays a selected sound a couple seconds after power is applied
- CK1028 selects between about 9 or 10 boot chimes
- audio plays through its own salvaged laptop speaker

The selector is mounted in one of the rear holes where the original brightness/contrast controls used to be.

## Main audio

Normal Raspberry Pi audio uses the internal USB speaker mounted on the bottom shelf.

An external USB-to-3.5mm/RCA audio adapter can be used if RCA audio is needed, but it is not built into the monitor. The rear RCA jack is composite video only.

MAX98357A amplifier boards were purchased and tested but are not part of the final installed audio path.

## Apple logo gesture input

The front Apple logo has a TTP223 capacitive touch sensor behind it.

- Sensor: TTP223
- GPIO: 23
- Function: multi-tap and hold gesture input

Gesture map:

| Gesture | Action |
|---|---|
| 1 tap | Open Internet Explorer themed launcher |
| 2 taps | Open Mac OS 9 / SheepShaver |
| 3 taps | Open Winamp/QMMP style player |
| 4 taps | Open RetroPie / EmulationStation |
| Hold | Close the active window |

The four-tap RetroPie gesture is the practical one. Power on, plug in a controller, tap the Apple logo four times, and start playing without pulling out the keyboard and mouse.

The hold gesture also solves the N64 controller hotkey problem. Instead of sacrificing a controller button, holding the Apple logo closes the active game or EmulationStation.

## Volume knob

The original monitor volume area is repurposed with an EC11 rotary encoder.

| Function | GPIO |
|---|---:|
| Encoder A | GPIO 17 |
| Encoder B | GPIO 27 |
| Encoder push | GPIO 22 |

Rotation adjusts system volume. Push-to-mute exists in software but is not physically usable in the final installation.

## Keyboard

Keyboard: Apple ADB Keyboard A9M0330

The keyboard is converted to Bluetooth using Matt Chesters' ZMK ADB keyboard project:

https://github.com/mattchesters/zmk-apple-desktop-bus-keyboard

This keyboard conversion is part of the Macintosh PiForma setup, but it is not an original design from this project.

Installed keyboard components:

- Seeed XIAO nRF52840
- custom PCB
- nice!view display
- MCP23017 I/O expander
- USB-C charging
- JST battery connector
- 110mAh LiPo battery
- ZMK firmware

The keyboard currently works over Bluetooth and charges over USB-C.

## Mouse

The matching mouse uses:

- Bambu wireless mouse kit electronics
- 3D printed Apple-style mouse shell
- USB receiver plugged into the Raspberry Pi
- Retro Platinum PLA for the printed shell

The original mouse shell model link still needs to be added.

## Bag system

The travel bag is part of the project.

Bag features:

- LOVFEIFAN / LOVFEI FAN style 55x30x20 cm bag
- corrugated plastic liner
- foam bottom
- green velvet covering
- spray adhesive
- hidden wireless charging transmitter
- alignment grooves for the monitor bottom

The bag stores the computer, ADB Bluetooth keyboard, mouse, controllers, USB hub, stand, cables, and power accessories.

The wireless charging pad is hidden under the velvet. A USB cable runs through the bag into a back pocket, where it can be pulled out to power the wireless charger. This is a trickle-charge setup for charging Macintosh PiForma while it is stored in the bag.
