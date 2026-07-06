# Bill of Materials

This BOM is based on the final installed build, purchase history, and project notes. Some parts are exact. Some are representative because they came from existing bins, local hardware stores, old project stock, or salvage.

The goal is not to pretend the project was clean. Hardware projects are not clean. This is the closest practical record of what is actually in the machine.

## Core donor and compute

| Item | Qty | Status | Purpose | Source / Notes |
|---|---:|---|---|---|
| Apple IIc Monitor A2M4090, Feb 1985 | 1 | final | donor shell | existing collection |
| Original Apple IIc Monitor AC inlet | 1 | final | charger input | reused from donor |
| Original Apple IIc Monitor power switch | 1 | final | interrupts battery output to 5V rail | reused from donor |
| Raspberry Pi 4 Model B, 4GB | 1 | final | compute board | already owned |
| 256GB microSD card | 1 | final | storage | already owned or existing stock |

## Display

| Item | Qty | Status | Purpose | Source / Notes |
|---|---:|---|---|---|
| 9-inch 800x480 HDMI/VGA/AV LCD monitor kit | 1 | final | screen and controller | May 16 AliExpress order |
| LCD controller board from final kit | 1 | final | HDMI/RCA display control | May 16 AliExpress order |
| 150mm FFC/LVDS ribbon cable | 1 | final | LCD to controller | currently installed |
| 50mm or 80mm FFC/LVDS ribbon cable | 1+ | future/backup | shorter cleaner LCD ribbon path | purchased as possible replacement |
| HDMI ribbon / angled adapter path | multiple | final | tight internal HDMI routing | AliExpress/Amazon experiments |
| Micro HDMI angled adapter | 1 | final | Raspberry Pi HDMI clearance | Amazon/AliExpress |
| RCA panel jack | 1 | final | composite video input | Amazon |
| RCA internal cable | 1 | final | rear RCA to LCD controller | Amazon/existing stock |

## Display experiments and engineering tax

| Item | Qty | Status | Purpose |
|---|---:|---|---|
| 9-inch 1024x600 LCD with board | 1 | experiment | early display approach |
| Additional 9-inch LCD panel | 1 | experiment | early panel attempt |
| PCB800099 LCD controller board | 1 | experiment/canceled | early controller attempt |
| PCB800099 / VS-TY2662 style controller | 1 | experiment | HDMI/VGA/AV LCD control |
| Multiple FPV HDMI ribbon cables | many | experiment/final mix | find the orientation that physically fit |
| VSDISPLAY 50-pin ZIF extension | 1 | experiment/backup | display ribbon extension |
| MECCANIXITY 50-pin 0.5mm FFC cables | 1 set | backup | possible shorter ribbon options |

Known AliExpress references:

- Final 9-inch display kit: https://www.aliexpress.com/item/3256805818626591.html
- FPV HDMI ribbon adapters: https://www.aliexpress.com/item/3256808758230576.html
- PCB800099 / VS-TY2662 controller experiment: https://www.aliexpress.com/item/2251832767582592.html
- PCB800099 controller order: https://www.aliexpress.com/item/3256807476829617.html
- 9-inch 1024x600 LCD experiment: https://www.aliexpress.com/item/3256808854350207.html

## Power

| Item | Qty | Status | Purpose | Source / Notes |
|---|---:|---|---|---|
| Anker Prime Power Bank 26K 300W | 1 | final | main battery / UPS / power management | eBay Jan 30 order |
| 100W USB-C power adapter | 1 | final | internal charger | eBay Jan 31 order |
| Original AC inlet wiring reuse | 1 | final | routes rear AC input to internal charger | donor part |
| Custom 5V JST rail | 1 | final | power distribution | handmade |
| Through-hole perfboard | 1 | final | power rail base | existing stock/local |
| Solid-core wire | several | final | soldered bus bars | existing stock |
| Small 2-pin JST connectors | about 6 | final | pluggable 5V outputs | Amazon/LCSC |
| 3D printed rail enclosure | 1 | final | protect rail underside and expose JST ports | printed |
| 18AWG DC barrel pigtails | set | final/stock | power wiring options | Amazon |
| USB-A to bare wire cable | set | final/stock | 5V power lead fabrication | Amazon |
| USB-C solder connector boards | set | stock/experiment | custom USB power/cable work | Amazon |
| Hook and loop cable wrap | 1 roll | final | cable management | Amazon |

Important: no fuses are currently installed in the custom rail. The build relies on the Anker and connected devices for protection.

## Audio

| Item | Qty | Status | Purpose | Source |
|---|---:|---|---|---|
| USB speaker | 1 | final | Raspberry Pi system audio | eBay Jan 30 order |
| YS-M3 MP3 module | 1 | final | boot chime playback | existing/purchased module |
| Mouser CK1028 selector switch | 1 | final | boot chime selector | https://www.mouser.com/ProductDetail/105-CK1028 |
| Salvaged laptop speaker | 1 | final | YS-M3 boot chime output | salvaged |
| 3D printed YS-M3/speaker mount | 1 | final | holds sound module and speaker | printed |
| USB-to-3.5mm/RCA audio adapter | 1 | external accessory | RCA audio when needed | Amazon |
| 3.5mm to RCA audio cable | 1 | external accessory | adapter to RCA | already owned |
| MAX98357A I2S amplifier boards | 2 | unused/experiment | possible audio amp path | Amazon |

## Controls and sensors

| Item | Qty | Status | Purpose | Source |
|---|---:|---|---|---|
| TTP223 capacitive touch sensor | 1 | final | Apple logo gesture input | Amazon |
| TTP223 spare modules | many | stock | experiments/spares | Amazon |
| EC11 rotary encoder | 1 | final | volume knob | Amazon |
| Physical source-select switch | 1 | final | LCD source button extension | existing stock/Amazon |
| Battery plunger button | 1 | final | external Anker button access | printed |
| LDR / LM393 light sensor modules | set | unused/experiment | possible ambient light behavior | Amazon |
| Relay modules | set | unused/abandoned | early touch/source switching idea | Amazon |
| MOSFET modules / transistors | set | unused/experiment | switching experiments | Amazon |

## Keyboard

| Item | Qty | Status | Purpose | Source |
|---|---:|---|---|---|
| Apple ADB Keyboard A9M0330 | 1 | final | main keyboard | existing collection |
| Seeed Studio XIAO nRF52840 | 1 | final | BLE keyboard controller | Seeed order #4000477519 |
| Custom keyboard PCB | 1 | final | ADB keyboard conversion | Fusion PCB order |
| nice!view display | 1 | final | keyboard status display | nice!view order |
| MCP23017-E/SS I/O expander | 2 purchased | final/stock | keyboard matrix I/O | LCSC |
| 110mAh LiPo battery | 1 | final | keyboard battery | Amazon |
| USB-C receptacle | multiple | final/stock | keyboard charging | LCSC |
| JST battery connector | multiple | final/stock | keyboard battery connector | LCSC |
| Slide switch | multiple | final/stock | keyboard power switch | LCSC |
| 10k resistors | 100 | stock | keyboard PCB passives | LCSC |
| 5.1k resistors | 100 | stock | USB-C CC resistors | LCSC |
| ZMK firmware | 1 | final | keyboard firmware | https://github.com/mattchesters/zmk-apple-desktop-bus-keyboard |

Keyboard attribution: the BLE ADB keyboard conversion is based on Matt Chesters' work and should be credited as such.

## Mouse

| Item | Qty | Status | Purpose | Source |
|---|---:|---|---|---|
| Bambu wireless mouse kit | 1 kit in use, 4 purchased | final/spares | matching wireless mouse electronics | Amazon |
| Apple-style 3D printed mouse shell | 1 | final | matching mouse enclosure | link to be added |
| Bambu Smooth PEI plate | 1 | used | better mouse shell printing | Bambu |
| Retro Platinum PLA | 1kg | used | retro-colored printed mouse | Polar Filament |
| USB mouse receiver | 1 | final | plugged into Raspberry Pi | from mouse kit |

## Bag and portability

| Item | Qty | Status | Purpose | Source |
|---|---:|---|---|---|
| LOVFEIFAN / LOVFEI FAN 55x30x20 cm bag | 1 | final | carrying case | Amazon |
| Corrugated plastic | several panels | final | bag liner | Menards/local hardware |
| Foam bottom | 1 | final | padding and alignment | Menards/local hardware |
| Green velvet fabric | 1 yard | final | interior finish | Amazon |
| Spray adhesive | 1 | final | velvet to liner/foam | local hardware |
| Qi wireless charging transmitter | 1 | final | hidden bag trickle charger | Amazon/existing |
| Hidden USB cable | 1 | final | powers wireless charging pad | existing/Amazon |
| Alignment grooves | 1 set | final | aligns monitor with charging pad | handmade/printed/foam work |
| Monitor stand | 1 | final | supports monitor when in use | 3D printed |

## Purchased but not final

| Item | Reason |
|---|---|
| Relay modules | source switching via touch was abandoned |
| Noisy Amazon power adapter | caused EMI problems |
| MAX98357A amps | USB speaker path won |
| Extra LCD panels/controllers | final May 16 display kit won |
| Many HDMI ribbons | only the fit-friendly path mattered |
| LDR modules | not part of final installed behavior |
| MOSFET switch boards | not part of final installed behavior |
