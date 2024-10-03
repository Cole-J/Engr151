import machine # import 
import utime
import _thread
signal = machine.Pin(15, machine.Pin.OUT) # sends voltage out from pin 15
led = machine.Pin(25, machine.Pin.OUT)

def interval_mapping(x, in_min, in_max, out_min, out_max): # interval mapping function
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

