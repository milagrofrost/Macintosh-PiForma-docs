# Config Files

Copy relevant live configuration here.

Suggested layout:

```text
config/
├── boot/
│   └── firmware/
│       └── config.txt
├── openbox/
│   └── rpd-rc.xml
├── piforma-panel/
│   └── config.yaml
├── control-strip/
│   ├── config.yaml
│   └── window-check.sh
├── atease/
│   ├── config.yaml
│   ├── apps/
│   └── apps-2/
├── lxpanel-pi/
│   └── panel  # historical/fallback unless reactivated
├── pcmanfm/
│   └── desktop-items-0.conf
├── lxsession/
│   └── autostart
├── sheepshaver/
│   └── prefs
└── asoundrc
```

Useful source paths:

```text
/boot/firmware/config.txt
~/.config/openbox/rpd-rc.xml
~/.local/share/piforma-panel/config.yaml
~/.local/share/control-strip/config.yaml
~/.local/share/control-strip/scripts/window-check.sh
~/.local/share/atease/config.yaml
~/.local/share/atease/apps/
~/.local/share/atease/apps-2/
~/.config/lxpanel-pi/panels/panel
~/.config/pcmanfm/LXDE-pi/desktop-items-0.conf
/etc/xdg/lxsession/rpd-x/autostart
~/.config/SheepShaver/prefs
~/.asoundrc
```
