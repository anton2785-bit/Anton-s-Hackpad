import board
import neopixel

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

# =========================
# SWITCHES SW1 → SW8
# =========================
keyboard.matrix = KeysScanner(
    pins=[
        board.GP26,  # SW1
        board.GP27,  # SW2
        board.GP28,  # SW3
        board.GP29,  # SW4
        board.GP6,   # SW5
        board.GP7,   # SW6
        board.GP0,   # SW7
        board.GP1,   # SW8
    ],
    value_when_pressed=False,
)

keyboard.keymap = [[
    KC.N1,
    KC.N2,
    KC.N3,
    KC.N4,
    KC.N5,
    KC.N6,
    KC.N7,
    KC.N8,
]]

# =========================
# SK6812 / NEOPIXEL LEDs
# =========================
NUM_LEDS = 3

pixels = neopixel.NeoPixel(
    board.GP3,     # LED DIN
    NUM_LEDS,
    brightness=0.3,
    auto_write=True,
)

def show_led(index):
    pixels.fill((0, 0, 0))
    pixels[index] = (0, 255, 0)  # green

show_led(0)

# =========================
# ROTARY ENCODER
# =========================
encoder = EncoderHandler()
keyboard.modules.append(encoder)

encoder.pins = (
    (board.GP4, board.GP2),  # A, B
)

encoder_pos = 0
ENCODER_MAX = 29

def encoder_update(direction):
    global encoder_pos
    encoder_pos += direction

    # Clamp range
    if encoder_pos < 0:
        encoder_pos = 0
    if encoder_pos > ENCODER_MAX:
        encoder_pos = ENCODER_MAX

    # Split into thirds
    if encoder_pos < ENCODER_MAX / 3:
        show_led(0)
    elif encoder_pos < (ENCODER_MAX * 2) / 3:
        show_led(1)
    else:
        show_led(2)

encoder.map = [
    ((encoder_update, encoder_update),),
]

# =========================
# START KMK
# =========================
if __name__ == '__main__':
    keyboard.go()
