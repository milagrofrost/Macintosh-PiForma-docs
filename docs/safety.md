# Safety

This build modifies a vintage monitor shell, reuses an AC inlet, contains a high-capacity lithium battery pack, and includes custom power wiring.

Do not copy the power wiring blindly.

## AC inlet warning

The original Apple IIc Monitor AC inlet is reused as part of the charging path.

In the final build:

- the AC inlet feeds an internal 100W USB power adapter
- the original monitor power switch does not switch mains AC
- the original power switch interrupts battery output to the 5V rail

This is safer than switching AC with the old monitor switch, but it still means there is AC wiring inside the case.

If reproducing:

- strain-relieve AC wiring
- insulate all AC connections
- keep AC wiring physically separated from low-voltage wiring
- do not leave exposed mains terminals
- do not route AC where it can rub against printed parts or sharp metal
- do not build this part if you are not comfortable with mains wiring

## Lithium battery warning

The build uses an Anker Prime 26K 300W battery.

The Anker handles battery management internally, but the build still physically traps a large battery inside an old monitor shell.

Do not:

- puncture the battery
- crush the battery
- block heat dissipation excessively
- use a swollen or damaged pack
- leave it charging unattended in a questionable state

## No custom rail fusing

The custom JST rail currently does not have separate fuse protection.

The build relies on the Anker and device protections.

If reproducing this, consider adding:

- a fuse on rail input
- per-output protection
- clear polarity markings
- strain relief
- wire gauge appropriate for load

## CRT warning

The donor CRT was removed years ago.

Anyone working with a vintage CRT monitor should understand that CRTs can hold dangerous voltages even after being unplugged. This documentation is for the finished LCD conversion, not a CRT repair guide.

## Heat

The build includes:

- Raspberry Pi 4B
- LCD driver
- internal USB power adapter
- Anker battery
- closed vintage plastic shell

Check heat under real use. Do not assume it is fine because it boots.

## The honest rule

If something smells hot, flickers weirdly, makes relays go crazy, causes touch sensors to false trigger, or behaves possessed, stop and debug power first.

That is not superstition. That is what already happened once.
