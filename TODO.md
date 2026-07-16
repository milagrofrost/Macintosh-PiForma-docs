# Documentation Completion Checklist

Macintosh PiForma is a finished project. This checklist tracks the remaining work needed to make the repository archival-grade and independently rebuildable. It is not a package-cleanup or hardware-redesign list.

## Completed foundation

- [x] Archive the final STL, 3MF, and OpenSCAD files under `stl/`
- [x] Add the printed-parts manifest, hashes, and file-format warnings
- [x] Archive the live PiForma Python and shell scripts under `scripts/`
- [x] Archive the live system and user systemd units under `systemd/`
- [x] Archive the verified desktop and application configuration under `config/`
- [x] Document the APT/dpkg package state and curated rebuild profiles under `packages/`
- [x] Document the Raspberry Pi 4B, 256GB microSD, Debian 13.5/Trixie, and X11 system baseline
- [x] Link the third-party mouse shell and project-specific scroll-wheel design
- [x] Document the companion application repositories and their integration
- [x] Add hardware, maintenance, known-issues, and safety documentation

## Priority 1: recovery blockers

These are the remaining items most likely to prevent a clean recovery from the repository.

- [ ] Identify and record the exact Raspberry Pi OS image filename, release date, architecture, and checksum used as the tested rebuild starting point
- [ ] Perform a complete fresh-microSD rebuild using only the repository and record every undocumented intervention
- [ ] Archive trusted copies of the five local PiForma `.deb` packages, or add repeatable build/release instructions that recreate them from documented commits
- [ ] Rebuild and independently verify the About This PiForma `.deb`; the currently discovered package does not match the live installation
- [ ] Archive `/boot/firmware/cmdline.txt`
- [ ] Archive the active LightDM autologin configuration and document the required `frost` UID/session assumptions
- [ ] Archive `~/.config/gtk-3.0/settings.ini` and any other active GTK appearance settings
- [ ] Archive `~/.config/autostart/clippy.desktop`
- [ ] Archive `/etc/xdg/autostart/env-display.desktop`
- [ ] Archive or document the narrow sudoers rule used by the Apple-logo ten-second shutdown gesture
- [ ] Archive the four exact `~/Desktop` launchers used by `apple_gesture_button.py`: `Chromium-70.desktop`, `MacOS9.desktop`, `Winamp.desktop`, and `Retropie.desktop`
- [ ] Archive the active GTK theme, icon theme, cursor theme, Chicago/Charcoal fonts, wallpaper, Apple logo image, launcher icons, and favicons needed to reproduce the desktop appearance
- [ ] Archive the Weather Channel `launch.html` and `satellite.png` files alongside the existing launcher script
- [ ] Preserve the deployed Flying Toasters build or document a tested process that recreates it from the companion repository
- [ ] Archive the selected Plymouth theme, RetroPie/asplashscreen configuration, and required boot-splash assets
- [ ] Archive the RetroPie and EmulationStation configuration, controller mappings, and any PiForma-specific launch/exit behavior
- [ ] Preserve the SheepShaver AppImage and document a private backup procedure for the ROM and Mac OS disk image
- [ ] Document how Kiwix content files are backed up and restored separately from the Flatpak application
- [ ] Review the three archived Python virtual environments and mark each one as required, optional, historical, or disposable

## Priority 2: exact hardware reproduction

- [ ] Replace the system-level wiring map with a connector-by-connector schematic showing polarity, pin numbers, wire colors, wire gauges, connector orientation, and strain relief
- [ ] Label every custom 5V rail output and document the exact load connected to each JST socket
- [ ] Record the exact JST connector family, pitch, mating housings, and terminal part numbers if they can be confirmed
- [ ] Record the exact final LCD panel and controller-board model text, connector type, and ribbon orientation if visible
- [ ] Add a strict disassembly and assembly sequence, including shelf insertion, cable-routing order, LCD/bezel/braces/feet order, and when each connector must be attached
- [ ] Record screw locations, screw lengths, thread sizes, original fasteners reused, zip-tie locations, tape locations, adhesive locations, and any critical clearances
- [ ] Document the boot-chime storage medium, supported audio format, track filenames, selector-position mapping, and replacement procedure
- [ ] Archive or privately preserve the boot-chime audio files used by the final selector configuration
- [ ] Document the complete bag-charging path from Qi transmitter through the PiForma receiver and into the Anker charging input
- [ ] Record measured idle/load power, rail voltage under load, approximate battery runtime, charging time, maximum Pi temperature, throttling state, and internal charger temperature
- [ ] Record the exact deployed ZMK keyboard firmware commit, configuration branch, build command, firmware hash, flashing procedure, and Bluetooth reset/pairing procedure

## Priority 3: documentation corrections and polish

- [ ] Update `docs/hardware.md` so the Apple-logo hold behavior lists the current 2-second, 6-second, and 10-second actions
- [ ] Replace the stale “link to be added” mouse-shell note in `docs/bom.md` with the existing Printables links
- [ ] Restore or replace the missing Space Jam launcher icon
- [ ] Correct invalid or incomplete `Categories=` fields in the archived AtEase launchers after comparing them with the live files
- [ ] Update `docs/cleanup-plan.md` so every archive item is marked completed, still missing, historical, or intentionally excluded
- [ ] Explicitly state the license for original STL, 3MF, and OpenSCAD files in `LICENSE.md`
- [ ] Decide whether the unusual `nobody:nogroup` ownership of deployed PiForma scripts and binaries should be corrected, then document the intended ownership
- [ ] Validate the archived system units on the unrestricted Pi console with `systemd-analyze verify`
- [ ] Decide whether `dex` should be installed as the documented `.desktop` launcher fallback used by the companion application guidance

## Final project photos

- [ ] Front beauty shot
- [ ] Rear controls and ports
- [ ] Interior with the case open
- [ ] Three-level shelf assembly
- [ ] Custom 5V power rail
- [ ] LCD controller and ribbon orientation
- [ ] Battery position and rear plunger
- [ ] Boot-chime selector and sound module
- [ ] Apple-logo touch sensor
- [ ] Bluetooth ADB keyboard conversion
- [ ] Matching wireless mouse
- [ ] Bag interior and wireless charging arrangement
- [ ] Folding monitor stand

## Definition of archival-grade

This checklist is complete when a second microSD card can be built from a named base image using the repository, the hardware can be disassembled and rewired without relying on memory, all legally distributable recovery assets are archived, private/copyrighted assets have an explicit private-backup procedure, and every final feature passes the verification checklist in `docs/software-installation.md`.
