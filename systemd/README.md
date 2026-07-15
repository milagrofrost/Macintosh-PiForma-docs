# PiForma systemd Services

## Purpose

This directory archives the verified systemd unit files from the live `macintosh-piforma` Pi. It is a recovery and maintenance reference, not a place for reconstructed service files.

Audit date: 2026-07-15.

## System Units And User Units

System units are installed under `/etc/systemd/system/` and managed with `systemctl`. PiForma currently uses system units for GPIO hardware helpers, AtEase, and the Flying Toasters local web server.

User units are installed under `/home/frost/.config/systemd/user/` and managed with `systemctl --user` from the `frost` user manager. PiForma currently uses user units for graphical desktop components and the USB audio loop.

Running `systemctl status` without `--user` will not show a user unit.

## Source-Of-Truth Policy

1. During the initial audit, the installed live unit is the source of truth.
2. Import the verified live unit into Git.
3. After archival, make future service changes in this repository.
4. Validate the edited unit.
5. Deploy it to the correct system or user location.
6. Run the matching daemon reload.
7. Restart only the affected service.
8. Verify service state, logs, and actual behavior.
9. Commit implementation and documentation changes together.

Do not normalize or redesign a working unit during import unless the live system has a verified defect or a deliberate migration requires it.

## Current Service Inventory

Observed active state is a point-in-time audit result, not a permanent guarantee.

| Unit | Scope | Purpose | Live fragment path | Repository path | Enabled | Active | Started after | Exec target | Last verified |
|---|---|---|---|---|---|---|---|---|---|
| `apple-gesture-button.service` | system | Apple-logo touch gesture handler | `/etc/systemd/system/apple-gesture-button.service` | `systemd/system/apple-gesture-button.service` | enabled | active/running | `graphical.target`, `display-manager.service` | `/usr/bin/python3` -> `/usr/local/bin/apple_gesture_button.py` | 2026-07-15 |
| `volume-knob.service` | system | EC11 GPIO volume knob | `/etc/systemd/system/volume-knob.service` | `systemd/system/volume-knob.service` | enabled | active/running | `graphical.target` | `/usr/bin/python3` -> `/usr/local/bin/volume_knob.py` | 2026-07-15 |
| `atease.service` | system | AtEase launcher shell | `/etc/systemd/system/atease.service` | `systemd/system/atease.service` | enabled | active/running | `display-manager.service`, `graphical.target` | `/usr/bin/atease` | 2026-07-15 |
| `flyingtoasters.service` | system | Local Flying Toasters HTTP server | `/etc/systemd/system/flyingtoasters.service` | `systemd/system/flyingtoasters.service` | enabled | active/running | `network.target` | `/usr/bin/python3` | 2026-07-15 |
| `piforma-panel.service` | user | PiForma top panel | `/home/frost/.config/systemd/user/piforma-panel.service` | `systemd/user/piforma-panel.service` | enabled | active/running | `graphical-session.target` | `/usr/bin/piforma-panel` | 2026-07-15 |
| `controlstrip-simulator.service` | user | Control Strip simulator | `/home/frost/.config/systemd/user/controlstrip-simulator.service` | `systemd/user/controlstrip-simulator.service` | enabled | active/running | `graphical-session.target` | `/usr/bin/controlstrip-simulator` | 2026-07-15 |
| `usb-audio-loop.service` | user | External USB audio-input loop | `/home/frost/.config/systemd/user/usb-audio-loop.service` | `systemd/user/usb-audio-loop.service` | enabled | active/running | default user target | `/home/frost/bin/usb-audio-loop.sh` | 2026-07-15 |

No PiForma-specific drop-ins were found for these units.

`n64-audio-loop.service` was checked and was `not-found`. Keep that old name only in historical migration notes.

## Startup Relationships

| Component | System service | User service | LXSession autostart | XDG autostart | Openbox autostart | Desktop launcher only | AtEase launcher only | Manual command | Application self-start | Duplicate automatic startup |
|---|---|---|---|---|---|---|---|---|---|---|
| Apple gesture button | yes | no | no | no | no | no | no | no | no | no |
| Volume knob | yes | no | no | no | no | no | no | no | no | no |
| AtEase | yes | no | no | no | no | yes, `/usr/share/applications/AtEase.desktop` | no | possible | no | no |
| Flying Toasters server | yes | no | no | no | no | no | paired with AtEase Chromium launcher | possible | no | no |
| PiForma Panel | no | yes | no | no | no | yes, `/usr/share/applications/PiForma Panel.desktop` | no | possible | no | no |
| Control Strip | no | yes | no | no | no | yes, `/usr/share/applications/ControlStrip Simulator.desktop` | no | possible | no | no |
| USB audio loop | no | yes | no | no | no | no | no | possible | no | no |
| Clippy | no | no | no | yes, `/home/frost/.config/autostart/clippy.desktop` | no | yes | no | possible | no | not a systemd duplicate |

The visible `.desktop` files for AtEase, PiForma Panel, and Control Strip are manual launchers, not automatic startup paths. LXSession autostart contains only `pcmanfm-pi` and `xscreensaver` in the inspected files. Openbox autostart has no PiForma service launches.

`/etc/xdg/autostart/env-display.desktop` runs `dbus-update-activation-environment --systemd DISPLAY WAYLAND_DISPLAY`, which helps imported graphical environment state reach the user manager.

## System Services

### `apple-gesture-button.service`

Runs as `User=frost` from `/home/frost`:

```ini
ExecStart=/usr/bin/python3 /usr/local/bin/apple_gesture_button.py
Restart=always
RestartSec=1
```

The script monitors GPIO 23 through `gpiozero` with `LGPIOFactory`. It maps taps to desktop launchers under `/home/frost/Desktop` and timed holds to closing windows, showing the desktop, or running `sudo /bin/systemctl poweroff`.

Although this is a system unit, it launches user desktop actions by running as `frost` and setting:

```text
HOME=/home/frost
DISPLAY=:0
XAUTHORITY=/home/frost/.Xauthority
XDG_RUNTIME_DIR=/run/user/1000
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
```

The live script exists and is executable. During the audit it was owned by `nobody:nogroup`, mode `0755`; that ownership is unusual for a system-executed helper and should be reviewed before future hardening.

### `volume-knob.service`

Runs as `User=frost` from `/home/frost`:

```ini
ExecStart=/usr/bin/python3 /usr/local/bin/volume_knob.py
Restart=always
RestartSec=1
```

The script reads the EC11 rotary encoder on GPIO 17 and 27 and the push switch on GPIO 22. It controls the PipeWire-compatible default sink with `pactl`, not direct ALSA mixer calls. The service supplies `XDG_RUNTIME_DIR=/run/user/1000` so `pactl` can reach the `frost` user audio session.

The live script exists and is executable. It was also owned by `nobody:nogroup`, mode `0755`; review that ownership before future hardening.

### `atease.service`

Runs AtEase as a system service under the `frost` user:

```ini
ExecStart=/usr/bin/atease
Restart=on-failure
RestartSec=2
```

The unit sets `DISPLAY=:0`, `XAUTHORITY=/home/frost/.Xauthority`, and `XDG_RUNTIME_DIR=/run/user/1000`. It does not set `DBUS_SESSION_BUS_ADDRESS`. The AtEase process was active during the audit and launched applications through `gio` from `/home/frost/.local/share/atease/apps/`.

AtEase also has a normal application launcher at `/usr/share/applications/AtEase.desktop`; that launcher is manual and is not an automatic duplicate.

The journal showed recurring Chromium D-Bus warnings from GUI applications launched by AtEase. These were not observed to stop the service.

### `flyingtoasters.service`

Runs a local static HTTP server as `frost`:

```ini
WorkingDirectory=/home/frost/.local/share/flyingtoasters/build
ExecStart=/usr/bin/python3 -m http.server 3000 --bind 127.0.0.1
Restart=always
RestartSec=3
```

The server listens on `127.0.0.1:3000`, so it is not exposed beyond localhost by this unit. Chromium is launched separately by the AtEase launcher `/home/frost/.local/share/atease/apps/FlyingToasters.desktop`.

The working directory exists. The journal showed normal local GET traffic and repeated 404s for `/joemama`; no restart loop was observed.

## User Services

### `piforma-panel.service`

Runs the PiForma top panel in the `frost` user manager:

```ini
ExecStart="/usr/bin/piforma-panel"
Restart=on-failure
RestartSec=2
After=graphical-session.target
PartOf=graphical-session.target
```

The binary exists and is executable. The service relies on the user manager's imported graphical environment. During the audit, `systemctl --user show-environment` included `DISPLAY=:0`, `XAUTHORITY=/home/frost/.Xauthority`, `DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus`, `XDG_RUNTIME_DIR=/run/user/1000`, and `XDG_SESSION_TYPE=x11`.

The panel is the custom menu bar and should not be duplicated by LXPanel or tint2 startup entries.

### `controlstrip-simulator.service`

Runs the Control Strip in the `frost` user manager:

```ini
ExecStart=/usr/bin/controlstrip-simulator
WorkingDirectory=%h/.local/share/control-strip
Restart=on-failure
RestartSec=2
After=graphical-session.target
PartOf=graphical-session.target
```

The binary and working directory exist. It uses the live configuration under `/home/frost/.local/share/control-strip`. The source checkout on the Pi is known to use the misspelled path `/home/frost/controlstrip-simualtor`; do not silently correct that operational path unless every reference is migrated together.

The status log showed active window placement and a non-fatal duplicate `.desktop` match for `About-piforma`.

### `usb-audio-loop.service`

Runs the canonical external USB audio loop helper:

```ini
ExecStart=%h/bin/usb-audio-loop.sh
Restart=always
```

The service runs `/home/frost/bin/usb-audio-loop.sh`. The old `n64-audio-loop.sh` and `n64-audio-loop.service` names are retired.

The script checks every five seconds for this PipeWire/PulseAudio source:

```text
alsa_input.usb-C-Media_Electronics_Inc._Cable_Creation-00.mono-fallback
```

When present, it sets the source volume to `50%` and starts `pw-loopback --capture="$SOURCE"` if `pgrep -f "$SOURCE"` does not already find a matching process. The supervising script stays active while the USB device is absent. It uses `pactl` and `pw-loopback`; it does not use `arecord`, `aplay`, `parec`, or `pacat` in the current live script.

## Installing Units

Install only units that are intended to be present and enabled on the target system.

System unit example:

```bash
sudo install -m 0644 \
  systemd/system/UNIT.service \
  /etc/systemd/system/UNIT.service

sudo systemctl daemon-reload
sudo systemctl enable UNIT.service
sudo systemctl restart UNIT.service
systemctl status UNIT.service --no-pager
```

User unit example:

```bash
install -m 0644 \
  systemd/user/UNIT.service \
  /home/frost/.config/systemd/user/UNIT.service

systemctl --user daemon-reload
systemctl --user enable UNIT.service
systemctl --user restart UNIT.service
systemctl --user status UNIT.service --no-pager
```

Do not enable every archived unit indiscriminately. Enabled state is deployment metadata, not unit source.

## Enabling And Disabling Units

Common unit-file states:

- `enabled`: starts through an install target.
- `disabled`: installed but not linked into an install target.
- `static`: has no independent enablement configuration.
- `indirect`: enabled through another unit relationship.
- `masked`: deliberately prevented from starting.
- `generated`: created dynamically.
- `not-found`: stale reference or missing unit.

This archive does not include `.wants/` or `.requires/` symlinks. Recreate enablement with `systemctl enable` or `systemctl --user enable` only when the target deployment should start that service.

## Validating Units

Repository validation commands:

```bash
systemd-analyze verify systemd/system/*.service
systemd-analyze --user verify systemd/user/*.service
grep -RIn '^ExecStart=' systemd/
grep -RIn '^WorkingDirectory=' systemd/
grep -RIn '^EnvironmentFile=' systemd/
```

Audit result: `systemd-analyze --user verify systemd/user/*.service` succeeded. `systemd-analyze verify systemd/system/*.service` could not run in the sandboxed shell because the system bus check failed with `SO_PASSCRED failed: Operation not permitted`; validate the system units on the Pi console or an unrestricted shell before deployment.

Syntax validation does not prove that the executable, display, D-Bus session, audio server, or working directory is available.

## Viewing Service Status And Logs

System services:

```bash
systemctl status UNIT.service --no-pager
journalctl -u UNIT.service -b --no-pager
systemctl cat UNIT.service
systemctl show UNIT.service
```

User services:

```bash
systemctl --user status UNIT.service --no-pager
journalctl --user -u UNIT.service -b --no-pager
systemctl --user cat UNIT.service
systemctl --user show UNIT.service
```

If running through `sudo` or from another account, make sure `systemctl --user` is querying the `frost` user manager, not root's user manager.

## Linger And Login Behavior

`loginctl show-user frost` could not be queried from this sandbox because the system bus was unavailable. User services were successfully queried through the active `frost` user manager, and the observed user environment had an active X11 `rpd-x` session.

Do not enable lingering automatically. Graphical user services generally should start after the graphical session exists. Persistent background user services can use lingering when intentionally configured, but audio and X11 applications may still fail without an active session even if lingering is enabled.

## Updating A Service

1. Edit the repository unit.
2. Run the relevant `systemd-analyze verify` command.
3. Check every `ExecStart=`, `WorkingDirectory=`, and `EnvironmentFile=` path.
4. Deploy only the affected unit.
5. Run `systemctl daemon-reload` or `systemctl --user daemon-reload`.
6. Restart only the affected service.
7. Check status, logs, and actual user-visible behavior.

## Recovery Procedure

For a broken system service:

```bash
sudo install -m 0644 systemd/system/UNIT.service /etc/systemd/system/UNIT.service
sudo systemctl daemon-reload
sudo systemctl restart UNIT.service
systemctl status UNIT.service --no-pager
journalctl -u UNIT.service -b --no-pager
```

For a broken user service:

```bash
install -m 0644 systemd/user/UNIT.service /home/frost/.config/systemd/user/UNIT.service
systemctl --user daemon-reload
systemctl --user restart UNIT.service
systemctl --user status UNIT.service --no-pager
journalctl --user -u UNIT.service -b --no-pager
```

If a graphical service fails, confirm `DISPLAY`, `XAUTHORITY`, `DBUS_SESSION_BUS_ADDRESS`, and `XDG_RUNTIME_DIR` in `systemctl --user show-environment`.

## Historical And Retired Units

- `n64-audio-loop.service`: obsolete name, `not-found` during this audit. Use `usb-audio-loop.service`.
- `n64-audio-loop.sh`: obsolete script name. Use `/home/frost/bin/usb-audio-loop.sh`.
- `asplashscreen.service`: present on the system as a RetroPie boot splash unit, but not archived here because it was outside the PiForma-specific service set for this task.
- `app-clippy@autostart.service`: generated from XDG autostart, not a hand-authored PiForma unit.
- `pipewire-media-session.service`, `pipewire-session-manager.service`, and `pulseaudio.service`: stale/not-found user references shown by `systemctl --user list-units --all`; current audio uses PipeWire and WirePlumber.

## Security Notes

- PiForma system services are configured with absolute paths and run as `frost`, not root, except for systemd itself supervising them.
- `apple-gesture-button.service` intentionally allows a desktop gesture to request shutdown through `sudo /bin/systemctl poweroff`; keep the corresponding sudoers rule narrow.
- The live `/usr/local/bin/apple_gesture_button.py`, `/usr/local/bin/volume_knob.py`, `/usr/bin/atease`, `/usr/bin/piforma-panel`, and `/usr/bin/controlstrip-simulator` were owned by `nobody:nogroup` during the audit. That is unusual for executable deployment paths and should be reviewed before any hardening pass.
- `flyingtoasters.service` binds to `127.0.0.1`, limiting exposure to localhost.
- No `EnvironmentFile=` directives were found, and no secrets were copied.
- `/home/frost/bin/usb-audio-loop.sh` and several working directories are user-writable by `frost`; this is expected for user services but should not be reused from root-running units without review.

## Related Documentation

- [Software](../docs/software.md)
- [Maintenance](../docs/maintenance.md)
- [Scripts](../scripts/README.md)
- [Config archive](../config/README.md)
- [Historical live audit](../docs/live-system-audit.md)
