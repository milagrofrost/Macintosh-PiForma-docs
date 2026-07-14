# Software Ecosystem

Macintosh PiForma is not just a Raspberry Pi in a monitor shell. The software stack is what makes it feel like a machine instead of a parts bin.

The hardware gives it a body. The software gives it a personality.

## The desktop illusion

The live system is a Raspberry Pi 4 Model B running a Raspberry Pi OS / Debian 13 Trixie-style desktop stack on X11. The shell is built around LightDM, LXDE, Openbox, PCManFM, PiForma Panel, AtEase, ControlStrip Simulator, PipeWire, and a pile of intentionally nostalgic launchers.

The point is not to fake macOS perfectly. The point is to make a Raspberry Pi behave like a computer that fell out of a late-90s Apple fever dream.

Core pieces:

| Layer | Role |
|---|---|
| LightDM | graphical login |
| rpd-x / LXDE | session environment |
| Openbox | window manager |
| PiForma Panel | active Mac-style top menu bar |
| PCManFM | desktop background and file-manager integration |
| AtEase | At Ease-style launcher surface |
| ControlStrip Simulator | bottom-left dock and app focus helper |
| PipeWire / WirePlumber | audio |
| systemd | boots custom services into the graphical target |

## Custom apps in the PiForma family

These are the companion apps that turned the desktop from a theme into an ecosystem.

| App | Repo | Role |
|---|---|---|
| PiForma Panel | https://github.com/milagrofrost/piforma-panel | active Macintosh-style top panel and menu bar |
| AtEase Simulator | https://github.com/milagrofrost/AtEase-simulator | full-screen At Ease-style launcher shell |
| ControlStrip Simulator | https://github.com/milagrofrost/ControlStrip-Simulator | transparent Mac OS-style Control Strip dock |
| About This PiForma | https://github.com/milagrofrost/about-this-pi | About This Mac-style system window for the build |
| Clippy PiForma fork | https://github.com/milagrofrost/clippy-rpi | retro desktop assistant, forked from Felix Rieseberg's Clippy |
| Flight of the Toasters | https://github.com/milagrofrost/Flight-of-the-Toasters | local Flying Toasters web app used by the launcher |
| Macintosh PiForma docs | https://github.com/milagrofrost/Macintosh-PiForma-docs | build documentation, BOM, wiring, lore, and maintenance notes |

## AtEase Simulator

AtEase is the main retro launcher shell.

It is a Tauri app modeled after Apple's At Ease experience. It shows tabbed pseudo-folders full of big beveled launcher buttons. Each item launches a configured `.desktop` file rather than letting the front end run arbitrary shell commands.

Known installed paths from the live audit:

```text
/usr/bin/atease
/usr/share/applications/AtEase.desktop
~/.local/share/atease/config.yaml
~/.local/share/atease/apps/
~/.local/share/atease/apps-2/
~/.local/share/atease/
```

Service:

```text
atease.service
```

The current live config renders at x=77, y=0, width=656, height=480. It starts on the main At Ease Items folder and also defines a second `sites` folder backed by `~/.local/share/atease/apps-2/`.

This is the part that makes PiForma feel less like a Linux desktop and more like a kid-safe restoration CD from an alternate Apple timeline.

## ControlStrip Simulator

ControlStrip Simulator is the dock-like utility strip.

It is a Tauri app that runs as a frameless transparent window under X11. It reads pinned apps from YAML, detects visible windows using X11 tooling, marks running apps, and launches or focuses them.

Known installed paths from the live audit:

```text
/usr/bin/controlstrip-simulator
/usr/share/applications/ControlStrip Simulator.desktop
~/.local/share/control-strip/config.yaml
```

Service:

```text
controlstrip-simulator.service
```

The live config pins Chromium/Netscape, LXTerminal, and PCManFM. It detects running windows with X11 tooling and focuses windows through `wmctrl`. Wayland is not the target right now.

## About This PiForma

About This PiForma is the machine's little brag window, except it is not really bragging. It is the classic About This Mac format translated into PiForma language.

Instead of pretending to be a real Mac, it reports the things that make sense for this build:

- PiForma name and version
- Raspberry Pi model
- memory
- swap
- running apps
- OS/system details

Repo:

```text
https://github.com/milagrofrost/about-this-pi
```

## Clippy

Clippy is not Mac at all, which is why it is funny.

It is Felix Rieseberg's Clippy idea pushed into the PiForma world as a retro desktop assistant. It runs locally and gives the machine that late-90s software-toy energy.

Installed paths from the audit:

```text
/usr/bin/clippy
/usr/lib/clippy/Clippy
~/.config/autostart/clippy.desktop
```

Repo:

```text
https://github.com/milagrofrost/clippy-rpi
```

## The launcher set

The AtEase launcher set is intentionally a little ridiculous.

| Launcher | Actually runs |
|---|---|
| Netscape | Chromium with scaling |
| America Online | Chromium kiosk to a web AOL simulator |
| Encarta | Kiwix |
| Flying Toasters | Chromium kiosk to local web server |
| LimeWire | Chromium kiosk launcher |
| Macintosh HD | PCManFM home folder |
| Mac OS 9 | SheepShaver AppImage |
| RetroPie | EmulationStation in LXTerminal |
| Winamp | QMMP |
| Weather Channel | local Weather Channel launcher script |
| Terminal | LXTerminal |

Kid Pix, LinApple, DOSBox-X, Windows 98, and Tux Paint should be documented as historical, dormant, or pending owner confirmation until they have current launchers in the live AtEase folders.

This is not about historical purity. It is about making the machine fun to touch.

## Apple logo gestures

The front Apple logo is not just decorative. It is a capacitive gesture button.

| Gesture | Action |
|---|---|
| 1 tap | Open Internet Explorer / Netscape-style browser launcher |
| 2 taps | Open Mac OS 9 / SheepShaver |
| 3 taps | Open Winamp / QMMP |
| 4 taps | Open RetroPie / EmulationStation |
| hold 2 seconds | close active window |
| hold 6 seconds | close all windows and show desktop |
| hold 10 seconds | power off |

This is one of the most important usability details in the whole build. It lets the machine work as a game station without needing to pull out the keyboard and mouse.

## Weather Channel subsystem

The Weather Channel launcher recreates a cable-TV WeatherStar style flow.

```text
~/weather-channel/weather-channel.sh
  -> pkill chromium
  -> chromium kiosk
  -> local launch.html
  -> satellite.png splash
  -> weatherstar.netbymatt.com kiosk mode
```

It is one of those features that sounds optional until you see it running. Then it becomes obvious why it belongs here.

## Audio behavior

The system uses PipeWire and WirePlumber with a USB audio device as the default output.

The physical volume knob changes `@DEFAULT_SINK@` through `pactl`. The boot chime is separate and plays through the YS-M3 module and its own salvaged laptop speaker.

That split matters:

- boot chime is part of the machine's power-on personality
- USB speaker is normal operating audio
- optional USB-to-RCA adapter handles external RCA audio needs

## The important part

The software is not just a skin. It is how the machine becomes usable.

The Apple logo launches apps. The Control Strip gives it a living dock. AtEase makes it feel approachable. The boot chime gives it ceremony. The AtEase launcher set makes it silly in the right way.

That is the difference between a Raspberry Pi project and Macintosh PiForma.
