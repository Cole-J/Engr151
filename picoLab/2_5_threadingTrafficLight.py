'''
modified code from SunFounder 2.5 traffic light assignment
'''

import machine
import utime
import _thread # import thread library

led_red = machine.Pin(15, machine.Pin.OUT)
led_yellow = machine.Pin(14, machine.Pin.OUT)
led_green = machine.Pin(13, machine.Pin.OUT)
led_blue = machine.Pin(12, machine.Pin.OUT) # led specifically for walk time
button = machine.Pin(16, machine.Pin.IN)

led_red.value(0) # force all leds off on program start
led_yellow.value(0)
led_green.value(0)
led_blue.value(0)

global button_status # making the button status a global variable
# now it can be changed localy in every function
button_status = 0

# all time is in seconds

# time that the blue AND red leds are on, simulates crosswalk time
blueLightTime = 15
# time that the red led is on, simulates the red light
redLightBaseTime = 120
# time that the yellow led is on, simulates the yellow light
yellowLightTime = 5
# time that the green led is on, simulates the green light
greenLightTime = 120

def button_thread(): # secondary thread function
    global button_status
    while True:
        if button.value() == 1: # look for change in button value
            button_status = 1

_thread.start_new_thread(button_thread, ()) # starts the second thread

while True: # starts the main thread
    if button_status == 1: # when the button value changes it increases the time the red led is on
        led_red.value(1)
        led_blue.value(1)
        utime.sleep(blueLightTime)
    global button_status
    button_status = 0 # sets the button value back to 0 until the next press
    led_blue(0)

    # default traffic light sequence

    led_red.value(1)
    utime.sleep(redLightBaseTime)
    led_red.value(0)

    led_yellow.value(1)
    utime.sleep(yellowLightTime)
    led_yellow.value(0)

    led_green.value(1)
    utime.sleep(greenLightTime)
    led_green.value(0)

    led_yellow.value(1)
    utime.sleep(yellowLightTime)
    led_yellow.value(0)