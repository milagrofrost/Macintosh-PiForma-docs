# Project Overview

**Macintosh PiForma** is a Raspberry Pi-powered Macintosh Performa fever dream built inside an Apple IIc Monitor.

It is not a restoration. It is not trying to be a museum piece. It is a working, portable, weirdly sincere Apple-flavored machine that lives somewhere between a Macintosh Performa, a Raspberry Pi desktop, a retro game station, and a piece of early-2000s Mac mod forum nostalgia.

## The short version

This is a 1985 Apple IIc Monitor shell turned into a portable Raspberry Pi Macintosh-ish computer.

It has:

- a Raspberry Pi 4B running an 800x480 Mac OS 9-ish desktop
- the original monitor power switch repurposed as the system power switch
- an internal Anker Prime 26K battery
- an internal USB-C charger wired to the original rear AC inlet
- a handmade 5V JST power rail
- HDMI and RCA composite video support through the LCD controller
- a boot chime selector with multiple startup sounds
- a front Apple logo that works as a capacitive gesture button
- a Bluetooth-converted Apple ADB keyboard
- a 3D printed Apple-style wireless mouse
- a custom At Ease-style launcher
- a Control Strip-style dock
- an About This PiForma app
- a retro Clippy assistant
- a velvet-lined travel bag with hidden wireless trickle charging

## The software family

Macintosh PiForma now includes a small family of companion apps.

| Project | Repo | What it does |
|---|---|---|
| AtEase Simulator | https://github.com/milagrofrost/AtEase-simulator | At Ease-style launcher shell |
| ControlStrip Simulator | https://github.com/milagrofrost/ControlStrip-Simulator | Mac OS-style utility strip / dock |
| About This PiForma | https://github.com/milagrofrost/about-this-pi | About This Mac-style system info window |
| Clippy | https://github.com/milagrofrost/clippy | retro desktop assistant |
| Macintosh PiForma docs | https://github.com/milagrofrost/Macintosh-PiForma-docs | the build, BOM, wiring, lore, and maintenance notes |

## Why this works

The hardware gives the machine a body. The software gives it a personality.

The power switch, boot chime, Apple logo gestures, AtEase launcher, Control Strip, and matching keyboard all work together. Any one of those pieces alone would be cute. Together, they make the build feel like a complete little computer from a timeline that never existed.

## The important trick

The front Apple logo is a real input device.

| Gesture | Action |
|---|---|
| 1 tap | Open Internet Explorer / Netscape-style launcher |
| 2 taps | Open Mac OS 9 / SheepShaver |
| 3 taps | Open Winamp / QMMP |
| 4 taps | Open RetroPie / EmulationStation |
| Hold | Close the active game or window |

The four-tap RetroPie gesture is not just cute. It means the keyboard and mouse can stay in the bag when the only goal is playing games.

## What to read next

- [Hardware](hardware.md)
- [Software](software.md)
- [Software Ecosystem](software-ecosystem.md)
- [Live System Audit Summary](live-system-audit.md)
- [Wiring](wiring.md)
- [Bill of Materials](bom.md)
- [Printed Parts](printed-parts.md)
- [Build Log](build-log.md)
- [Related Projects](related-projects.md)
- [Cleanup and Archival Plan](cleanup-plan.md)
- [Media Plan](media-plan.md)
- [Maintenance](maintenance.md)
- [Known Issues](known-issues.md)
- [Safety](safety.md)
