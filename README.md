# Mini Keyboard (Hackpad‑Style)

A small, customizable **mini keyboard / hackpad-style macropad** designed for tinkering, learning, and daily shortcuts. This project uses a custom PCB, schematic, and a fully **3D‑printed case** (no acrylic).

---

## Overview

* **Form factor:** Mini keyboard / hackpad
* **Switch type:** MX‑style
* **Keycap profile:** DSA
* **Case:** 3D‑printed only
* **Firmware:** User‑defined (QMK / KMK / other RP2040‑compatible firmware)

This project is intended to be beginner‑friendly while still allowing deep customization for more advanced users.

---

## Repository Contents

```
/pcb        → PCB design files
/schematic → Electrical schematic
/case       → 3D files for the printed case
/firmware   → (optional) firmware files
README.md   → This file
```

---

## Bill of Materials (BOM)

### Mass‑Produced / Standard Parts

*(Fill in exact quantities as needed)*

* MX‑style mechanical switches (Max **16×**)
* Blank DSA keycaps – **White**
* Rotary encoder (EC11 / Alps‑style)
* Knob for rotary encoder (6 mm D‑shaft)
* Microcontroller (RP2040‑based, e.g. XIAO RP2040)
* SK6812 MINI‑E (or compatible) RGB LEDs
* Diodes (if required by PCB design)
* USB‑C cable

### Hardware

* M3 × 16 mm screws
* M3 heat‑set inserts (5 mm OD × 4 mm length)
* Optional: M3 washers
* Optional: Rubber feet

---

### Custom / Non‑Mass‑Produced Parts

*(Project‑specific — intentionally left open)*

* Custom PCB
* Custom schematic
* 3D‑printed case (top & bottom)
* Optional: 3D‑printed switch plate or integrated plate design
* Optional: Custom knob or decorative elements

---

## Case & Mounting

* The case is **fully 3D‑printed** (no acrylic parts required)
* Heat‑set inserts are installed into the case for durability
* PCB is mounted directly to the case using M3 screws
* Switches are either:

  * PCB‑mounted (plate‑less), or
  * Mounted using an integrated 3D‑printed plate

Ensure heat‑set inserts are installed carefully using a soldering iron tip sized for M3 inserts.

---

## Assembly Notes

1. Solder all SMD components (LEDs, diodes, etc.)
2. Solder the microcontroller
3. Solder the rotary encoder
4. Insert and solder MX switches
5. Install heat‑set inserts into the case
6. Mount PCB into the case using M3 screws
7. Attach keycaps and encoder knob

---

## Firmware

* Compatible with RP2040‑based firmware ecosystems
* Recommended:

  * QMK
  * KMK

Keymaps, layers, and encoder behavior are fully customizable.

---

## Theme & Inspiration

This project is inspired by **hackpads and mini keyboards** — compact, playful, and purpose‑built devices for shortcuts, macros, and creative workflows.

Perfect for:

* Coding shortcuts
* Media control
* CAD / design macros
* Learning keyboard firmware

---

## License

*(Add license information here)*

---

## Credits

Designed and built by *(your name / handle)*
Inspired by open‑source mechanical keyboard and hackpad communities.
