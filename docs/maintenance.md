# Maintenance

This is the future-me-forgot-how-this-worked page.

## Opening the case

Be careful with:

- LCD ribbon cable
- HDMI ribbon path
- wires to rear source switch
- wires to boot chime selector
- power rail JST plugs
- Apple logo touch sensor wiring

The display ribbon is the most delicate final-build item. Do not let it flop around.

## Display problems

Symptoms:

- weird lines
- flicker
- image distortion
- display cuts in and out

Check:

1. LCD ribbon seating
2. tape/strain relief
3. HDMI ribbon clearance
4. Pi HDMI adapter touching rear of LCD
5. display controller power JST

## No boot

Check:

1. Anker battery is charged
2. rear AC inlet is providing charge
3. original power switch is on
4. Anker output is awake
5. battery plunger can wake the Anker
6. 5V rail input is live
7. Pi power JST is seated
8. microSD card is seated

## No boot chime

Check:

1. 5V rail output to YS-M3
2. CK1028 selector position
3. YS-M3 speaker connection
4. SD/card/media on YS-M3 if applicable
5. wait two seconds after power-on

## No audio from Pi

Check:

1. USB speaker connected to Pi
2. PipeWire default sink
3. volume knob did not turn volume down
4. USB speaker is not muted
5. service logs for volume knob

Useful commands:

```bash
pactl list short sinks
pactl get-sink-volume @DEFAULT_SINK@
systemctl status volume-knob.service --no-pager
```

## Apple logo gestures not working

Check:

1. TTP223 gets 5V from rail
2. GPIO signal wire to GPIO 23
3. service is running
4. script uses `LGPIOFactory`
5. no old pigpio assumptions

Useful commands:

```bash
systemctl status apple-gesture-button.service --no-pager
journalctl -u apple-gesture-button.service -f
```

## Volume knob not working

Check:

1. GPIO 17 and 27 encoder lines
2. GPIO 22 push line if needed
3. service is running
4. script has permissions
5. PipeWire default sink exists

```bash
systemctl status volume-knob.service --no-pager
journalctl -u volume-knob.service -f
```

## RetroPie controller exit behavior

The Apple logo hold gesture is intentional.

For the N64 USB controller, there is no spare clean hotkey button. Hold the Apple logo to close the running game. Hold again to close EmulationStation if needed.

## Source select

The rear source button cycles through:

```text
HDMI -> RCA -> VGA -> RCA2 -> repeat
```

Only HDMI and RCA are normally useful.

## Bag charging

If wireless bag charging does not work:

1. confirm hidden USB cable is powered
2. confirm wireless transmitter is aligned under velvet
3. confirm monitor bottom is seated in alignment grooves
4. remember this is trickle charging, not fast charging
