# PiForma APT Cleanup Proposal

Audit date: 2026-07-15

This is the pre-change cleanup proposal for the live `macintosh-piforma` Raspberry Pi.
It is not the final fresh-install package manifest.

## Current Status: Preserved Inventory, Not Removal

This document began as a cleanup investigation. The owner has since decided that no package removal is authorized as part of this task, and no packages were removed during this work.

Experimental, compatibility, development, source-build, and possible future-feature software should be preserved and documented. Packages that were previously described as removal candidates are now classification candidates. "Not currently referenced" does not mean "unneeded"; it may mean development, experiment, fallback, alternate implementation, compatibility support, diagnostic utility, historical build dependency, or intentionally preserved unknown.

This file remains useful as the initial audit record. The canonical long-term package results now live in:

- [PiForma Package Inventory](package-inventory.md)
- [Macintosh PiForma Software Installation](software-installation.md)
- [`../packages/`](../packages/)

## System Snapshot

- OS: Debian GNU/Linux 13.5 (trixie)
- Kernel: `6.18.34+rpt-rpi-v8`
- Architecture: `arm64` / aarch64
- Foreign architecture: `armhf`
- Active desktop session: LightDM autologin, `rpd-x`, X11
- Active desktop processes: `lxsession -s rpd-x -e LXDE`, Openbox, `pcmanfm --desktop`, PiForma Panel, AtEase, ControlStrip Simulator, Clippy, PipeWire, WirePlumber
- Installed dpkg packages before cleanup: 2911
- Manually marked APT packages before cleanup: 401
- Automatically marked APT packages before cleanup: 2508
- Held packages: `libsdl2-dev`
- Failed systemd units before cleanup: none
- Failed user units before cleanup: none

## APT Sources

Configured repositories are Debian Trixie and Raspberry Pi Foundation Trixie for `arm64` and `armhf`:

- `http://deb.debian.org/debian/` suites `trixie trixie-updates`
- `http://deb.debian.org/debian-security/` suite `trixie-security`
- `http://archive.raspberrypi.com/debian/` suite `trixie`

No third-party APT repository was found. Local PiForma application packages installed outside configured repositories:

- `about-this-pi-forma`
- `at-ease`
- `clippy`
- `control-strip-simulator`
- `pi-forma-panel`

## Definitely Keep

These have direct live evidence from active services, live processes, or current launchers:

- Base display/session: `lightdm`, `rpd-x-core`, `rpd-x-extras`, `xserver-xorg`, `openbox`, `pcmanfm`, `lxsession`, `lxpolkit`, `picom`, `xcompmgr`
- PiForma apps: `pi-forma-panel`, `at-ease`, `control-strip-simulator`, `clippy`, `about-this-pi-forma`
- Audio/runtime: `pipewire`, `pipewire-audio`, `pipewire-pulse`, `wireplumber`, `pulseaudio-utils`, `alsa-utils`
- Script/runtime tools: `python3`, `python3-gpiozero`, `python3-rpi-lgpio`, `wmctrl`, `xdotool`, `x11-utils`, `jq`
- Launchers/features: `chromium`, `qmmp`, `flatpak`, `lxterminal`, `pcmanfm`
- Raspberry Pi support: `raspi-firmware`, `raspi-utils`, `rpi-eeprom`, `raspberrypi-sys-mods`, `raspberrypi-net-mods`, firmware packages, networking and Bluetooth packages

## Keep If Local Development Continues

These appear to support local building/packaging rather than base runtime:

- General build: `build-essential`, `cmake`, `gcc`, `g++`, `git`, `devscripts`, `debhelper`, `dh-autoreconf`, `shellcheck`
- Node/Tauri: `nodejs`, `npm`, `libwebkit2gtk-4.1-dev`, `libgtk-3-dev`, `libayatana-appindicator3-dev`
- PiForma/ControlStrip media or native builds: `libpipewire-0.3-dev`, `libspa-0.2-dev`, `libasound2-dev`, `libpulse-dev`, `libudev-dev`, `libx11-xcb-dev`, `libgbm-dev`, `libdrm-dev`, `libusb-1.0-0-dev`, FFmpeg dev packages
- Qt/local app experiments: `qt6-base-dev`, `qt6-multimedia-dev`, `qt6-tools-dev`, `qtcreator`, related Python/Qt packages
- Emulator or media build headers: `libvlc-dev`, `libvlccore-dev`, `libcdio-dev`, `libiso9660-dev`, `libsdl2-dev`, `libfreeimage-dev`, `libfreetype-dev`, `libboost-filesystem-dev`, `libspeexdsp-dev`

Do not remove this group until the owner decides whether this Pi remains a development machine.

## Optional Feature Packages

Keep unless the feature is intentionally removed:

- `qmmp`: current Winamp launcher target
- `flatpak`: current Kiwix/Encarta launcher target; Flatpak apps found: `org.kiwix.desktop`, `org.kde.marble`, `org.qgis.qgis`
- `chromium`: many AtEase kiosk launchers and Weather Channel/Flying Toasters
- `vlc`: no current AtEase launcher, but may be retained as optional media support
- `x11vnc`, RealVNC packages: remote access; owner decision
- RetroPie/EmulationStation: current AtEase launcher calls `emulationstation`, but it is not owned by APT
- SheepShaver: current AtEase launcher uses `/home/frost/emulation/SheepShaver-aarch64.AppImage`

## First Batch Reclassified As Preserved Experiments

These were initially identified as a possible small cleanup batch. That removal framing is now superseded. They are preserved as installed experiments unless future owner review establishes a different purpose.

| Package | Evidence | Simulation | Installed size | Disposition |
| --- | --- | --- | ---: | --- |
| `dosbox-x` | Docs mark DOSBox-X / Windows 98 as experimental or pending confirmation; no current AtEase launcher or live process found. | Earlier simulation removed only the four named packages; no real removal was run. | 11452 KiB | preserved experiment |
| `qtractor` | Audio workstation / music production experiment candidate; no service, current launcher, or live process found. | Earlier simulation removed only named packages; no real removal was run. | 8574 KiB | preserved experiment |
| `tuxpaint` | Docs mark Tux Paint as historical/dormant/pending owner confirmation; no current AtEase launcher or live process found. | Earlier simulation removed only named packages; no real removal was run. | 617 KiB | preserved experiment |
| `tuxpaint-config` | Configuration tool associated with the preserved Tux Paint experiment. | Earlier simulation removed only named packages; no real removal was run. | 1414 KiB | preserved experiment |

## Other Groups Reframed As Preserved Classifications

- XFCE packages: alternate desktop/session and appmenu experiment. Preserve.
- Wayland and Weston packages: alternate display/session experiment and Raspberry Pi desktop compatibility. Preserve.
- Xephyr: nested display testing tool. Preserve as experiment/diagnostic utility.
- `rpd-wayland` packages: Raspberry Pi desktop Wayland stack and alternate implementation. Preserve.
- `labwc`: Wayland compositor retained for alternate desktop testing. Preserve.
- `wayvnc`: Wayland remote-access support retained with the Wayland stack. Preserve.
- Wine and `armhf` packages: compatibility layer and foreign-architecture support. Preserve.
- VLC: optional media player and media-development support. Preserve.
- VNC packages: remote administration and fallback access. Preserve.
- Firefox: Raspberry Pi desktop application/fallback browser. Preserve.
- Old kernels: kernel history and possible boot fallback. Do not remove during package inventory work.
- Development headers: intentionally retained local build environment. Preserve.
- Qt development packages: Qt/local app experiments and development. Preserve.
- Media development packages: confirmed or likely source-build dependencies. Preserve.
- Emulator development packages: confirmed or likely emulator/source-build dependencies. Preserve.

## Superseded Cleanup Plan

The earlier plan to remove a first explicit batch is superseded and must not be followed. Current plan:

1. Preserve installed software.
2. Snapshot exact dpkg/APT state.
3. Classify packages by role and rebuild profile.
4. Document local `.deb` packages and non-APT software.
5. Build a future fresh-install guide without claiming reproducibility until a separate-media rebuild is tested.
