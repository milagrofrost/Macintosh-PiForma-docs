# PiForma Configuration Archive

## Purpose

This directory stores verified recovery snapshots for PiForma configuration files that are needed to rebuild the live `macintosh-piforma` desktop, launchers, panel layout, boot behavior, input defaults, and emulator preferences.

The initial audit found that `config/` contained only this README. The files now archived here were copied from the live Pi during the July 2026 audit rather than recreated from documentation.

## Source-of-truth Policy

During the initial archival audit, the live Pi is the source of truth. Once a live file has been verified and imported here, the repository should become the maintained source for future revisions.

For future changes:

1. Compare the repository copy with the deployed file.
2. Import the verified live version if this archive is stale.
3. Make future changes in a Git branch.
4. Validate syntax and application-specific behavior.
5. Deploy the reviewed file to the Pi.
6. Restart the associated service or session component.
7. Verify logs and behavior.
8. Commit configuration and documentation changes together.

Do not replace a working live configuration with a file reconstructed from old notes. Also do not blindly restore files marked historical, fallback, missing, sanitized, hardware-specific, or unverified.

## Current Configuration Inventory

| Repository path | Live destination | Component | Status | Sanitized | Last verified |
|---|---|---|---|---|---|
| `config/boot/firmware/config.txt` | `/boot/firmware/config.txt` | Raspberry Pi firmware boot config | active | no | July 2026 audit |
| `config/keyboard/default-keyboard` | `/etc/default/keyboard` | Keyboard defaults | active | no | July 2026 audit |
| `config/lxsession/rpd-x-autostart` | `/home/frost/.config/lxsession/rpd-x/autostart` | User LXSession autostart | active user override | no | July 2026 audit |
| `config/lxsession/system-rpd-x-autostart` | `/etc/xdg/lxsession/rpd-x/autostart` | System LXSession autostart | system fallback | no | July 2026 audit |
| `config/openbox/rpd-rc.xml` | `/home/frost/.config/openbox/rpd-rc.xml` | Openbox window manager | active | no | July 2026 audit |
| `config/pcmanfm/desktop-items-0.conf` | `/home/frost/.config/pcmanfm/LXDE-pi/desktop-items-0.conf` | PCManFM desktop | active | no | July 2026 audit |
| `config/piforma-panel/config.yaml` | `/home/frost/.local/share/piforma-panel/config.yaml` | PiForma Panel | active | no | July 2026 audit |
| `config/control-strip/config.yaml` | `/home/frost/.local/share/control-strip/config.yaml` | Control Strip simulator | active | no | July 2026 audit |
| `config/control-strip/scripts/window-check.sh` | `/home/frost/.local/share/control-strip/scripts/window-check.sh` | Control Strip window detector | active helper | no | July 2026 audit |
| `config/atease/config.yaml` | `/home/frost/.local/share/atease/config.yaml` | AtEase shell | active | no | July 2026 audit |
| `config/atease/apps/*.desktop` | `/home/frost/.local/share/atease/apps/` | AtEase main folder launchers | active launcher configs | no | July 2026 audit |
| `config/atease/apps-2/*.desktop` | `/home/frost/.local/share/atease/apps-2/` | AtEase sites folder launchers | active launcher configs | no | July 2026 audit |
| `config/sheepshaver/prefs` | `/home/frost/.config/SheepShaver/prefs` | SheepShaver Mac OS 9 emulator | active for launcher | no | July 2026 audit |
| `config/historical/lxpanel-pi/panel` | `/home/frost/.config/lxpanel-pi/panels/panel` | LXPanel | historical fallback | no | July 2026 audit |
| `config/historical/tint2/tint2rc` | `/home/frost/.config/tint2/tint2rc` | tint2 | historical fallback | no | July 2026 audit |
| `config/historical/tint2/tint2rc_bak` | `/home/frost/.config/tint2/tint2rc_bak` | tint2 backup | historical fallback | no | July 2026 audit |
| `config/historical/atease-legacy/config.yaml` | `/home/frost/.config/atease/config.yaml` | older AtEase config path/schema | historical | no | July 2026 audit |
| `config/historical/pcmanfm-default/desktop-items-0.conf` | `/home/frost/.config/pcmanfm/default/desktop-items-0.conf` | older PCManFM profile | historical fallback | no | July 2026 audit |

The live `/boot/config.txt` file is only a pointer to `/boot/firmware/config.txt` on this Debian 13 Raspberry Pi installation and is not archived separately. `/home/frost/.asoundrc` and `/home/frost/.sheepshaver_prefs` were not found during the audit.

## Active Configurations

### Boot Firmware

`config/boot/firmware/config.txt` is the authoritative boot configuration. It preserves the live comments and PiForma-specific settings, including HDMI overscan margins, forced HDMI hotplug, disabled splash, UART enablement, VC4 KMS graphics, onboard audio enablement, CM4 USB OTG host behavior, and CM5 USB host overlay behavior.

The archived file should be restored to `/boot/firmware/config.txt`, not `/boot/config.txt`.

### Keyboard

`config/keyboard/default-keyboard` archives `/etc/default/keyboard`. The live file uses the US keyboard layout and sets `XKBOPTIONS="ctrl:swap_lwin_lctl"`, which affects modifier behavior on the PiForma keyboard setup.

### LXSession Autostart

The live user override and the system default both contain only:

```text
@pcmanfm-pi
@xscreensaver -no-splash
```

PiForma Panel, Control Strip, and AtEase are handled by services rather than by this autostart file. Restoring an older autostart that starts those components directly could create duplicate launches.

### Openbox

`config/openbox/rpd-rc.xml` is the active Openbox configuration. The live session is running `openbox --config-file /home/frost/.config/openbox/rpd-rc.xml`.

This snapshot includes PiForma-specific window placement and application rules, including behavior for the panel, Control Strip, AtEase, Clippy, fullscreen windows, decorations, focus, and desktop count. Restore it as a full file unless a later migration deliberately changes the window-manager policy.

### PCManFM Desktop

`config/pcmanfm/desktop-items-0.conf` controls the active PCManFM desktop profile. The live file uses a black color background, ChicagoFLF desktop font, no window-manager desktop menu, no thumbnails, trash icon visible, and mounted volumes hidden.

The historical default PCManFM profile is archived separately under `config/historical/pcmanfm-default/`.

### PiForma Panel

`config/piforma-panel/config.yaml` is the active PiForma Panel configuration. The live `piforma-panel.service` runs `/usr/bin/piforma-panel`, and the verified configuration path is `/home/frost/.local/share/piforma-panel/config.yaml`.

The file defines the panel size and position, top corner radii, Charcoal font settings, Apple logo path, clock format, application scan directories, menu visibility, and desktop applications that should continue showing while the panel is active.

The checked source code recognizes the `bar`, `apple`, `clock`, `applications`, `menus`, `actions`, and `diagnostics` sections. The live file also includes `show_desktop_apps`; preserve that key when restoring because it is part of the deployed configuration even though it was not present in the checked source schema.

### Control Strip

`config/control-strip/config.yaml` is the active Control Strip configuration and `config/control-strip/scripts/window-check.sh` is the archived helper script from `/home/frost/.local/share/control-strip/scripts/window-check.sh`.

The live `controlstrip-simulator.service` runs `/usr/bin/controlstrip-simulator` with `WorkingDirectory=%h/.local/share/control-strip`. The configuration defines window geometry, visible icon behavior, snap-back timing, rounded bottom-left screen corner behavior, filtered window classes, and pinned applications for Chromium, LXTerminal, and PCManFM.

The Control Strip source checkout on the Pi uses the misspelled path `/home/frost/controlstrip-simualtor`. Do not silently correct that path in source or service references; treat it as an operational detail until a coordinated migration is made.

### AtEase

`config/atease/config.yaml`, `config/atease/apps/`, and `config/atease/apps-2/` archive the current AtEase configuration. The live `atease.service` runs `/usr/bin/atease`.

The current config uses the newer `/home/frost/.local/share/atease/config.yaml` layout with render geometry, window behavior, two folders, and `startup_folder: main`. An older schema still exists at `/home/frost/.config/atease/config.yaml` and is archived as historical only.

### SheepShaver

`config/sheepshaver/prefs` archives the active SheepShaver preference file referenced by the Mac OS 9 AtEase launcher. It contains local paths for the disk image, ROM, shared folder, serial port, and display settings.

The ROM, disk images, and other binary emulator assets are not stored in this configuration archive. They must be supplied separately during recovery.

## Historical And Fallback Configurations

`config/historical/lxpanel-pi/panel` is preserved because the old desktop stack used LXPanel-style configuration, but no `lxpanel` process was active during the audit. PiForma Panel is the active top panel.

`config/historical/tint2/` is preserved because tint2 configuration files exist on the live system, but no `tint2` process was active during the audit.

`config/historical/atease-legacy/config.yaml` preserves the older AtEase configuration path and schema. It should not be restored over the current `.local/share/atease` configuration without checking the installed AtEase build.

`config/historical/pcmanfm-default/desktop-items-0.conf` preserves the older default PCManFM profile. The active profile is `LXDE-pi`.

## AtEase Launchers

These `.desktop` files were copied from the live AtEase folders. The executable targets were checked during the audit; all were present. `desktop-file-validate` reports category-field errors in several copied live launchers, and the Space Jam launcher references a missing icon file. These files are preserved as live snapshots rather than silently rewritten during archival.

| Launcher | Repository file | Live file | Exec target | Notes |
|---|---|---|---|---|
| America Online | `config/atease/apps/America Online.desktop` | `/home/frost/.local/share/atease/apps/America Online.desktop` | `chromium` | Chromium kiosk web app |
| Netscape | `config/atease/apps/Chromium-70.desktop` | `/home/frost/.local/share/atease/apps/Chromium-70.desktop` | `chromium` | Uses `--force-device-scale-factor=0.7` |
| Encarta | `config/atease/apps/Encarta.desktop` | `/home/frost/.local/share/atease/apps/Encarta.desktop` | `flatpak` | Runs `org.kiwix.desktop` |
| Flying Toasters | `config/atease/apps/FlyingToasters.desktop` | `/home/frost/.local/share/atease/apps/FlyingToasters.desktop` | `chromium` | Chromium kiosk to localhost; companion HTTP server is `flyingtoasters.service` |
| LimeWire | `config/atease/apps/LimeWire.desktop` | `/home/frost/.local/share/atease/apps/LimeWire.desktop` | `chromium` | Chromium kiosk web app |
| Mac OS 9 | `config/atease/apps/MacOS9.desktop` | `/home/frost/.local/share/atease/apps/MacOS9.desktop` | `/home/frost/emulation/SheepShaver-aarch64.AppImage` | Uses archived SheepShaver prefs |
| Macintosh HD | `config/atease/apps/Macintosh-HD.desktop` | `/home/frost/.local/share/atease/apps/Macintosh-HD.desktop` | `pcmanfm` | Opens `/home/frost` |
| Retropie | `config/atease/apps/Retropie.desktop` | `/home/frost/.local/share/atease/apps/Retropie.desktop` | `lxterminal` | Runs `emulationstation --debug` |
| Terminal | `config/atease/apps/Terminal.desktop` | `/home/frost/.local/share/atease/apps/Terminal.desktop` | `/usr/bin/lxterminal` | Opens zsh |
| Weather Channel | `config/atease/apps/Weather Channel.desktop` | `/home/frost/.local/share/atease/apps/Weather Channel.desktop` | `/home/frost/weather-channel/weather-channel.sh` | Custom script discovered through launcher |
| Winamp | `config/atease/apps/Winamp.desktop` | `/home/frost/.local/share/atease/apps/Winamp.desktop` | `qmmp` | Music player launcher |
| Cameron's World | `config/atease/apps-2/01-camerons-world.desktop` | `/home/frost/.local/share/atease/apps-2/01-camerons-world.desktop` | `chromium` | Uses `--force-device-scale-factor=0.7` |
| Homestar Runner | `config/atease/apps-2/02-homestar-runner.desktop` | `/home/frost/.local/share/atease/apps-2/02-homestar-runner.desktop` | `chromium` | Uses `--force-device-scale-factor=0.7` |
| Space Jam 1996 | `config/atease/apps-2/03-space-jam-1996.desktop` | `/home/frost/.local/share/atease/apps-2/03-space-jam-1996.desktop` | `chromium` | Icon path missing: `/home/frost/.local/share/icons/space-jam-1996.png` |
| Windows 93 | `config/atease/apps-2/04-windows-93.desktop` | `/home/frost/.local/share/atease/apps-2/04-windows-93.desktop` | `chromium` | Uses `--force-device-scale-factor=0.7` |
| Infinite Mac | `config/atease/apps-2/05-infinite-mac.desktop` | `/home/frost/.local/share/atease/apps-2/05-infinite-mac.desktop` | `chromium` | Uses `--force-device-scale-factor=0.7` |
| Shareware CDs | `config/atease/apps-2/06-shareware-cds.desktop` | `/home/frost/.local/share/atease/apps-2/06-shareware-cds.desktop` | `chromium` | Uses `--force-device-scale-factor=0.7` |
| TEXTFILES.COM | `config/atease/apps-2/07-textfiles.desktop` | `/home/frost/.local/share/atease/apps-2/07-textfiles.desktop` | `chromium` | Uses `--force-device-scale-factor=0.7` |
| Neocities | `config/atease/apps-2/08-neocities.desktop` | `/home/frost/.local/share/atease/apps-2/08-neocities.desktop` | `chromium` | Uses `--force-device-scale-factor=0.7` |
| The Old Net | `config/atease/apps-2/09-the-old-net.desktop` | `/home/frost/.local/share/atease/apps-2/09-the-old-net.desktop` | `chromium` | Uses `--force-device-scale-factor=0.7` |
| Web Design Museum | `config/atease/apps-2/10-web-design-museum.desktop` | `/home/frost/.local/share/atease/apps-2/10-web-design-museum.desktop` | `chromium` | Uses `--force-device-scale-factor=0.7` |

The Weather Channel launcher is the only archived launcher that directly invokes a custom shell script. Other launchers invoke Chromium, Flatpak, PCManFM, SheepShaver, EmulationStation through LXTerminal, LXTerminal itself, or QMMP. Launcher validation currently reports unregistered or incomplete `Categories` values for America Online, Encarta, LimeWire, Macintosh HD, Weather Channel, and Winamp; those values match the deployed files.

## Permissions And Ownership

The archive preserves live file modes. Important examples from the audit:

| Live file | Owner | Mode |
|---|---|---|
| `/boot/firmware/config.txt` | `root:root` | `755` |
| `/etc/default/keyboard` | `root:root` | `644` |
| `/home/frost/.config/openbox/rpd-rc.xml` | `frost:frost` | `644` |
| `/home/frost/.local/share/control-strip/scripts/window-check.sh` | `frost:frost` | `755` |
| `/home/frost/.local/share/atease/apps/*.desktop` | `frost:frost` | `775` |
| `/home/frost/.local/share/atease/apps-2/*.desktop` | `frost:frost` | `755` |

Executable helper scripts and launchers should retain executable mode. Service files belong under `systemd/system/` or `systemd/user/`, not in `config/`.

Check repository modes with:

```bash
git ls-files --stage config/
```

Check live modes with:

```bash
stat -c '%A %a %U:%G %n' /path/to/live/file
```

## Validation

Use format-specific validation after importing or editing files:

```bash
python3 - <<'PY'
import pathlib
import yaml

for path in pathlib.Path("config").rglob("*.yaml"):
    with path.open("r", encoding="utf-8") as handle:
        yaml.safe_load(handle)
    print(f"OK: {path}")
PY

xmllint --noout config/openbox/rpd-rc.xml
bash -n config/control-strip/scripts/window-check.sh
desktop-file-validate config/atease/apps/*.desktop
desktop-file-validate config/atease/apps-2/*.desktop
```

If `xmllint` is unavailable, use Python XML parsing:

```bash
python3 - <<'PY'
import xml.etree.ElementTree as ET
ET.parse("config/openbox/rpd-rc.xml")
print("OK: config/openbox/rpd-rc.xml")
PY
```

YAML parsing only proves syntax. For PiForma Panel, Control Strip, and AtEase, compare keys against the installed application source or the current documented schema before changing behavior.

## Comparing Before Copying

Always compare before importing from the live Pi or restoring to it:

```bash
diff -u \
  config/piforma-panel/config.yaml \
  /home/frost/.local/share/piforma-panel/config.yaml

diff -u \
  config/control-strip/config.yaml \
  /home/frost/.local/share/control-strip/config.yaml

diff -ruN \
  config/atease/apps \
  /home/frost/.local/share/atease/apps
```

For a verified import from live to repository:

```bash
cp --preserve=mode,timestamps \
  /home/frost/.local/share/control-strip/scripts/window-check.sh \
  config/control-strip/scripts/window-check.sh
```

For a reviewed restore from repository to live, use the matching destination from the inventory table, then restart or reload the owning component. For example:

```bash
cp --preserve=mode,timestamps \
  config/piforma-panel/config.yaml \
  /home/frost/.local/share/piforma-panel/config.yaml

systemctl --user restart piforma-panel.service
systemctl --user status piforma-panel.service --no-pager
```

Do not use the historical files as restore inputs unless you are intentionally rolling back to an older desktop stack.

## Sensitive Data Policy

The audit did not find passwords, tokens, private keys, API keys, Wi-Fi credentials, browser cookies, SSH keys, or private certificates in the archived files.

The SheepShaver prefs include local emulator asset paths, but not the ROM or disk images themselves. Those supporting binary files are intentionally excluded.

These locations are intentionally excluded from this archive unless a separate sanitized backup strategy is requested:

```text
/etc/NetworkManager/system-connections/
/home/frost/.ssh/
/home/frost/.config/chromium/
/home/frost/.mozilla/
```

If a future configuration file contains a required private value, replace only the repository snapshot with a clear marker such as `REDACTED_NOT_STORED_IN_REPOSITORY` and document that the archived file cannot be copied blindly.

## Missing Or Not Archived

| Live path | Status | Reason |
|---|---|---|
| `/boot/config.txt` | not archived | Stub pointing to `/boot/firmware/config.txt` |
| `/home/frost/.asoundrc` | not found | Current audio services do not depend on an archived ALSA dotfile |
| `/home/frost/.sheepshaver_prefs` | not found | Active SheepShaver prefs are under `.config/SheepShaver/prefs` |
| Browser profiles and caches | intentionally excluded | Runtime state and possible secrets |
| NetworkManager connections | intentionally excluded | Wi-Fi/network credentials |
| SSH configuration and keys | intentionally excluded | private credentials |

## Related Documentation

- [Software overview](../docs/software.md)
- [Maintenance guide](../docs/maintenance.md)
- [Live system audit](../docs/live-system-audit.md) is a dated snapshot, not the current source of truth.
- [Scripts archive](../scripts/README.md)
- [Systemd archive](../systemd/README.md)
