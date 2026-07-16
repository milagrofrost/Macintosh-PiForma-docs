# Macintosh PiForma Software Installation

## Scope

This is the beginning of the fresh-install software saga. It documents the current known-good machine and a safe conceptual rebuild order. It is not yet a fully tested installer or a guarantee that the PiForma is reproducible from blank media.

## Current known-good system baseline

Confirmed current OS: Debian GNU/Linux 13.5 / Raspberry Pi OS Trixie-style desktop stack on `arm64`, with `armhf` enabled.

Probable original image family: Raspberry Pi OS with desktop for Debian 13/Trixie.

Unknown: exact Raspberry Pi OS image filename, image date, and whether every non-APT asset is archived.

## Rebuild profiles

Core PiForma contains the Raspberry Pi OS and X11 desktop foundation, LightDM, Openbox, PCManFM, PipeWire/WirePlumber, GPIO script dependencies, PiForma Panel, AtEase, Control Strip, Clippy, core scripts, configs, and services.

Current-feature PiForma adds actively configured features such as Chromium kiosk launchers, Weather Channel, Flying Toasters, QMMP, Flatpak/Kiwix, SheepShaver, RetroPie/EmulationStation, and retained remote access.

PiForma development workstation adds Rust/Cargo, Node.js/npm, Tauri build dependencies, Debian packaging tools, C/C++/CMake/Qt/media/emulator/hardware development headers.

Experimental full clone recreates the current package state most closely, including XFCE, Wayland/Weston, Xephyr, DOSBox-X, Tux Paint, Qtractor, Wine/armhf compatibility, alternate media tools, and historical build dependencies.

## Stage 1: Raspberry Pi OS base

Install the confirmed Raspberry Pi OS base on separate media. Create user `frost`, set hostname `macintosh-piforma`, and confirm UID, home path, graphical-session, and display assumptions before restoring PiForma services.

The future tested guide must name the exact starting image after a real rebuild test.

## Stage 2: APT sources and architecture

Restore Debian/Raspberry Pi Trixie APT sources as documented in `packages/apt-sources.txt`. Confirm native architecture `arm64` and foreign architecture `armhf`.

Do not add repositories or enable foreign architectures blindly on a live system without an explicit rebuild plan.

## Stage 3: System and desktop packages

Use `packages/apt-system-base.txt` as the base package reference. It contains curated top-level roots, not every dependency and not historical kernel versions.

Future rebuild simulation command, not run as an install during this audit:

```bash
grep -Ev '^[[:space:]]*(#|$)' packages/apt-system-base.txt \
  | xargs -r apt-get -s install
```

Future rebuild install command, to run only on rebuild media after simulation review:

```bash
grep -Ev '^[[:space:]]*(#|$)' packages/apt-system-base.txt \
  | xargs -r sudo apt install -y
```

## Stage 4: PiForma runtime packages

Use `packages/apt-piforma-runtime.txt` for directly evidenced repository-backed runtime roots. The local PiForma `.deb` package names are intentionally not in this APT profile.

```bash
grep -Ev '^[[:space:]]*(#|$)' packages/apt-piforma-runtime.txt \
  | xargs -r apt-get -s install
```

```bash
grep -Ev '^[[:space:]]*(#|$)' packages/apt-piforma-runtime.txt \
  | xargs -r sudo apt install -y
```

Then restore scripts, configs, local apps, and services before expecting the desktop to behave like PiForma.

## Stage 5: Local PiForma Debian packages

The local packages cannot be restored through normal configured APT repositories unless a package repository is created later.

Rebuild or reinstall:

- `about-this-pi-forma`
- `at-ease`
- `clippy`
- `control-strip-simulator`
- `pi-forma-panel`

Use `packages/local-deb-packages.tsv` for source paths, current checkout commits, found `.deb` files, found `.deb` metadata, hashes, build-command confidence, and file-comparison notes. Do not assume a found `.deb` was built from the current checkout unless `verified_build_source_commit` is populated. Do not assume the `.deb` files are safely archived just because they exist on the live machine.

## Stage 6: Optional applications and features

Install optional APT feature roots from `packages/apt-optional-features.txt` only for the current-feature or larger profiles.

```bash
grep -Ev '^[[:space:]]*(#|$)' packages/apt-optional-features.txt \
  | xargs -r apt-get -s install
```

```bash
grep -Ev '^[[:space:]]*(#|$)' packages/apt-optional-features.txt \
  | xargs -r sudo apt install -y
```

Restore Flatpak apps and AppImages from `packages/non-apt-software.tsv`.

## Stage 7: Development environment

Install development roots from `packages/apt-development.txt` for the development workstation profile.

```bash
grep -Ev '^[[:space:]]*(#|$)' packages/apt-development.txt \
  | xargs -r apt-get -s install
```

```bash
grep -Ev '^[[:space:]]*(#|$)' packages/apt-development.txt \
  | xargs -r sudo apt install -y
```

This intentionally includes broad C/C++, Tauri-adjacent, Qt, media, emulator, and Debian packaging support. Rust itself is managed through `rustup` and documented in `packages/development-toolchains.md`.

## Stage 8: Experimental and compatibility packages

Install experiments and compatibility roots only for the experimental full clone.

```bash
grep -Ev '^[[:space:]]*(#|$)' packages/apt-experiments.txt \
  | xargs -r apt-get -s install

grep -Ev '^[[:space:]]*(#|$)' packages/apt-compatibility.txt \
  | xargs -r apt-get -s install
```

```bash
grep -Ev '^[[:space:]]*(#|$)' packages/apt-experiments.txt \
  | xargs -r sudo apt install -y

grep -Ev '^[[:space:]]*(#|$)' packages/apt-compatibility.txt \
  | xargs -r sudo apt install -y
```

This is the closest APT root profile to the current machine, but it still does not automatically install exact historical kernel packages or guarantee exact old package versions.

## Stage 9: Non-APT software

Restore Flatpak apps, SheepShaver AppImage, RetroPie/EmulationStation, Pi-Apps if intentionally retained, user-local binaries, Rust toolchain state, Python virtual environments, and any emulator trees not owned by APT. `packages/python-environments.tsv` is an ownership inventory, not a blanket pip requirements file.

## Stage 10: Restore scripts, configurations, and services

Safe conceptual order:

1. install confirmed Raspberry Pi OS base
2. create user `frost`
3. configure hostname `macintosh-piforma`
4. confirm UID and graphical-session assumptions
5. configure APT sources and foreign architecture
6. install base and desktop packages
7. install PiForma runtime dependencies
8. install or rebuild local PiForma Debian packages
9. install optional applications
10. install development and experimental packages for those profiles
11. restore scripts
12. restore configuration files
13. restore system and user services
14. restore `.desktop` launchers
15. restore themes, icons, fonts, wallpaper, and other assets
16. restore non-APT applications
17. enable intended services
18. reboot
19. validate every feature

## Stage 11: Restore visual assets

Rebuild gaps needing owner archival decisions:

- exact Raspberry Pi OS image: unknown
- local PiForma `.deb` files: documented but not archived in Git
- PiForma source commits: documented
- GTK theme and icon themes: partially archived/configured, verify assets
- Chicago and Charcoal fonts: documented but not fully archived here
- Apple logo image, wallpaper, launcher icons, favicons: partially documented, verify archive completeness
- Weather Channel `launch.html` and `satellite.png`: documented but verify archive state
- Flying Toasters build directory: documented but not fully reproducible here
- Clippy assets: rebuildable from local source/deb, verify upstream/private assets
- Plymouth theme and boot files: partially archived, verify binary assets
- RetroPie, EmulationStation config, controller mappings: documented but not fully archived here
- SheepShaver AppImage: present locally
- SheepShaver ROM and Mac OS disk image: private or copyrighted asset
- Flatpak applications and Kiwix content: documented but content not fully archived
- sudoers rule for Apple-logo shutdown: verify and archive
- `env-display.desktop`: documented in systemd notes, verify archive
- Python packages not supplied by APT: dedicated inventory created in `packages/python-environments.tsv`; currently observed system Python distributions are Debian-managed, with three virtual environments requiring separate review

## Stage 12: Verification

After a rebuild, validate boot, display mode, LightDM autologin, Openbox, PCManFM desktop, PiForma Panel, AtEase, Control Strip, Clippy, Apple-logo tap/hold gestures, volume knob, audio output, USB audio loop, Weather Channel, Flying Toasters, Chromium launchers, QMMP, SheepShaver, RetroPie, Flatpak/Kiwix, VNC if retained, and service health.

## Remaining reproducibility gaps

The system is not ready to claim full reproducibility. Curated profiles have been validated as repository-backed roots, but they still require a fresh-media test. A tested fresh-install procedure requires separate media, an exact base image, confirmed asset archival, local `.deb` archival or rebuild automation, non-APT restore steps, and full feature validation.
