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

Use `packages/apt-system-base.txt` as the base package reference. It includes metapackages and important roots rather than every dependency.

Example command shape, not run during this audit:

```bash
sudo apt install $(grep -v '^#' packages/apt-system-base.txt)
```

## Stage 4: PiForma runtime packages

Use `packages/apt-piforma-runtime.txt` for directly evidenced runtime packages.

```bash
sudo apt install $(grep -v '^#' packages/apt-piforma-runtime.txt)
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

Use `packages/local-deb-packages.tsv` for source paths, commits, found `.deb` files, hashes, and dirty state. Do not assume the `.deb` files are safely archived just because they exist on the live machine.

## Stage 6: Optional applications and features

Install optional APT features from `packages/apt-optional-features.txt` only for the current-feature or larger profiles.

```bash
sudo apt install $(grep -v '^#' packages/apt-optional-features.txt)
```

Restore Flatpak apps and AppImages from `packages/non-apt-software.tsv`.

## Stage 7: Development environment

Install development packages from `packages/apt-development.txt` for the development workstation profile.

```bash
sudo apt install $(grep -v '^#' packages/apt-development.txt)
```

This intentionally includes broad C/C++, Rust/Tauri-adjacent, Qt, media, emulator, and Debian packaging support.

## Stage 8: Experimental and compatibility packages

Install experiments and compatibility packages only for the experimental full clone.

```bash
sudo apt install $(grep -v '^#' packages/apt-experiments.txt)
sudo apt install $(grep -v '^#' packages/apt-compatibility.txt)
```

This is the closest profile to the current machine. It is intentionally not a minimal install.

## Stage 9: Non-APT software

Restore Flatpak apps, SheepShaver AppImage, RetroPie/EmulationStation, Pi-Apps if intentionally retained, user-local binaries, Python package state, and any emulator trees not owned by APT.

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
- Python packages not supplied by APT: unresolved until separated from Debian-managed Python packages

## Stage 12: Verification

After a rebuild, validate boot, display mode, LightDM autologin, Openbox, PCManFM desktop, PiForma Panel, AtEase, Control Strip, Clippy, Apple-logo tap/hold gestures, volume knob, audio output, USB audio loop, Weather Channel, Flying Toasters, Chromium launchers, QMMP, SheepShaver, RetroPie, Flatpak/Kiwix, VNC if retained, and service health.

## Remaining reproducibility gaps

The system is not ready to claim full reproducibility. A tested fresh-install procedure requires separate media, an exact base image, confirmed asset archival, local `.deb` archival or rebuild automation, non-APT restore steps, and full feature validation.
