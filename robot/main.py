

# imports
import machine # microcontroller library
#import math as m # math library
#import _thread as _t # threading library
#import utime as t # time library
import utime

# methods
from ws2812 import WS2812 # rbg led strip method
#from servo import servoClass as servo # servo class method
#from frame import interval_mapping # framework method



ws = WS2812(machine.Pin(0),8)

