# PiForma Scripts

## Purpose

This directory stores recovery snapshots of scripts used by the Macintosh PiForma software stack. These files are meant to make the live system recoverable and reviewable in Git; they are not a dumping ground for reconstructed snippets from old notes.

The scripts installed on `macintosh-piforma` are the operational source of truth until a deployed copy has been verified and archived here. Repository copies should be updated from the live system after a working change is verified. Do not replace a working live script with a version reconstructed from documentation.

Once a repository copy has been verified against the deployed file, use the repository as the maintained source for future revisions: compare the live and repository copies, import the live version if the repository is stale, make changes on a Git branch, validate syntax, deploy the reviewed file, restart the associated service or launcher, verify behavior and logs, then commit the implementation and documentation together.

## Script Inventory

| Script | Purpose | Live path | Started by | Repository status |
|---|---|---|---|---|
| `apple_gesture_button.py` | Reads the capacitive Apple-logo input and interprets taps and timed holds for app, desktop, and power actions. | `/usr/local/bin/apple_gesture_button.py` | system service: `apple-gesture-button.service` | Archived as `scripts/apple_gesture_button.py` |
| `volume_knob.py` | Reads the EC11 rotary encoder and controls the PipeWire-compatible default audio sink through `pactl`. | `/usr/local/bin/volume_knob.py` | system service: `volume-knob.service` | Archived as `scripts/volume_knob.py` |
| `weather-channel.sh` | Launches the local Weather Channel / WeatherStar presentation through Chromium kiosk mode and the local splash page. | `/home/frost/weather-channel/weather-channel.sh` | AtEase `.desktop` launcher | Archived as `scripts/weather-channel.sh` |
| `usb-audio-loop.sh` | Detects the configured USB audio-input source and loops incoming audio to the PiForma speaker output. | `/home/frost/bin/usb-audio-loop.sh` | user service: `usb-audio-loop.service` | Archived as `scripts/usb-audio-loop.sh` |

## Active Deployed Scripts

### `apple_gesture_button.py`

Verified live path: `/usr/local/bin/apple_gesture_button.py`

Verified service: `apple-gesture-button.service`

The service runs `/usr/bin/python3 /usr/local/bin/apple_gesture_button.py` as user `frost`. The script reads the Apple-logo capacitive input, interprets taps and timed holds, and launches applications or performs desktop and power actions. Keep the detailed gesture map in [../docs/software.md](../docs/software.md) rather than duplicating it here.

Live verification showed the service active and enabled, with the process running from `/usr/local/bin/apple_gesture_button.py`.

### `volume_knob.py`

Verified live path: `/usr/local/bin/volume_knob.py`

Verified service: `volume-knob.service`

The service runs `/usr/bin/python3 /usr/local/bin/volume_knob.py` as user `frost`. The script reads the EC11 rotary encoder and controls the PipeWire-compatible default audio sink through `pactl`.

Do not treat older files such as `volume_control.py`, `volume_control2.py`, or `volume_knob.py_old` as current scripts unless a future live audit proves otherwise.

### `weather-channel.sh`

Verified live path: `/home/frost/weather-channel/weather-channel.sh`

Verified launcher: `/home/frost/.local/share/atease/apps/Weather Channel.desktop`

The AtEase launcher runs `/home/frost/weather-channel/weather-channel.sh`. The script kills existing Chromium processes, waits briefly, then starts Chromium in kiosk/fullscreen mode against `file:///home/frost/weather-channel/launch.html`. The local `launch.html` file is part of the Weather Channel / WeatherStar presentation flow.

This script is active or potentially active through the visible AtEase launcher even when no process is running during an audit. It would be missed by checking systemd services alone.

### `usb-audio-loop.sh`

Verified live path: `/home/frost/bin/usb-audio-loop.sh`

Verified service: `usb-audio-loop.service`

Repository archive: `scripts/usb-audio-loop.sh`

This is the generic external USB audio-input helper. It is not specific to Nintendo 64. It watches for the configured USB audio-input or capture device and loops incoming audio to the PiForma speaker output. The upstream source may be RCA, 3.5 mm, a console, or another analog source, as long as it reaches the Pi through a compatible USB audio adapter.

The current script selects the device by exact PipeWire/PulseAudio source name:

```text
alsa_input.usb-C-Media_Electronics_Inc._Cable_Creation-00.mono-fallback
```

When that source appears in `pactl list short sources`, the script sets the source volume to `50%` and starts `pw-loopback --capture="$SOURCE"` if no matching loopback process is already running. When the USB capture device is disconnected, the supervising script remains active and sleeps between checks.

The helper may be active as a service while no audio loop is running if the external USB input device is not connected.

## Historical Or Obsolete Names

The external USB audio helper was formerly discovered as `n64-audio-loop.sh` with a matching user service name. The current canonical names are `usb-audio-loop.sh` and `usb-audio-loop.service`. The old names should appear only in historical migration notes, not in current deployment instructions.

Older volume-control experiments such as `volume_control.py`, `volume_control2.py`, and `volume_knob.py_old` are not current scripts.

## Launcher Relationships

Custom `.desktop` launchers are part of script discovery because AtEase applications may invoke shell scripts, application binaries, Chromium kiosk sessions, AppImages, or command chains without any systemd reference.

| Launcher | Desktop file | Invoked target | Notes |
|---|---|---|---|
| Weather Channel | `/home/frost/.local/share/atease/apps/Weather Channel.desktop` | `/home/frost/weather-channel/weather-channel.sh` | Custom shell script; relevant to this directory. |
| Mac OS 9 | `/home/frost/.local/share/atease/apps/MacOS9.desktop` | `/home/frost/emulation/SheepShaver-aarch64.AppImage` | Existing AppImage, not a script archive candidate. |
| Terminal | `/home/frost/.local/share/atease/apps/Terminal.desktop` | `/usr/bin/lxterminal -e /usr/bin/zsh` | Command launcher, not a PiForma script. |
| Retropie | `/home/frost/.local/share/atease/apps/Retropie.desktop` | `lxterminal -e emulationstation --debug` | Command launcher; no script target found. |
| Flying Toasters | `/home/frost/.local/share/atease/apps/FlyingToasters.desktop` | Chromium kiosk URL | Browser launcher; no script target found. |
| America Online | `/home/frost/.local/share/atease/apps/America Online.desktop` | Chromium kiosk URL | Browser launcher; no script target found. |
| LimeWire | `/home/frost/.local/share/atease/apps/LimeWire.desktop` | Chromium kiosk URL | Browser launcher; no script target found. |
| Netscape | `/home/frost/.local/share/atease/apps/Chromium-70.desktop` | `chromium --force-device-scale-factor=0.7` | Browser launcher; no script target found. |
| Encarta | `/home/frost/.local/share/atease/apps/Encarta.desktop` | `flatpak run org.kiwix.desktop` | Flatpak launcher; no script target found. |
| Winamp | `/home/frost/.local/share/atease/apps/Winamp.desktop` | `qmmp` | Application launcher; no script target found. |
| Macintosh HD | `/home/frost/.local/share/atease/apps/Macintosh-HD.desktop` | `pcmanfm /home/frost` | File-manager launcher. |
| Pi-Apps | `/home/frost/.local/share/applications/pi-apps.desktop` | `/home/frost/pi-apps/gui` | Shell script from Pi-Apps, not a PiForma-maintained script. |
| Pi-Apps Settings | `/home/frost/.local/share/applications/pi-apps-settings.desktop` | `/home/frost/pi-apps/settings` | Shell script from Pi-Apps, not a PiForma-maintained script. |
| Claude Code URL Handler | `/home/frost/.local/share/applications/claude-code-url-handler.desktop` | `/home/frost/.local/bin/claude` | Existing symlink to a binary, not a PiForma script. |
| About This PiForma | `/home/frost/.local/share/applications/about-piforma.desktop`; `/home/frost/.local/share/applications/About This PiForma.desktop`; `/usr/share/applications/About This PiForma.desktop` | `about-piforma` | Binary in `/usr/bin`, not a script. |
| Clippy | `/home/frost/.local/share/applications/clippy.desktop`; `/usr/share/applications/clippy.desktop` | `clippy` | Resolved command, not archived under `scripts/`. |
| AtEase | `/usr/share/applications/AtEase.desktop` | `atease` | Binary in `/usr/bin`. |
| ControlStrip Simulator | `/usr/share/applications/ControlStrip Simulator.desktop` | `controlstrip-simulator` | Binary in `/usr/bin`. |
| PiForma Panel | `/usr/share/applications/PiForma Panel.desktop` | `piforma-panel` | Binary in `/usr/bin`. |

The AtEase secondary app directory, `/home/frost/.local/share/atease/apps-2/`, was also inspected. Its launchers currently invoke Chromium URLs directly and did not identify additional PiForma scripts.

No broken custom launcher targets were found in the inspected set. The only custom script discovered through `.desktop` inspection that would have been missed by systemd alone was `/home/frost/weather-channel/weather-channel.sh`.

## Deployment Locations

System-level scripts used by system services live under `/usr/local/bin` and were verified as `root:root` with executable mode `755`:

```text
/usr/local/bin/apple_gesture_button.py
/usr/local/bin/volume_knob.py
```

User-level scripts live under `/home/frost` and were verified as `frost:frost` with executable mode `775`:

```text
/home/frost/weather-channel/weather-channel.sh
/home/frost/bin/usb-audio-loop.sh
```

Repository copies should retain executable mode when the deployed script is executed directly. systemd service files belong under `systemd/`, not `scripts/`.

## Validating Scripts

Validate repository copies before deploying them:

```bash
python3 -m py_compile scripts/apple_gesture_button.py
python3 -m py_compile scripts/volume_knob.py
bash -n scripts/weather-channel.sh
bash -n scripts/usb-audio-loop.sh
```

Only run commands for files that are actually present in the repository. The verified active scripts listed in the inventory are now archived here.

Validate live files on the Pi with verified deployment paths:

```bash
PYTHONPYCACHEPREFIX=/tmp/piforma-pycache python3 -m py_compile /usr/local/bin/apple_gesture_button.py
PYTHONPYCACHEPREFIX=/tmp/piforma-pycache python3 -m py_compile /usr/local/bin/volume_knob.py
bash -n /home/frost/weather-channel/weather-channel.sh
bash -n /home/frost/bin/usb-audio-loop.sh
```

Check associated services only where verified services exist:

```bash
systemctl status apple-gesture-button.service --no-pager
systemctl status volume-knob.service --no-pager
systemctl --user status usb-audio-loop.service --no-pager
```

For launcher-driven scripts, inspect the launcher and then run the script syntax check:

```bash
grep -n '^Exec=' '/home/frost/.local/share/atease/apps/Weather Channel.desktop'
bash -n /home/frost/weather-channel/weather-channel.sh
```

## Permissions And Ownership

Use `stat` and Git mode bits to confirm executable state before and after archival:

```bash
stat -c '%A %a %U:%G %n' /usr/local/bin/apple_gesture_button.py
stat -c '%A %a %U:%G %n' /usr/local/bin/volume_knob.py
stat -c '%A %a %U:%G %n' /home/frost/weather-channel/weather-channel.sh
stat -c '%A %a %U:%G %n' /home/frost/bin/usb-audio-loop.sh
git ls-files --stage scripts/
```

Expected guidance:

- Python and shell scripts executed directly must be executable.
- System-level scripts under `/usr/local/bin` are normally owned by `root:root`.
- User-level scripts under `/home/frost` are normally owned by `frost`.
- Repository copies should preserve executable mode where appropriate.
- Service units belong in `systemd/` and should not be executable.

## Synchronizing Repository And Live Scripts

Always compare before copying in either direction. Do not blindly overwrite a newer repository version or a working live file.

Examples:

```bash
diff -u scripts/apple_gesture_button.py /usr/local/bin/apple_gesture_button.py
diff -u scripts/volume_knob.py /usr/local/bin/volume_knob.py
diff -u scripts/weather-channel.sh /home/frost/weather-channel/weather-channel.sh
diff -u scripts/usb-audio-loop.sh /home/frost/bin/usb-audio-loop.sh
```

When archiving a verified live script into the repository, preserve mode and timestamps:

```bash
cp --preserve=mode,timestamps \
  /home/frost/bin/usb-audio-loop.sh \
  scripts/usb-audio-loop.sh
```

For system-level scripts, copying back to the live Pi normally requires privileges and should preserve executable mode and ownership intentionally:

```bash
sudo install -o root -g root -m 755 \
  scripts/apple_gesture_button.py \
  /usr/local/bin/apple_gesture_button.py
```

After deploying a service-backed script, restart and verify the matching service:

```bash
sudo systemctl restart apple-gesture-button.service
sudo systemctl status apple-gesture-button.service --no-pager
```

For user services:

```bash
systemctl --user restart usb-audio-loop.service
systemctl --user status usb-audio-loop.service --no-pager
```

For launcher-backed scripts, relaunch from AtEase or the desktop launcher and confirm the expected process appears.

## Archiving Checklist

1. Find the live deployed file through systemd, `.desktop` launchers, or direct filesystem inspection.
2. Read the live file and confirm it contains no secrets, tokens, private keys, captured environment dumps, or unnecessary temporary paths.
3. Compare with any existing repository copy.
4. Copy the verified live file into `scripts/` with preserved mode and timestamps.
5. Run the relevant syntax check.
6. Update this README and any service documentation in [../systemd/README.md](../systemd/README.md).
7. Commit the script and documentation together.

## Related Documentation

- [Software inventory](../docs/software.md) documents the active software stack and detailed Apple-logo gesture behavior.
- [Live system audit](../docs/live-system-audit.md) is a dated historical snapshot, not the current source of truth.
- [Maintenance notes](../docs/maintenance.md) contain broader operational guidance and may include legitimate Nintendo 64 controller or emulation references.
- [systemd service notes](../systemd/README.md) document archived service units and useful `systemctl` commands.
