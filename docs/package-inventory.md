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
- Initial counts: 2911 dpkg status rows, 2908 fully installed `ii` rows, 1 held-installed `hi` row (`libsdl2-dev:arm64`), 2 config/status residue `rc` rows, 401 manual marks, 2508 automatic marks, held package `libsdl2-dev`.

The probable original image family is Raspberry Pi OS with desktop for Debian 13/Trixie. The exact image date or filename is not proven and must be named only after a rebuild test.

## APT repositories and architectures

Configured APT sources are Debian Trixie, Trixie updates, Trixie security, and Raspberry Pi Foundation Trixie. Components include `main`, `contrib`, `non-free`, and `non-free-firmware` for Debian, and `main` for Raspberry Pi.

See `packages/apt-sources.txt` for the sanitized source snapshot, architecture settings, policy output, and packages with no configured repository version. The scan found only the five local PiForma Debian packages as local-only; `libsdl2-dev` has a held local/status version but a lower Debian repository version exists.

## Installed package summary

There are two layers under `packages/`:

- Forensic state snapshots record what exists now, including dependency closure, local-only packages, experiments, foreign-architecture packages, historical kernels, and dpkg residue rows.
- Curated rebuild roots are deliberately selected top-level APT package names for future rebuild experiments. They are not generated from categories and intentionally omit dependency closure, local `.deb` packages, residue rows, and exact historical kernels.

Primary forensic classification totals:

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

The curated base profile selects Debian/Raspberry Pi OS roots, firmware and hardware support, networking, Bluetooth, supported Pi 4 arm64 kernel metapackages, and LightDM/X11 desktop foundations. Exact historical kernels and `rpd-wayland-*` are excluded from this X11 base profile and documented separately.

See `packages/apt-system-base.txt`.

## Desktop runtime

The active desktop runtime is X11. Live process evidence shows LightDM, Xorg, `lxsession -s rpd-x -e LXDE`, Openbox, PCManFM, `picom`, and `xcompmgr`.

Both compositors are installed and were observed running with parent PID 1 and the same start time. `picom` has explicit user LXDE-pi autostart evidence in `/home/frost/.config/lxsession/LXDE-pi/autostart`; `xcompmgr -aR` is referenced by `/etc/xdg/autostart/xcompmgr.desktop`. The core curated runtime includes `picom` only. `xcompmgr` is preserved in the experimental profile as a current-state compatibility/anomaly until a display test proves whether it is intentionally required.

## Core PiForma runtime

Confirmed core repository-backed runtime roots include:

`pipewire-audio`, `pipewire-bin`, `pipewire-pulse`, `wireplumber`, `pulseaudio-utils`, `python3`, `python3-gpiozero`, `python3-lgpio`, `wmctrl`, `xdotool`, `x11-utils`, `jq`, `libglib2.0-bin`, `lxterminal`, `zsh`, and `picom`.

The five local PiForma `.deb` packages (`about-this-pi-forma`, `at-ease`, `clippy`, `control-strip-simulator`, and `pi-forma-panel`) are core runtime applications but are deliberately excluded from repository-backed APT install commands.

`pulseaudio-utils` is core because it supplies `pactl`, used by the volume knob and USB audio loop scripts. `alsa-utils` is preserved as audio foundation/diagnostic support; no current script directly requires it as core runtime.

`libglib2.0-bin` is included because it supplies `gio`. No active launcher or service inspected in this audit directly invokes `gio`, and `dex` is not installed; AtEase may still use desktop-launching behavior internally, so `gio` is preserved as runtime support rather than treated as disposable. The AtEase and Control Strip repositories recommend `dex` as an optional fallback, so it should be tested during the fresh-media rebuild before deciding whether to add it to the runtime roots.

`python3-dbus-next`, `python3-libgpiod`, and `python3-rpi-lgpio` remain in the forensic installed-package inventory, but no direct active consumer was established during this audit. They are therefore not treated as minimal core installation roots.

See `packages/apt-piforma-runtime.txt`.

## Optional PiForma features

Optional/current features include Chromium kiosk launchers, QMMP/Winamp launcher, Flatpak/Kiwix Encarta launcher, VLC, Firefox, VNC packages, media tools, Flying Toasters, Weather Channel, RetroPie/EmulationStation, and SheepShaver.

Not all optional features are APT-owned. SheepShaver is an AppImage, RetroPie lives outside APT, and Kiwix is a Flatpak.

## Development and build toolchains

Development packages are intentionally preserved. Confirmed or likely groups include:

- Tauri/Rust/Node: `nodejs`, `npm`, Rust/Cargo from user-local tooling, WebKitGTK, GTK, Ayatana appindicator, GLib/GIO, OpenSSL, XDo, and related libraries for PiForma Panel, AtEase, Control Strip, and About This PiForma.
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

Source paths, current checkout commits, dirty state, found `.deb` paths, found `.deb` metadata, SHA-256 hashes, file-comparison notes, and build-command confidence are recorded in `packages/local-deb-packages.tsv`. Current checkout commit does not prove the found `.deb` was built from that commit; `verified_build_source_commit` remains blank unless a build record proves it.

The discovered About This PiForma `.deb` did not fully match the live installed files. One compared file differed and another expected file was missing. Treat that package as an unverified recovery artifact until it is rebuilt or independently validated.

## Non-APT software

Non-APT inventory includes Flatpak apps (`org.kiwix.desktop`, `org.kde.marble`, `org.qgis.qgis`), SheepShaver AppImage, Tauri AppImage helpers, Pi-Apps, RetroPie, `/opt/retropie`, local emulation files, user-local Codex/Claude binaries, the rustup Rust toolchain, and Python virtual environments. `packages/python-environments.tsv` separates Debian-managed Python distributions from virtualenvs and is not a pip restore manifest.

An APT-only package list cannot recreate the complete PiForma software stack.

## Held packages

`libsdl2-dev` is held. Installed version: `2.32.10+1rpi` for `arm64`; candidate version is also `2.32.10+1rpi` from the local dpkg status, while Debian Trixie offers `2.32.4+dfsg-1`. APT/dpkg history shows it was installed on 2026-02-21 during emulator/media development dependency work. No log line proving when the hold was set was found. The exact reason for the hold was not conclusively identified, so it remains unresolved for owner review. The hold was not changed.

## Unknown or unresolved package purposes

`packages/apt-unknown.txt` currently contains no curated install roots. The dpkg config/status residue rows `rpi-connect-lite` and `tint2` are recorded in `packages/dpkg-residue.txt` and remain visible in the forensic snapshots for transparency.

## Rebuild profiles

- Core PiForma: `apt-system-base.txt`, `apt-piforma-runtime.txt`, local PiForma `.deb` packages, scripts, configs, systemd units, and required visual assets.
- Current-feature PiForma: core plus `apt-optional-features.txt`, Flatpak applications, SheepShaver, RetroPie/EmulationStation, Weather Channel assets, Flying Toasters build, and retained remote access.
- PiForma development workstation: current-feature plus `apt-development.txt`, Rust toolchain, Node/npm build environment, and project source repositories.
- Experimental full clone: development workstation plus `apt-experiments.txt`, `apt-compatibility.txt`, foreign architecture configuration, and forensic historical package-state references. Historical exact kernel packages are documented but not automatically installed without an explicit historical-clone decision.

Curated root counts are: system base 36, PiForma runtime 15, optional features 31, development 85, experiments 25, compatibility 9, unknown 0. `apt-kernel-history.txt` records 20 historical kernel status entries.

## Known limitations

Exact package versions may not remain available in repositories forever. Local `.deb` files are present on this machine but are not committed here. Private or copyrighted assets, ROMs, disk images, Kiwix content, and some visual assets need separate archival decisions.

## Related files

- `packages/README.md`
- `packages/apt-installed.tsv`
- `packages/apt-package-roles.tsv`
- `packages/local-deb-packages.tsv`
- `packages/non-apt-software.tsv`
- `packages/python-environments.tsv`
- `packages/development-toolchains.md`
- `packages/validate-package-profiles.py`
- `docs/software-installation.md`
- `docs/package-cleanup-proposal.md`
