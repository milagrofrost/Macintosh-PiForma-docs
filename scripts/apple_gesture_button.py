#!/usr/bin/env python3
import os
import re
import shlex
import time
import subprocess
import threading
from typing import Callable, Dict, Optional, List

from gpiozero import Device, Button
from gpiozero.pins.lgpio import LGPIOFactory

Device.pin_factory = LGPIOFactory()

GPIO_PIN = 23

# Tap behavior
MULTITAP_WINDOW_S = 0.70
BOUNCE_S = 0.05

# Hold thresholds (seconds)
HOLD_CLOSE_ACTIVE_S = 2.0     # 2 to 3 seconds closes top window
HOLD_CLOSE_ALL_S = 6.0        # 6 to 10 seconds closes everything and shows desktop
HOLD_SHUTDOWN_S = 10.0        # 10+ seconds powers off

# Path to your desktop entries
DESKTOP_DIR = "/home/frost/Desktop"
DESKTOP_MAP = {
    1: f"{DESKTOP_DIR}/Chromium-70.desktop",
    2: f"{DESKTOP_DIR}/MacOS9.desktop",
    3: f"{DESKTOP_DIR}/Winamp.desktop",
    4: f"{DESKTOP_DIR}/Retropie.desktop",
}

def log(msg: str) -> None:
    print(msg, flush=True)

def run_bg(argv: List[str], env: Optional[dict] = None) -> None:
    subprocess.Popen(argv, env=env or os.environ.copy())

def run_capture(argv: List[str], env: Optional[dict] = None) -> subprocess.CompletedProcess:
    return subprocess.run(argv, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=env)

def x_env() -> dict:
    env = os.environ.copy()
    env.setdefault("HOME", "/home/frost")
    env.setdefault("DISPLAY", ":0")
    env.setdefault("XAUTHORITY", "/home/frost/.Xauthority")
    env.setdefault("XDG_RUNTIME_DIR", "/run/user/1000")
    env.setdefault("DBUS_SESSION_BUS_ADDRESS", "unix:path=/run/user/1000/bus")
    return env

def parse_desktop_exec(desktop_file: str) -> Optional[List[str]]:
    if not os.path.exists(desktop_file):
        log(f"Desktop file not found: {desktop_file}")
        return None

    exec_line = None
    in_desktop_entry = False

    with open(desktop_file, "r", encoding="utf-8", errors="ignore") as f:
        for raw in f:
            line = raw.strip()
            if line.startswith("[") and line.endswith("]"):
                in_desktop_entry = (line == "[Desktop Entry]")
                continue
            if not in_desktop_entry:
                continue
            if line.startswith("Exec="):
                exec_line = line[len("Exec="):].strip()
                break

    if not exec_line:
        log(f"No Exec= found in {desktop_file}")
        return None

    # Remove desktop placeholders like %U, %u, %F, %f, etc.
    exec_line = re.sub(r"\s%[fFuUdDnNickvm]", "", exec_line).strip()

    try:
        return shlex.split(exec_line)
    except Exception as e:
        log(f"Failed to parse Exec line in {desktop_file}: {e}")
        return None

def launch_desktop(desktop_file: str) -> None:
    argv = parse_desktop_exec(desktop_file)
    if not argv:
        return
    log(f"Launching from {os.path.basename(desktop_file)}: {' '.join(argv)}")
    run_bg(argv, env=x_env())

def close_active_window() -> None:
    env = x_env()
    # Close the currently active window
    run_bg(["wmctrl", "-c", ":ACTIVE:"], env=env)

def show_desktop() -> None:
    env = x_env()
    # Try EWMH show-desktop
    r = run_capture(["wmctrl", "-k", "on"], env=env)
    if r.returncode == 0:
        return
    # Fallback: Super+D if xdotool exists
    if subprocess.call(["which", "xdotool"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0:
        run_bg(["xdotool", "key", "super+d"], env=env)

def close_all_windows() -> None:
    env = x_env()
    r = run_capture(["wmctrl", "-l"], env=env)
    if r.returncode != 0:
        log("wmctrl -l failed, cannot close all windows")
        return

    # Lines look like: 0x03a00007  0 host Window Title
    window_ids = []
    for line in r.stdout.splitlines():
        parts = line.split()
        if parts and parts[0].startswith("0x"):
            window_ids.append(parts[0])

    for wid in window_ids:
        # -i means use the hex window id
        run_bg(["wmctrl", "-i", "-c", wid], env=env)

def shutdown_pi() -> None:
    # This will require permissions. See sudoers note below.
    log("Shutdown requested (hold >= 10s)")
    run_bg(["sudo", "/bin/systemctl", "poweroff"])

class GestureButton:
    def __init__(self, pin: int):
        self.btn = Button(pin, pull_up=True, bounce_time=BOUNCE_S)

        self._tap_count = 0
        self._tap_timer: Optional[threading.Timer] = None

        self._pressed_at: Optional[float] = None
        self._hold_consumed = False

        self.btn.when_pressed = self._on_pressed
        self.btn.when_released = self._on_released

    def _on_pressed(self) -> None:
        self._pressed_at = time.time()
        self._hold_consumed = False

    def _on_released(self) -> None:
        if self._pressed_at is None:
            return

        held_s = time.time() - self._pressed_at
        self._pressed_at = None

        # Holds override taps
        if held_s >= HOLD_SHUTDOWN_S:
            self._cancel_taps()
            self._hold_consumed = True
            shutdown_pi()
            return

        if held_s >= HOLD_CLOSE_ALL_S:
            self._cancel_taps()
            self._hold_consumed = True
            log("Hold action: close all windows and show desktop")
            close_all_windows()
            show_desktop()
            return

        if held_s >= HOLD_CLOSE_ACTIVE_S:
            self._cancel_taps()
            self._hold_consumed = True
            log("Hold action: close active window")
            close_active_window()
            return

        # Short press counts as a tap
        self._tap_count += 1
        self._restart_tap_timer()

    def _restart_tap_timer(self) -> None:
        if self._tap_timer:
            self._tap_timer.cancel()
        self._tap_timer = threading.Timer(MULTITAP_WINDOW_S, self._finalize_taps)
        self._tap_timer.daemon = True
        self._tap_timer.start()

    def _cancel_taps(self) -> None:
        self._tap_count = 0
        if self._tap_timer:
            self._tap_timer.cancel()
            self._tap_timer = None

    def _finalize_taps(self) -> None:
        taps = self._tap_count
        self._tap_count = 0

        desktop_file = DESKTOP_MAP.get(taps)
        if desktop_file:
            log(f"Tap action: {taps} tap(s)")
            launch_desktop(desktop_file)
        else:
            log(f"{taps} tap(s): no action mapped")

def main() -> None:
    # Prevent lgpio notify file weirdness under systemd
    os.chdir("/home/frost")

    log(f"Apple logo gesture button active on GPIO {GPIO_PIN}")
    log("Tap map: 1=Chromium, 2=MacOS9, 3=Winamp, 4=RetroPie")
    log("Hold: 2s close active, 6s close all + desktop, 10s shutdown")

    GestureButton(GPIO_PIN)

    while True:
        time.sleep(60)

if __name__ == "__main__":
    main()
