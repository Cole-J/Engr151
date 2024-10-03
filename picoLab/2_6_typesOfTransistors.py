'''
the transistor is able to take a low voltage input to control a high voltage. The button is the low voltage input and the signal is 
the high voltage output. the wiring has the input on a 1k resistor, and the led is on a 220 om resistor.

in the while true loop it is checking for when the voltage from the input is detected, and when it is it sends voltage to the output.
since the out runs through a 1k om resistor, normally the led would be very dim but instead of running into the led it is
controlling the transistor. the transistor is connected from the ground to the transistor to the led and then to the vbus.
when pin 15 sends a signal to the transistor it then allows current to flow from the vbus to te led to ground.
'''
import machine # import 
button = machine.Pin(14, machine.Pin.IN) # when the putton is pressed / voltage flows it is detected at pin 14
signal = machine.Pin(15, machine.Pin.OUT) # sends voltage out from pin 15

while True:
    button_status = button.value()
    if button_status== 1: # detects low voltage signal from the button
        signal.value(1) # sends a larger voltage out
    elif button_status == 0: # if there is now voltage going in to pin 14
        signal.value(0) # stop sending voltage to pin 15