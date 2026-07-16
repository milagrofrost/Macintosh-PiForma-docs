# PiForma Package Inventory

## Purpose

This document explains the package snapshots under `packages/`. Those machine-readable files are the authoritative record of the live `macintosh-piforma` package state as audited on 2026-07-15.

## Audit scope and non-destructive decision

This began as a cleanup investigation, but the owner decided not to remove packages as part of this task. No APT or dpkg packages were installed, removed, purged, upgraded, marked, held, unheld, or reconfigured during this inventory work.

Experimental, compatibility, and development software is intentionally preserved. A package may belong to more than one conceptual role; the TSV assigns one primary role so future audits have readable diffs.

## System baseline

- Current OS: Debian GNU/Linux 13.5 / Raspberry Pi OS Trixie-style desktop stack.
- Hostname: `macintosh-piforma`.
- Native architecture: `arm64`.
- Foreign architecture: `armhf`.
- Active session: LightDM, Xorg, `rpd-x`, LXSession/LXDE, Openbox, PCManFM.
- Active PiForma processes: AtEase, PiForma Panel, Control Strip Simulator, Clippy, PipeWire, WirePlumber, Apple gesture button, volume knob, USB audio loop.
- Initial counts: 2911 dpkg package rows, 401 manual marks, 2508 automatic marks, held package `libsdl2-dev`.

The probable original image family is Raspberry Pi OS with desktop for Debian 13/Trixie. The exact image date or filename is not proven and must be named only after a rebuild test.

## APT repositories and architectures

Configured APT sources are Debian Trixie, Trixie updates, Trixie security, and Raspberry Pi Foundation Trixie. Components include `main`, `contrib`, `non-free`, and `non-free-firmware` for Debian, and `main` for Raspberry Pi.

See `packages/apt-sources.txt` for the sanitized source snapshot, architecture settings, policy output, and packages with only local `now` candidates.

## Installed package summary

Primary classification totals:

- `base-os`: 41
- `compatibility`: 14
- `dependency`: 1593
- `development-toolchain`: 600
- `experiment`: 71
- `feature-runtime`: 16
- `foreign-architecture`: 262
- `kernel-history`: 20
- `local-deb`: 5
- `optional-utility`: 227
- `piforma-core-runtime`: 29
- `raspberry-pi-hardware`: 31
- `unknown`: 2

APT marks are not functional roles. Manual marks may be experiments or convenience utilities. Automatic marks may be required by active applications.

## How packages were classified

Classification used dpkg status, APT marks, APT history, dpkg history, live process evidence, systemd unit files, launcher `Exec=` lines, script imports and commands, local source checkouts, and installed dependency parents.

For automatic packages, `packages/apt-package-roles.tsv` records dependency status and, where practical, nearby installed parent/root packages. Many dependency families are intentionally documented as groups here rather than thousands of repeated paragraphs.

## Base operating system and Raspberry Pi support

The base profile preserves Debian/Raspberry Pi OS core packages, firmware, kernel metapackages, Raspberry Pi utilities, networking, Bluetooth, LightDM/X11 desktop foundations, PipeWire audio foundation, and Raspberry Pi desktop metapackages.

See `packages/apt-system-base.txt`.

## Desktop runtime

The active desktop runtime is X11. Live process evidence shows LightDM, Xorg, `lxsession -s rpd-x -e LXDE`, Openbox, PCManFM, `picom`, and `xcompmgr`.

Both compositors are installed and running. They are therefore documented as active desktop runtime rather than cleanup candidates.

## Core PiForma runtime

Confirmed runtime packages include:

`about-this-pi-forma`, `at-ease`, `clippy`, `control-strip-simulator`, `pi-forma-panel`, `lightdm`, `openbox`, `pcmanfm`, `lxsession`, `picom`, `xcompmgr`, `pipewire`, `pipewire-audio`, `pipewire-pulse`, `wireplumber`, `pulseaudio-utils`, `python3`, `python3-gpiozero`, `python3-rpi-lgpio`, `wmctrl`, `xdotool`, `x11-utils`, `jq`, `libglib2.0-bin`, `desktop-file-utils`, `lxterminal`, and `zsh`.

`pulseaudio-utils` is core because it supplies `pactl`, used by the volume knob and USB audio loop scripts. `alsa-utils` is preserved as audio foundation/diagnostic support; no current script directly requires it as core runtime.

`libglib2.0-bin` is included because it supplies `gio`. No active launcher or service inspected in this audit directly invokes `gio`, and `dex` is not installed; AtEase may still use desktop-launching behavior internally, so `gio` is preserved as runtime support rather than treated as disposable.

See `packages/apt-piforma-runtime.txt`.

## Optional PiForma features

Optional/current features include Chromium kiosk launchers, QMMP/Winamp launcher, Flatpak/Kiwix Encarta launcher, VLC, Firefox, VNC packages, media tools, Flying Toasters, Weather Channel, RetroPie/EmulationStation, and SheepShaver.

Not all optional features are APT-owned. SheepShaver is an AppImage, RetroPie lives outside APT, and Kiwix is a Flatpak.

## Development and build toolchains

Development packages are intentionally preserved. Confirmed or likely groups include:

- Tauri/Rust/Node: `nodejs`, `npm`, Rust/Cargo from user-local tooling, WebKitGTK, GTK, Ayatana appindicator, GLib/GIO, and related libraries for PiForma Panel, AtEase, Control Strip, and About This PiForma.
- Debian packaging: `devscripts`, `debhelper`, `dh-autoreconf`, `dpkg-dev`, `build-essential`.
- C/C++ and media: GCC/G++, CMake, FFmpeg development libraries, PipeWire/ALSA/PulseAudio development libraries, USB/udev/DRM/GBM/X11 headers.
- Qt/media experiments: Qt 6 development packages and Qt Creator.
- Emulator/media source builds: SDL, FreeImage, FreeType, Boost filesystem, SpeexDSP, VLC development libraries, CDIO/ISO9660.

APT history shows explicit February 2026 source-build dependency batches for these groups.

## Experiments and possible future features

Preserved experiments include DOSBox-X, Qtractor, Tux Paint, XFCE, appmenu plugins, Weston/Wayland, Xephyr, `rpd-wayland`, `labwc`, `wayvnc`, Qt tools, and alternate desktop/media paths.

The first previously proposed removal batch, `dosbox-x`, `qtractor`, `tuxpaint`, and `tuxpaint-config`, is now classified as preserved experiments.

## Compatibility and foreign architecture

Compatibility packages include `armhf` libraries, Wine-related packages, Xwayland, Wayland libraries, and fallback display/session support. The foreign architecture remains configured and unchanged.

## Local Debian packages

Five locally built Debian packages are installed and not available from configured repositories:

- `about-this-pi-forma`
- `at-ease`
- `clippy`
- `control-strip-simulator`
- `pi-forma-panel`

Source paths, commits, dirty state, found `.deb` paths, and SHA-256 hashes are recorded in `packages/local-deb-packages.tsv`.

## Non-APT software

Non-APT inventory includes Flatpak apps (`org.kiwix.desktop`, `org.kde.marble`, `org.qgis.qgis`), SheepShaver AppImage, Tauri AppImage helpers, Pi-Apps, RetroPie, `/opt/retropie`, local emulation files, and user-local Codex/Claude binaries.

An APT-only package list cannot recreate the complete PiForma software stack.

## Held packages

`libsdl2-dev` is held. Installed version: `2.32.10+1rpi` for `arm64`; candidate version is also `2.32.10+1rpi` from the local dpkg status, while Debian Trixie offers `2.32.4+dfsg-1`. APT/dpkg history shows it was installed on 2026-02-21 during emulator/media development dependency work. No log line proving when the hold was set was found. The exact reason for the hold was not conclusively identified, so it remains unresolved for owner review. The hold was not changed.

## Unknown or unresolved package purposes

`packages/apt-unknown.txt` contains only dpkg config/status residue rows at the time of this audit: `rpi-connect-lite` and `tint2`. These are not active installed packages in the same sense as `ii` packages, but they remain in the dpkg-query snapshot for transparency.

## Rebuild profiles

- Core PiForma: Raspberry Pi OS/X11 desktop foundation, LightDM, Openbox, PCManFM, PipeWire/WirePlumber, GPIO dependencies, PiForma Panel, AtEase, Control Strip, Clippy, scripts, configs, and services.
- Current-feature PiForma: core plus Chromium kiosk launchers, Weather Channel, Flying Toasters, QMMP, Flatpak/Kiwix, SheepShaver, RetroPie/EmulationStation, and retained remote access.
- PiForma development workstation: current-feature plus Rust/Cargo, Node/npm, Tauri dependencies, Debian packaging tools, C/C++/CMake/Qt/media/emulator/hardware headers.
- Experimental full clone: closest reproduction of the current machine, including experiments, alternate desktops, Wayland/Xephyr, DOSBox-X, Tux Paint, Qtractor, Wine/armhf, compatibility layers, and historical dependencies.

## Known limitations

Exact package versions may not remain available in repositories forever. Local `.deb` files are present on this machine but are not committed here. Private or copyrighted assets, ROMs, disk images, Kiwix content, and some visual assets need separate archival decisions.

## Related files

- `packages/README.md`
- `packages/apt-installed.tsv`
- `packages/apt-package-roles.tsv`
- `packages/local-deb-packages.tsv`
- `packages/non-apt-software.tsv`
- `docs/software-installation.md`
- `docs/package-cleanup-proposal.md`
