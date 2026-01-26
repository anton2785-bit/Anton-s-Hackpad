# Mini Keyboard (Hackpad‑Style)

A small, customizable **mini keyboard / hackpad-style macropad** designed for tinkering, learning, and daily shortcuts. This project uses a custom PCB, schematic, and a fully **3D‑printed case** (no acrylic).

---

## Overview

* **Form factor:** Mini keyboard / hackpad
* **Switch type:** MX‑style
* **Keycap profile:** DSA
* **Case:** 3D‑printed only
* **Firmware:** KMK
This project is intended to be beginner‑friendly while still allowing deep customization for more advanced users.

---

## Repository Contents

```
/pcb        → 
/CAD        → 
/firmware   → 
README.md   → 
```

---

## Bill of Materials (BOM)

### Mass‑Produced / Standard Parts

*(Fill in exact quantities as needed)*

* MX‑style mechanical switches (**8x**)
* Blank DSA keycaps – **White**
* Rotary encoder (EC11E / Alps‑style)
* Microcontroller (XIAO RP2040)
* SK6812 MINI‑E RGB LEDs
* USB‑C cable

### Hardware

* M3 × 16 mm screws
* M3 heat‑set inserts (5 mm OD × 4 mm length)

---

### Custom / Non‑Mass‑Produced Parts

*(Project‑specific)*

* Custom PCB
* Custom schematic
* 3D‑printed case (top & bottom)

---

## Case & Mounting

* The case is **fully 3D‑printed** 
* Heat‑set inserts are installed into the case for durability
* PCB is mounted directly to the case 

Ensure heat‑set inserts are installed carefully using a soldering iron tip sized for M3 inserts.

---

## Assembly Notes

1. Solder all LEDs
2. Solder the microcontroller
3. Solder the rotary encoder
4. Insert and solder MX switches
5. Install heat‑set inserts into the case
6. Mount PCB into the case using M3 screws
7. Attach keycaps 

---

## Firmware

* Compatible with RP2040‑based firmware ecosystems
* Recommended:

  * KMK

Keymaps, layers, and encoder behavior are fully customizable.

---

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

Designed and built by *(Anton/ Anton-2785-bit)*
Inspired by open‑source mechanical keyboard and hackpad communities (https://blueprint.hackclub.com/home).
