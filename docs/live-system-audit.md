# Live System Audit Summary

This page summarizes the live PiForma software audit generated on 2026-06-23 and revised on 2026-07-05 with the newer apps and theme work.

The audit matters because it captures what is actually running on the machine, not just what the build was supposed to be.

## Machine identity

| Item | Value |
|---|---|
| Hostname | `macintosh-piforma` |
| Primary user | `frost` |
| Board | Raspberry Pi 4 Model B, Rev 1.1 |
| OS base | Debian 13 / Trixie-style Raspberry Pi desktop stack |
| Session | X11, `rpd-x` |
| Window manager | Openbox |
| Display manager | LightDM |

## Active custom services

| Service | State | Purpose |
|---|---|---|
| `apple-gesture-button.service` | enabled, active | reads the Apple logo capacitive touch sensor on GPIO 23 and maps taps/holds to app launches and window actions |
| `atease.service` | enabled, active | starts the AtEase Tauri launcher shell at graphical target |
| `controlstrip-simulator.service` | enabled, active user unit | runs the Control Strip-style dock as a per-user graphical-session service |
| `flyingtoasters.service` | enabled, active | serves the local After Dark Flying Toasters web build on localhost port 3000 |
| `volume-knob.service` | enabled, active | reads the EC11 rotary encoder and controls PipeWire volume through `pactl` |
| `asplashscreen.service` | enabled, active oneshot | RetroPie VLC boot splash |

## Stock services worth knowing about

Running stock services include:

- LightDM
- NetworkManager
- wpa_supplicant
- PipeWire / WirePlumber
- Bluetooth
- CUPS
- Avahi
- cron
- ssh
- systemd-timesyncd

`pigpiod` is installed but inactive. The final GPIO scripts use `gpiozero` with `lgpio`, not pigpio.

`wayvnc-control.service` exists but is inactive because the system is using X11, not Wayland.

## Startup sequence

```text
Power on
  -> firmware reads /boot/firmware/config.txt
  -> kernel starts with quiet splash and Plymouth
  -> asplashscreen.service runs RetroPie VLC splash
  -> multi-user.target starts networking and support services
  -> graphical.target starts LightDM
  -> user frost enters rpd-x LXDE/Openbox session
  -> lxpanel-pi, pcmanfm-pi, xscreensaver start
  -> custom graphical services start
```

Boot splash chain:

```text
Plymouth pix theme -> RetroPie asplashscreen -> LightDM -> desktop
```

Mac-style Plymouth themes are installed but not currently selected.

## GPIO integrations

| BCM pin | Hardware | Service | Function |
|---|---|---|---|
| GPIO 23 | capacitive touch pad behind Apple logo | `apple-gesture-button.service` | multi-tap and hold gestures |
| GPIO 17 | rotary encoder A | `volume-knob.service` | volume control |
| GPIO 27 | rotary encoder B | `volume-knob.service` | volume control |
| GPIO 22 | rotary encoder push | `volume-knob.service` | mute toggle in software |

All final GPIO code uses BCM numbering and `LGPIOFactory`.

## Apple logo gesture map

The deployed script lives at:

```text
/usr/local/bin/apple_gesture_button.py
```

The older copy at `~/apple_gesture_button.py` is a stale placeholder and should not be treated as source of truth.

Live gesture behavior:

| Gesture | Action |
|---|---|
| 1 tap | Chromium/Netscape style launcher |
| 2 taps | Mac OS 9 / SheepShaver |
| 3 taps | Winamp / QMMP |
| 4 taps | RetroPie / EmulationStation |
| hold 2 seconds | close active window |
| hold 6 seconds | close all windows and show desktop |
| hold 10 seconds | power off |

## Volume knob

The deployed script lives at:

```text
/usr/local/bin/volume_knob.py
```

It uses:

```text
RotaryEncoder(17, 27)
Button(22)
```

Each detent changes `@DEFAULT_SINK@` by roughly 2 percent through `pactl`.

Older scripts like `volume_control.py`, `volume_control2.py`, and `volume_knob.py_old` are superseded.

## Desktop theme state

Active visual stack:

| Area | Current choice |
|---|---|
| GTK theme | `Mac-OS-9-Platinum-Default` |
| Icons | `MoNine` |
| Cursor | `retrosmart-xcursor-black-color-shadow` |
| Font | `ChicagoFLF Medium 7` |
| Wallpaper | `~/atease-1.png` |
| Panel | `lxpanel-pi`, top Mac-style menu bar |

Additional PiForma theme work exists in:

```text
~/.themes/PiForma-Platinum9-Classic
~/.themes/PiForma-PlatiPlus
~/.themes/PiForma-PlatiPlus26
~/.icons/PiForma-NineIcons
~/theme-lab/
```

## Desktop launchers

| Launcher | Backing app |
|---|---|
| Netscape | Chromium |
| America Online | Chromium kiosk to web AOL simulator |
| Encarta | Kiwix |
| Flying Toasters | Chromium kiosk to localhost:3000 |
| Kid Pix | Tux Paint |
| Macintosh HD | PCManFM home folder |
| Mac OS 9 | SheepShaver AppImage |
| RetroPie | EmulationStation |
| Winamp | QMMP |
| Weather Channel | local Weather Channel script |
| Terminal | LXTerminal |

## Weather Channel flow

```text
Desktop Weather Channel launcher
  -> ~/weather-channel/weather-channel.sh
  -> pkill chromium
  -> chromium kiosk fullscreen
  -> file:///home/frost/weather-channel/launch.html
  -> satellite.png splash for 3 seconds
  -> WeatherStar web emulator
```

Files:

```text
~/weather-channel/weather-channel.sh
~/weather-channel/launch.html
~/weather-channel/satellite.png
```

## Audio state

The live audit found PipeWire, WirePlumber, and `pipewire-pulse` active.

Known sinks include:

- GEMBIRD USB DAC, default output
- onboard 3.5mm audio
- HDMI audio

The volume knob controls `@DEFAULT_SINK@` through `pactl`.

There is also an `n64-audio-loop.sh` helper that watches for a C-Media USB capture device and can loop console audio through the speakers when connected.

## Newer post-audit apps

The 2026-07-05 revision added the newer apps:

| App | Path | Purpose |
|---|---|---|
| AtEase | `~/atEase/` | fullscreen At Ease-style launcher shell |
| ControlStrip Simulator | `~/controlstrip-simualtor/` | transparent Mac-style Control Strip dock |
| Clippy | `~/clippy-rpi/` | local retro assistant |
| About This PiForma | `~/about-my-piforma/about-piforma-tauri/` | About This Mac-style info window |

Note the misspelling in the local ControlStrip directory: `controlstrip-simualtor`.

## Cleanup candidates

The audit identified old scripts, logs, and backups that can likely be archived once the live paths are copied into this repo.

Do not delete these without checking:

- `~/toggle-panel.sh`, still referenced
- `~/xdg.sh`, still referenced
- `/usr/local/bin/apple_gesture_button.py`, live source of truth
- `/usr/local/bin/volume_knob.py`, live source of truth

Good cleanup targets after review:

- old GPIO discovery scripts
- older home-directory placeholder gesture scripts
- old volume control iterations
- stale Weston logs
- old theme zip archives
- audit zip packages after they are preserved

## Best next archival step

Copy these from the Pi into this repo:

```text
/usr/local/bin/apple_gesture_button.py
/usr/local/bin/volume_knob.py
/etc/systemd/system/apple-gesture-button.service
/etc/systemd/system/volume-knob.service
/etc/systemd/system/atease.service
~/.config/systemd/user/controlstrip-simulator.service
~/.config/lxpanel-pi/panels/panel
~/.config/openbox/rpd-rc.xml
~/.config/gtk-3.0/settings.ini
/boot/firmware/config.txt
~/weather-channel/
```

That is the difference between documentation and recoverability.
