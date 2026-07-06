# Build Log

This is the story version. The technical docs explain what it is. This explains how it became that way.

## The old idea

Macintosh PiForma started as one of those future-me-will-do-something-with-this objects.

The donor Apple IIc Monitor came from the existing collection. The CRT was not in good shape. It was discolored, flickering, and not worth turning into a heroic restoration project. The CRT was removed years ago, but the case, screws, internals, and shell were kept because maybe someday there would be a reason.

This build is that reason.

## The influence

This project owes a lot of its spirit to the old Macintosh modding scene. AppleFritter, G3 and G4 mods, painted cases, weird internal hacks, utilitarian mods, and builds that made no sense except that they absolutely made sense to the person building them.

That is the lane Macintosh PiForma lives in.

It is not a museum restoration. It is a Mac mod. A Pi mod. A Performa pun. A portable retro computer. A small pile of what-if-this-actually-worked.

## January 2026: display and power start to take shape

The early purchases were about proving the core idea:

- 9-inch LCD with controller
- Anker Prime 26K 300W battery
- USB speaker
- 100W USB-C charger
- Apple-ish supporting parts
- early display boards and adapters

The Anker became the right choice because it solved the ugly power problems:

- charging
- battery management
- protection
- portable runtime
- USB power output

Instead of building a battery management system, the build wraps around a battery pack that already knows how to be a battery pack.

## February 2026: the cable and controller era

This was the part where theory got punched in the face by connector orientation.

A lot of HDMI ribbon cables and display controller options were purchased because there was no way to know exactly what angle, length, or connector direction would fit until parts were physically inside the case.

This is the engineering tax phase.

Not waste. Tuition.

Also around this time, the keyboard conversion work became real:

- XIAO nRF52840
- custom PCB
- nice!view
- LiPo
- ZMK
- ADB keyboard conversion based on Matt Chesters' work

## March and April 2026: structure and refinement

The project moved from will-this-display-work to how-does-everything-live-inside-this-thing.

This is where the custom internal shelf becomes the actual heart of the build.

The shell is vintage. The Pi is the compute module. The Anker is the battery. But the shelf is what makes it one machine.

It organizes:

- Pi
- display controller
- internal charger
- speaker
- 5V rail
- cable paths

The battery stayed separate, sitting on the rear metal chassis floor, wedged in by friction.

## May 2026: final display and less nonsense

The May 16 LCD kit became the final working display setup. The build settled around 800x480.

The noisy Amazon power adapter was rejected after causing EMI weirdness. Relays and touch sensors were acting possessed. The eBay 100W adapter behaved better and became the final internal charger.

The source select plan also got simpler. Instead of using touch sensors and relays, the final build wires the LCD controller's source button to a physical rear switch.

That is not less clever. It is more finished.

## June 2026: software, gestures, and putting a bow on it

The software side matured into the final experience:

- Mac OS 9-ish desktop
- Apple logo gesture button
- volume knob service
- boot chime selector
- RetroPie launch without keyboard/mouse
- Weather Channel kiosk
- Flying Toasters
- Mac OS 9 / SheepShaver
- Winamp/QMMP
- browser launchers

The Apple logo gesture button became one of the most useful features. Four taps launches RetroPie. Holding the logo closes the game or exits EmulationStation, solving the N64 controller hotkey problem without sacrificing a game button.

That is exactly the kind of feature that makes this feel integrated instead of just assembled.

## What made it finished

The project felt done when these things were true:

- it powered on with the original monitor switch
- it played a selectable boot chime
- it had a working internal display
- it had working internal audio
- it had a usable desktop
- it could launch RetroPie from the Apple logo
- it had a working Bluetooth ADB keyboard
- it had a matching mouse
- it had a travel bag that protected and charged it

At that point, it stopped being a project I need to finish and became a computer I built.

That is where this documentation freezes the build.
