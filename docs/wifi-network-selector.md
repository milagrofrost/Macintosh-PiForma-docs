# Wi-Fi Network Selector (Openbox / NetworkManager)

## Status

Added October 20, 2026. Tested interactively on the live PiForma using `wlan0`; end-to-end connection to a *new* SSID and passwordless desktop launching have **not yet been verified**.

PiForma uses Openbox with its own top panel rather than a conventional notification-area/system tray. `nm-applet` is therefore not a suitable standalone wireless picker. The chosen approach is [networkmanager-dmenu](https://github.com/firecat53/networkmanager-dmenu) with [Rofi](https://github.com/davatorium/rofi). It presents nearby wireless SSIDs as a searchable menu and delegates connections to NetworkManager.

## Requirements and installation

NetworkManager must already be managing `wlan0`:

```bash
nmcli device status
nmcli general permissions
```

Install the launcher and its dependencies:

```bash
sudo apt update
sudo apt install rofi python3-gi gir1.2-nm-1.0 git
git clone https://github.com/firecat53/networkmanager-dmenu.git
cd networkmanager-dmenu
sudo install -m 755 networkmanager_dmenu /usr/local/bin/networkmanager_dmenu
```

If using an existing clone, skip the `git clone` step. Launch from a terminal **within the graphical X11/Openbox session**, not from a separate text console:

```bash
networkmanager_dmenu
```

Configuration file used on PiForma: `~/.config/networkmanager-dmenu/config.ini`. Confirmed settings:

```ini
[dmenu]
dmenu_command = rofi
compact = False
list_saved = False
prompt = Networks

[nmdm]
rescan_delay = 5
notification_timeout = 5
show_notifications = True
```

`list_saved = False` **does not hide unknown access points**. Saved connections appear separately. If the system lacks a notification daemon, setting `show_notifications = False` avoids desktop-notification errors without altering scan behavior.

## Critical detail: refresh scan results *before* opening

On the live PiForma, an initial `networkmanager_dmenu` launch showed only the connected `Green Ice` SSID, even though `nmcli` and the Python NetworkManager API could see nearby networks.

A forced scan followed by a five-second delay corrected the list. The menu then showed `Green Ice`, `AIRPLAY-1E552F`, `Green Ice Backup`, and an empty/unnamed SSID. The specific reason for the initially incomplete API snapshot is unconfirmed; it is **not** evidence of broken duplicate-SSID filtering or a second Wi-Fi adapter.

```bash
sudo nmcli device wifi rescan ifname wlan0
sleep 5
nmcli -f IN-USE,SSID,SIGNAL,SECURITY device wifi list ifname wlan0 --rescan no
networkmanager_dmenu
```

NetworkManager may report different nearby APs on consecutive scans as radio conditions change. The app intentionally reduces multiple access points broadcasting the same SSID to one menu entry.

## Convenience launcher

A wrapper at `/usr/local/bin/piforma-wifi` was proposed so PiForma can open a freshly populated menu:

```bash
sudo tee /usr/local/bin/piforma-wifi >/dev/null <<'EOF'
#!/bin/bash
sudo nmcli device wifi rescan ifname wlan0
sleep 5
exec networkmanager_dmenu
EOF
sudo chmod +x /usr/local/bin/piforma-wifi
```

Run it with:

```bash
piforma-wifi
```

**Permission caveat:** The first version of this wrapper used `nmcli device wifi rescan` without `sudo` and failed with:

```text
Error: org.freedesktop.NetworkManager.wifi.scan request failed: not authorized.
```

The revised wrapper uses `sudo` **only for scanning**, not for the graphical application. It may need a sudo password at an interactive terminal and is **not yet suitable for an unattended desktop icon**. Do not run Rofi/NetworkManager-dmenu as root. Do not grant blanket passwordless sudo or broad NetworkManager configuration rights simply to make scanning work.

For seamless desktop integration, verify:

```bash
nmcli general permissions
loginctl session-status
```

Then establish a functioning active desktop session / Polkit authorization or a narrowly scoped scan-only authorization, and test it before replacing the interactive workaround. The exact rule has not been validated on PiForma.

## Troubleshooting

```bash
nmcli device status
nmcli -f IN-USE,SSID,SIGNAL,SECURITY device wifi list --rescan yes
echo "Desktop: $XDG_CURRENT_DESKTOP"
echo "Session: $DESKTOP_SESSION"
echo "Session type: $XDG_SESSION_TYPE"
ps -e -o comm= | grep -E 'openbox|labwc|wayfire|xfwm4'
```

The session reported `XDG_SESSION_TYPE=tty` and an Openbox process during troubleshooting. The empty desktop-related environment variables do not mean Openbox is absent.

To inspect the very same access points visible through the NetworkManager Python API:

```bash
/usr/bin/python3 - <<'PY'
import gi
gi.require_version("NM", "1.0")
from gi.repository import NM

client = NM.Client.new(None)
for device in client.get_devices():
    if device.get_device_type() == NM.DeviceType.WIFI:
        print("Wi-Fi adapter:", device.get_iface())
        for ap in device.get_access_points():
            ssid = ap.get_ssid()
            name = NM.utils_ssid_to_utf8(ssid.get_data()) if ssid else "<hidden>"
            print(f"  {name}: {ap.get_strength()}%")
PY
```

Rofi's `Networks: Type to filter` prompt filters the list, and the `15/15` counter includes actions, not necessarily 15 discovered SSIDs.

## Follow-up integration work

- Verify the `sudo` rescan wrapper works in a terminal and that passwords can be supplied to connect to a new SSID.
- Resolve scanning authorization so a PiForma desktop icon can launch the picker without a terminal or elevation prompt.
- Create an At Ease / PiForma Panel **Wireless Networks** launcher targeting `piforma-wifi`.
- Optionally replace the Rofi presentation with a classic Mac OS-style GTK selector while retaining NetworkManager as the backend.
