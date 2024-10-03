import machine
from utime import sleep # gets only the sleep function from utime

# define variables and constants
led_r = machine.Pin(15, machine.Pin.OUT) # red yellow and green leds
led_y = machine.Pin(14, machine.Pin.OUT)
led_g = machine.Pin(13, machine.Pin.OUT)

led_c = [led_r, led_y, led_g] # makes a list of the leds
led_basis = [1, 2, 3] # list for when each led turns on

final = 4 # const
c = 0 # const < ^ can be changed but should not be
sleepTime = 1 # the time between lights changing (can be changed)


''' the different states the lights will be in (r, y, and g are different leds)
0 no light
1 r
2 r and y
3 r y and g
'''

while True: # loops while program is active
    
    if (c >= final):
        c = 0 # counts from 0-3 by counting up and changing 4 to 0
        
    if (c > 0): # stops errors when c = 0 aka no lights on
        x = 0 # makes new count variable
        while (x < 3): # loops 3 times
            
            if (c >= led_basis[x]):
                led_c[x].value(1)
            else:
                led_c[x].value(0)    
            x += 1
            # loops through each led and sees if it should be turned on (based off the basis list)
    
    else:
        for led in led_c: # pulls each led in led_c individually
            led.value(0) # turns off all leds when c == 0
            
    #print(c) # for debugging
    c += 1
    sleep(sleepTime)