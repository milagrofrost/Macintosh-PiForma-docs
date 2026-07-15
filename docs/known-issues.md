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

## Raspberry Pi heat can warp the upper shelf

The Raspberry Pi 4B runs very hot inside the enclosed case. Because the Pi originally sat directly on the upper printed shelf, prolonged heat softened and warped the shelf plastic.

The LCD display controller board is mounted directly beneath that shelf. As the shelf sagged and flexed, it began pressing against or bending the display controller board. This produced symptoms that initially looked like a bad ribbon cable or loose display connection, including:

- graphical glitches
- intermittent display failure
- loss or distortion of color
- image instability
- behavior that changed when the shelf, controller board, or ribbon area was disturbed

The actual cause was mechanical pressure on the display controller board resulting from heat deformation above it, not necessarily a failed LCD ribbon.

Current mitigation:

- Raspberry Pi elevated above the printed shelf with an additional 3D printed cradle or mount
- air gap added between the Pi and the shelf
- aluminum foil used as a heat-reflective layer below the Pi and above it near the top of the shelf enclosure
- shelf secured to the case with a zip tie to reduce further sagging
- display controller board checked to ensure the shelf is no longer flexing it

The foil must remain electrically isolated from the Raspberry Pi, display controller, GPIO pins, solder joints, and other exposed electronics because aluminum foil is conductive.

Current result:

- the shelf appears more stable
- heat transfer into the printed shelf is reduced
- display glitches caused by pressure on the controller board have not returned so far

Future improvement:

- redesign the upper shelf with a center support column or rib
- use a more heat-resistant filament for the shelf
- add a purpose-built Pi mount with permanent airflow clearance
- add active or passive cooling for the Raspberry Pi
- replace loose foil with a nonconductive thermal barrier or properly secured insulated heat shield
- add ventilation openings if they can be incorporated without harming the exterior appearance
- monitor Pi temperature during extended use
- inspect the display controller board and shelf whenever unexplained display problems appear

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
