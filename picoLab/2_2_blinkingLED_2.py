# imports
import machine
import utime 

led = machine.Pin(15, machine.Pin.OUT) # sets object led to pin 15
while True: # loops while program is active
    led.toggle() # toggles / switches current value
    utime.sleep(1) # wait 1 second