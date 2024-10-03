import machine
import utime

b_left = machine.Pin(15, machine.Pin.IN) # gets the button and switch inputs
b_right = machine.Pin(16, machine.Pin.IN)
switch = machine.Pin(14, machine.Pin.IN)

o_left = machine.Pin(0, machine.Pin.OUT) # motor outputs
o_right = machine.Pin(1, machine.Pin.OUT)
o_left.value(0) # sets motor output to off
o_right.value(0)
led = machine.Pin(2, machine.Pin.OUT) # led outputs

while True: # main loop
    if switch.value() == 1: # checks if the switch is at its high position
        led.value(1) # turns on the leds
        print("switch open")
        if b_left.value() == 0: # checks if the left button is at high value (pull up)
            o_left.value(1) # sets motor output to high
        else:
            o_left.value(0) # sets motor output to low
        
        if b_right.value() == 0: # same as above
            o_right.value(1)
        else:
            o_right.value(0)
    else:
        led.value(0) # turns off the leds when switch is in low position
    utime.sleep(.02)
