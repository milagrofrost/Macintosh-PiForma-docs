# Cleanup and Archival Plan

This is not a delete list. This is a make-it-recoverable-first list.

The live audit found a bunch of old scripts, logs, installers, theme experiments, and backups. That is normal. PiForma has been a real build, and real builds leave sawdust.

The rule:

> Archive first. Delete later. Regret never.

## Source of truth files

These should be copied into this repo before any cleanup happens.

### Gesture and volume

```text
/usr/local/bin/apple_gesture_button.py
/usr/local/bin/volume_knob.py
/etc/systemd/system/apple-gesture-button.service
/etc/systemd/system/volume-knob.service
```

Why:

- the deployed gesture script is in `/usr/local/bin`, not the older home-directory placeholder
- the deployed volume script is in `/usr/local/bin`
- these are core hardware features, not optional experiments

### AtEase

```text
/etc/systemd/system/atease.service
~/.config/atease/config.yaml
~/.local/share/atease/
/usr/share/applications/AtEase.desktop
```

Why:

AtEase is now part of the finished experience. Its config should be preserved with the build docs.

### ControlStrip Simulator

```text
~/.config/systemd/user/controlstrip-simulator.service
~/.local/share/control-strip/config.yaml
/usr/share/applications/ControlStrip Simulator.desktop
```

Why:

The Control Strip depends on X11 window matching and app config. That config is easy to lose and annoying to recreate.

### Desktop and theme

```text
~/.config/lxpanel-pi/panels/panel
~/.config/openbox/rpd-rc.xml
~/.config/pcmanfm/LXDE-pi/desktop-items-0.conf
~/.config/gtk-3.0/settings.ini
~/.icons/
~/.themes/
~/theme-lab/
```

Why:

The look is not one file. It is a pile of theme, panel, icon, font, and Openbox details that together make the illusion work.

### Boot and display

```text
/boot/firmware/config.txt
/boot/firmware/cmdline.txt
```

Why:

Display mode, HDMI hotplug, overscan, Plymouth behavior, and audio settings live here.

### Weather Channel

```text
~/weather-channel/weather-channel.sh
~/weather-channel/launch.html
~/weather-channel/satellite.png
```

Why:

This is a complete little subsystem and should be preserved as such.

## Safe-ish archive candidates

These are probably safe to move into an archive folder after the current live versions are copied into the repo.

### Superseded scripts

```text
~/apple_gesture_button.py
~/volume_control.py
~/volume_control2.py
/usr/local/bin/volume_knob.py_old
~/gpio_test.py
~/gpio_test2.py
~/gpio_test3.py
~/gpio_test4.py
~/gpio_test5.py
~/find_gpio.py
```

Notes:

- `~/apple_gesture_button.py` is an older placeholder
- GPIO discovery scripts were useful during the build, but not needed at runtime
- keep them only if you want the archaeology

### Logs and old Wayland attempt files

```text
~/weston.log
~/weston-tty2.log
~/plymouth.log
~/nested.log
```

Notes:

The current system is X11, not Weston/Wayland. These are probably old investigation artifacts.

### Old installers and archives

```text
~/master.zip
~/169365-Mac Classic Platinum.zip
~/linamp_1.4.0_arm64.deb
```

Notes:

Preserve if needed. Delete once replacements are in the repo or easy to redownload.

### Old audit package

```text
~/piforma-audit-20260621-113244/
~/piforma-audit-20260621-113244.zip
```

Notes:

Archive externally if desired. Once the useful audit findings are in this repo, the giant package does not need to live in `$HOME` forever.

## Do not delete without checking

The audit specifically called out these as referenced/live:

```text
~/toggle-panel.sh
~/xdg.sh
```

Also do not delete:

```text
/usr/local/bin/apple_gesture_button.py
/usr/local/bin/volume_knob.py
~/weather-channel/
~/.local/share/flyingtoasters/build
~/.config/atease/config.yaml
~/.local/share/control-strip/config.yaml
```

## Suggested cleanup workflow

1. Create a local archive folder:

```bash
mkdir -p ~/piforma-archive/2026-07-cleanup
```

2. Copy, do not move, live source-of-truth files into the repo checkout.

3. Commit the repo.

4. Move old candidates into the archive folder.

5. Reboot.

6. Test:

```text
Apple logo 1/2/3/4 taps
Apple logo hold
volume knob
AtEase service
ControlStrip service
Weather Channel launcher
Flying Toasters launcher
RetroPie launcher
boot chime
```

7. If everything works, zip the archive folder and move it off the Pi.

## The goal

The goal is not to make `$HOME` spotless.

The goal is to make Macintosh PiForma reproducible, maintainable, and less haunted.
