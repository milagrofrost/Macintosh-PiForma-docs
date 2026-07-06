# Known Issues and Future Improvements

This is the honest list. Every finished hardware project has one.

## Display ribbon sensitivity

The LCD ribbon currently works, but it is sensitive.

Current state:

- 150mm ribbon cable installed
- taped down to reduce movement
- needs careful alignment
- can cause display issues if shifted during assembly

Future improvement:

- test 80mm or 50mm cable
- reduce slack
- add better strain relief
- avoid disturbing the connector once stable

## Battery fit is tight

The Anker battery is held in the rear by friction.

This works, but it is tight. Probably tighter than ideal.

Future improvement:

- design a dedicated rear cradle
- add thin padding
- add a removable retaining strap
- avoid stressing the case sides

## No fuse protection on custom 5V rail

The rail has no inline fuse or polyfuse.

Current protection depends on:

- Anker battery protection
- device-level protection
- common sense

Future improvement:

- add inline fuse on rail input
- add per-output fusing if rebuilding
- add reverse-polarity protection

## Battery display visibility

The Anker battery display is only visible by peeking through the top slits.

The rear plunger can press the battery button, but the display is not cleanly exposed.

Future improvement:

- add a light pipe
- add a tiny mirror/window
- integrate battery status another way
- ignore it because this is already good enough

## Source select is physical, not touch

Original idea: touch sensor and relay source switching.

Final reality: physical switch wired to LCD controller source button.

Reason:

- noisy power adapter made relays and touch sensors unreliable
- physical switch worked

Future improvement:

- revisit touch-based source selection only if a clean power/noise strategy is used

## Raspberry Pi 5 upgrade

A Raspberry Pi 5 would be nice, but the Pi 4B is currently doing the job.

Future upgrade considerations:

- thermals
- power draw
- HDMI connector differences
- mounting differences
- software compatibility
- cost

## Audio could be fancier

The internal USB speaker is simple and works.

Future improvement:

- better internal speaker
- proper stereo amp
- cleaner RCA audio integration
- keep boot chime speaker separate because it is charming

## External RCA audio is not built in

The rear RCA jack is composite video only. RCA audio requires an external USB-to-audio adapter.

Future improvement:

- add rear RCA audio jacks
- integrate USB audio internally
- add a switchable audio path

## Documentation needs real photos

This repo expects photos to be added under `docs/images/`.

Most important photos:

- front beauty shot
- rear controls
- inside open
- shelf closeup
- battery position
- power rail
- display controller
- Apple logo sensor
- keyboard
- mouse
- bag charging setup
