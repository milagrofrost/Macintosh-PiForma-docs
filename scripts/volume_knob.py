#!/usr/bin/env python3

from gpiozero import Device, RotaryEncoder, Button
from gpiozero.pins.lgpio import LGPIOFactory
from signal import pause
import subprocess
import time
import re

Device.pin_factory = LGPIOFactory()

# GPIO pins (BCM numbering)
A = 17
B = 27
SW = 22

# Tuning
STEP_PERCENT = 2
DEBOUNCE_S = 0.01
MIN_SET_INTERVAL_S = 0.05  # max 20 updates/sec

SINK = "@DEFAULT_SINK@"  # PipeWire/Pulse default sink

def run_cmd(args):
    return subprocess.run(
        args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )

def get_volume_percent():
    # Example output includes percentages like "  50% "
    r = run_cmd(["pactl", "get-sink-volume", SINK])
    m = re.search(r"(\d+)%", r.stdout)
    return int(m.group(1)) if m else 50

def set_volume_percent(vol):
    # Clamp to 0-100. Change 100 to 150 if you want "overdrive" volume.
    vol = max(0, min(100, vol))
    run_cmd(["pactl", "set-sink-volume", SINK, f"{vol}%"])
    return vol

def toggle_mute():
    run_cmd(["pactl", "set-sink-mute", SINK, "toggle"])

enc = RotaryEncoder(A, B, max_steps=0)
btn = Button(SW, pull_up=True, bounce_time=0.15)

current_volume = get_volume_percent()
print(f"Start volume: {current_volume}% (sink={SINK})")

last_steps = enc.steps
last_event = 0.0
last_set = 0.0

def on_rotate():
    global last_steps, last_event, current_volume, last_set

    now = time.time()
    if now - last_event < DEBOUNCE_S:
        return
    last_event = now

    steps = enc.steps
    delta = steps - last_steps
    if delta == 0:
        return
    last_steps = steps

    if now - last_set < MIN_SET_INTERVAL_S:
        return

    if delta > 0:
        current_volume = min(100, current_volume + STEP_PERCENT)
    else:
        current_volume = max(0, current_volume - STEP_PERCENT)

    set_volume_percent(current_volume)
    last_set = now
    print(f"Volume: {current_volume}%")

def on_press():
    toggle_mute()
    print("Mute toggled")

enc.when_rotated = on_rotate
btn.when_pressed = on_press

print("Volume knob active. Ctrl+C to exit.")
pause()
