import machine
import utime
import _thread # import thread library

led_red = machine.Pin(1, machine.Pin.OUT)
led_yellow = machine.Pin(2, machine.Pin.OUT)
led_green = machine.Pin(3, machine.Pin.OUT)
button = machine.Pin(4, machine.Pin.IN)

global button_status # making the button status a global variable
# now it can be changed localy in every function
button_status = 0

def button_thread(): # secondary thread function
    global button_status
    while True:
        print("t")
        if button.value() == 1: # look for change in button value
            button_status = 1
        utime.sleep(.5)
_thread.start_new_thread(button_thread, ()) # starts the second thread

while True: # starts the main thread
    if button_status == 1: # when the button value changes it increases the time the red led is on
        led_red.value(1)
        utime.sleep(2)
    global button_status
    button_status = 0 # sets the button value back to 0 until the next press

    # default sequence
    print("m")
    utime.sleep(1)