import machine
import utime

# button
button = machine.Pin(15,machine.Pin.IN)
# rgb led
led_r = machine.PWM(machine.Pin(12))
led_g = machine.PWM(machine.Pin(13))
led_b = machine.PWM(machine.Pin(14))
led_r.freq(1000)
led_g.freq(1000)
led_b.freq(1000)

# functions from 2.9 rgb led
def interval_mapping(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def color_to_duty(rgb_value): # go from a color 0-255 value to the u16 / 0-65535 value using
                              # this function and the interval_mapping() function
    rgb_value = int(interval_mapping(rgb_value,0,255,0,65535))
    return rgb_value
    
def color_set(red_value,green_value,blue_value): # sets the r g b values to a given value
    led_r.duty_u16(color_to_duty(red_value))
    led_g.duty_u16(color_to_duty(green_value))
    led_b.duty_u16(color_to_duty(blue_value))
# end of functions from 2.9

while True:
    print(button.value())
    
    if (button.value() == 1):
        color_set(0,0,255) # sets color to blue if value == 1
    else:
        color_set(255,0,0) # sets color to red if value == 0

    utime.sleep_ms(500) # sleep for .5s