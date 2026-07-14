# systemd Services

Copy live unit files here.

Recommended files:

```text
apple-gesture-button.service
volume-knob.service
atease.service
flyingtoasters.service
user/piforma-panel.service
user/controlstrip-simulator.service
user/n64-audio-loop.service
```

Useful commands on the Pi:

```bash
systemctl cat apple-gesture-button.service
systemctl cat volume-knob.service
systemctl cat atease.service
systemctl cat flyingtoasters.service
systemctl --user cat piforma-panel.service
systemctl --user cat controlstrip-simulator.service
systemctl --user cat n64-audio-loop.service
```
