import machine
from framework import interval_mapping

class create_led:

    def __init__(self, pin_r, pin_g, pin_b):
        self.pin_r = pin_r
        self.pin_b = pin_b
        self.pin_g = pin_g

        self.led_r = machine.PWM(machine.Pin(self.pin_r))
        self.led_b = machine.PWM(machine.Pin(self.pin_b))
        self.led_g = machine.PWM(machine.Pin(self.pin_g))

    def set_color(self, r, g, b):
        self.led_r.duty_u16(__color_to_duty(r))
        self.led_b.duty_u16(__color_to_duty(b))
        self.led_g.duty_u16(__color_to_duty(g))

def __color_to_duty(rgb_value):
    rgb_value = int(interval_mapping(rgb_value,0,255,0,65535))
    return rgb_value