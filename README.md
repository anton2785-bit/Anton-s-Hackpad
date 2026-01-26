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
/pcb        → https://github.com/anton2785-bit/Anton-s-Hackpad/tree/main/PCB
/CAD        → https://github.com/anton2785-bit/Anton-s-Hackpad/tree/main/CAD
/firmware   → https://github.com/anton2785-bit/Anton-s-Hackpad/tree/main/Firmware
README.md   → This file
```

---

## Bill of Materials (BOM)

### Standard Parts

*(Fill in exact quantities as needed)*

* MX‑style mechanical switches (**8x**)
* Blank DSA keycaps – **White**
* Rotary encoder (EC11E / Alps‑style)
* Microcontroller (XIAO RP2040)
* SK6812 MINI‑E RGB LEDs

### Hardware

* M3 × 16 mm screws
* M3 heat‑set inserts (5 mm OD × 4 mm length)

---

### Custom / Non‑Mass‑Produced Parts

*(Project‑specific)*

* Custom PCB                         
*  <img width="500" height="314" alt="PCB" src="https://github.com/user-attachments/assets/6383d823-9b49-4665-939e-46c50596156d" />
* Custom schematic
* <img width="500" height="314" alt="sheme" src="https://github.com/user-attachments/assets/15d03ea6-f131-48ee-abd6-9f552d25272d" />
*  3D‑printed case (top & bottom)
*  <img width="500" height="314" alt="CAD case" src="https://github.com/user-attachments/assets/b69bd919-653e-4ac3-8c99-e03bbc4ab3e6" />




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
