import machine
import utime
button = machine.Pin(14, machine.Pin.IN) # using IN to say that it will be recieving information form the pin
while True:
    if button.value() == 1: # button flips from 0 to 1 when pressed, if statment checks that
        print("You pressed the button!", button.value())
        utime.sleep(1)