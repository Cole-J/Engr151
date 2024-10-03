import machine
import utime

red = machine.PWM(machine.Pin(12))
green = machine.PWM(machine.Pin(13))
blue = machine.PWM(machine.Pin(14))
red.freq(1000)
green.freq(1000)
blue.freq(1000)
# sets up the 13 14 15 pins and give them the freq of 1000 hz

def interval_mapping(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def color_to_duty(rgb_value): # go from a color 0-255 value to the u16 / 0-65535 value using
                              # this function and the interval_mapping() function
    rgb_value = int(interval_mapping(rgb_value,0,255,0,65535))
    return rgb_value

def color_set(red_value,green_value,blue_value): # sets the r g b values to a given value
    red.duty_u16(color_to_duty(red_value))
    green.duty_u16(color_to_duty(green_value))
    blue.duty_u16(color_to_duty(blue_value))

#color_set(255,75,255) # sets the color using the functions
    
color_set(300,0,0)