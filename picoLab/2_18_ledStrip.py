'''
this program uses the ws2812 module to control the led strip using the ws object. the ws object acts like a 2d array in that
the first array is the led node and the second is the 3 color values (r, g, b).

you call the node with ws[x] and set it with ws[x] = [r, g, b].

the write function sets the led strips values to the ones that you passed to the ws object
'''
import machine # imports machine / micropython api
from ws2812 import WS2812 # imports the WS class from the ws method

ws = WS2812(machine.Pin(16),8) # creates a object from the WS class
# the classes __init__ passes the pin and the length of the led strip

ws[0] = [64,154,227] # sets the rgb values from node 1 to 8
ws[1] = [128,0,128]
ws[2] = [50,150,50]
ws[3] = [255,30,30]
ws[4] = [0,128,255]
ws[5] = [99,199,0]
ws[6] = [128,128,128]
ws[7] = [255,100,0]
ws.write() # writes the current node led values to the out pin / rgb strip