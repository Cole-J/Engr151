# imports
import machine # gets the machine library / commands related to the board
import utime # gets library for internal clock commands

# pulls the led location from the board
led_onboard = machine.Pin(25, machine.Pin.OUT)
while True: # loops program
    led_onboard.value(1) # turns led on
    utime.sleep(2) # waits 2 seconds
    led_onboard.value(0) # turns led off
    utime.sleep(2) #waits 2 seconds for proper looping