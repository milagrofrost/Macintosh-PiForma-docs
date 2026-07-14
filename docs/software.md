# Software

This document captures the Macintosh PiForma software stack as currently known.

The software is not trying to be a perfect clone of classic Mac OS. It is Raspberry Pi OS dressed up like a Mac OS 9 / At Ease / early internet fever dream.

## System

| Item | Value |
|---|---|
| Board | Raspberry Pi 4 Model B |
| RAM | 4GB |
| Storage | 256GB microSD |
| Hostname | `macintosh-piforma` |
| User | `frost` |
| OS | Raspberry Pi OS / Debian 13 Trixie-style Raspberry Pi desktop stack |
| Desktop | LXDE / Openbox / PCManFM desktop |
| Session | X11 |
| Display mode | 800x480 |

## Current graphical stack

The current live desktop is an X11 `rpd-x` session launched by LightDM. Openbox manages windows, PCManFM owns the desktop background, and PiForma Panel is the active top panel.

| Layer | Current implementation |
|---|---|
| Display manager | LightDM |
| Session | `rpd-x` / LXDE on X11 |
| Window manager | Openbox |
| Desktop background | PCManFM |
| Top panel | PiForma Panel |
| Launcher shell | AtEase |
| Dock / Control Strip | ControlStrip Simulator |
| Assistant | Clippy |
| Audio | PipeWire / WirePlumber |

LXPanel-pi and tint2 configuration files may still exist on the machine, but they are not the active top panel in the July 2026 live audit.

## Boot flow

Expected flow:

```text
Power switch on
  -> Anker battery output energizes 5V rail
  -> YS-M3 boot chime plays
  -> Raspberry Pi boots
  -> Plymouth splash
  -> RetroPie asplashscreen
  -> LightDM
  -> LXDE/Openbox desktop
  -> custom services start
```

## Desktop look

The desktop is intended to feel like a Mac OS 9-ish Raspberry Pi system.

Visual pieces:

- Mac OS 9 Platinum-style GTK theme
- Chicago-style font
- MoNine icons
- PiXflat as fallback
- At Ease inspired wallpaper
- Apple-menu-style top panel
- retro launchers

It is not macOS. It is Raspberry Pi OS wearing a thrift-store Macintosh costume, and honestly that is kind of the point.

## Important config paths

Known files and directories touched during the build:

```text
/boot/firmware/config.txt
/boot/config.txt
/etc/default/keyboard
/etc/xdg/lxsession/rpd-x/autostart
~/.config/openbox/rpd-rc.xml
~/.config/pcmanfm/LXDE-pi/desktop-items-0.conf
~/.config/lxpanel-pi/panels/panel
~/.local/share/piforma-panel/config.yaml
~/.local/share/control-strip/config.yaml
~/.local/share/atease/config.yaml
~/.local/share/atease/apps/
~/.local/share/atease/apps-2/
~/.config/SheepShaver/prefs
~/.sheepshaver_prefs
~/.asoundrc
~/weather-channel/
~/Desktop/
~/.icons/
~/.themes/
```

## Custom services

| Service | Scope | Purpose |
|---|---|---|
| `apple-gesture-button.service` | system | Handles Apple logo capacitive gestures |
| `volume-knob.service` | system | Handles EC11 volume knob |
| `atease.service` | system | Starts the AtEase launcher as user `frost` |
| `flyingtoasters.service` | system | Serves local Flying Toasters web build |
| `piforma-panel.service` | user | Starts PiForma Panel |
| `controlstrip-simulator.service` | user | Starts ControlStrip Simulator |
| `n64-audio-loop.service` | user | Optional external-input audio helper |

## Apple logo gesture button

Script:

```text
/usr/local/bin/apple_gesture_button.py
```

Service:

```text
apple-gesture-button.service
```

Hardware:

- TTP223 capacitive touch sensor
- mounted behind the Apple logo
- GPIO 23
- active-low
- uses `gpiozero`
- uses `LGPIOFactory`

Gesture mapping:

| Gesture | Action |
|---|---|
| 1 tap | Open Internet Explorer themed launcher |
| 2 taps | Open Mac OS 9 / SheepShaver |
| 3 taps | Open Winamp/QMMP style player |
| 4 taps | Open RetroPie / EmulationStation |
| Hold | Close active window |

The four-tap RetroPie gesture exists so the keyboard and mouse can stay packed when the only goal is playing games. Power on, plug in a controller, tap the Apple logo four times, and go.

The hold gesture works around the Nintendo 64 controller problem. The controller does not have a spare clean hotkey button, so holding the Apple logo closes the running game or exits EmulationStation.

## Volume knob

Script:

```text
/usr/local/bin/volume_knob.py
```

Service:

```text
volume-knob.service
```

Hardware:

- EC11 rotary encoder
- GPIO 17 and 27 for rotation
- GPIO 22 for push/mute support

Behavior:

- rotate clockwise: volume up
- rotate counterclockwise: volume down
- push-to-mute supported in software
- push-to-mute not physically usable in final hardware

## Audio stack

Normal output:

- PipeWire
- internal USB speaker
- speaker plugged directly into Raspberry Pi

Optional external audio:

- USB-to-3.5mm/RCA adapter can be used when RCA audio is needed

Previous experiments included MAX98357A I2S amplifier boards and other audio adapters. The final installed path is the internal USB speaker because it works.

## Included apps and launchers

Current visible launchers are managed by AtEase from `~/.local/share/atease/apps/` and `~/.local/share/atease/apps-2/`, not from `~/Desktop`.

| App / Feature | Role | Status |
|---|---|---|
| RetroPie / EmulationStation | games | primary practical use |
| Web browser | general use | primary practical use |
| SheepShaver / Mac OS 9 | classic Mac nostalgia | included |
| LinApple | Apple II emulation | dormant or pending confirmation |
| DOSBox-X / Windows 98 | retro Windows | experimental or pending confirmation |
| WeatherStar / Weather Channel kiosk | ambient retro weather | included |
| Flying Toasters | screensaver nostalgia | included |
| AOL simulator | early internet nostalgia | included |
| Netscape launcher | early internet nostalgia | included |
| Encarta | encyclopedia nostalgia | included |
| LimeWire | early internet nostalgia | included |
| Kid Pix | classic creative software | historical or pending confirmation |
| Winamp / QMMP style player | music nostalgia | included |

Some are practical. Some are there because the computer would feel wrong without them.

## Weather Channel kiosk

Known path:

```text
~/weather-channel/
```

Known files:

```text
weather-channel.sh
launch.html
satellite.png
```

The kiosk flow shows a satellite image first, then opens the WeatherStar web interface in Chromium kiosk/app mode.

## Suggested repo files

Copy the real live files from the Pi into the repo later.

Suggested scripts:

```text
scripts/apple_gesture_button.py
scripts/volume_knob.py
scripts/weather-channel.sh
scripts/n64-audio-loop.sh
scripts/center-display.sh
scripts/run_this.sh
```

Suggested systemd units:

```text
systemd/apple-gesture-button.service
systemd/volume-knob.service
systemd/atease.service
systemd/flyingtoasters.service
systemd/user/piforma-panel.service
systemd/user/controlstrip-simulator.service
systemd/user/n64-audio-loop.service
```

Suggested config snapshots:

```text
config/boot/firmware/config.txt
config/openbox/rpd-rc.xml
config/piforma-panel/config.yaml
config/control-strip/config.yaml
config/atease/config.yaml
config/atease/apps/
config/atease/apps-2/
config/lxpanel-pi/panel
config/pcmanfm/desktop-items-0.conf
config/lxsession/autostart
config/sheepshaver/prefs
config/asoundrc
```
