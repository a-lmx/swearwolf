import time

import board
import neopixel

RED = (255, 0, 0)
YELLOW = (255, 115, 0)

class Jewel():
    
    led_count = 7 # One Jewel
    led_pin = board.D18
    led_brightness = 0.3
    led_order = neopixel.GRB
    
    def __init__(self):
        self.led = neopixel.NeoPixel(
            self.led_pin,
            self.led_count,
            brightness=self.led_brightness,
            auto_write=False,
            pixel_order=self.led_order,
        )

    def neutral_eyes(self):
        self.led.fill(YELLOW)
        self.led.show()

    def red_eyes(self, duration):
        self.led.fill(RED)
        self.led.show()
        time.sleep(duration)

    def flash_eyes(self, duration):
        self.red_eyes(duration)
        self.neutral_eyes()

    def turn_off(self):
        self.led.deinit()

j = Jewel()
j.neutral_eyes()
time.sleep(5)
j.flash_eyes(2)
time.sleep(2)
j.turn_off()
