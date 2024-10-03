import machine as m
import time as t
import random as r
import _thread as _t

import ws2812

ws = ws2812.WS2812(m.Pin(16),8)

button = m.Pin(15, m.Pin.IN)
# 0 low 1 high

def off(ws, num = 8): # turns off the led nodes
    for x in range(num):
        ws[x] = [0, 0, 0]
    ws.write()

def t_bounce(ws, color, wait, num = 8): # bounces a set of colors between the 2 ends of the led strip
    for x in range(num): # moves from node 0 to 7
        print(x)
        ws[x] = color
        ws.write()
        t.sleep(wait)
        off(ws)
    for x in range(num-1, 0, -1): # moves from node 7 to 1
        print(x)
        ws[x] = color
        ws.write()
        t.sleep(wait)
        off(ws)

def t_swipe(ws,  color, wait, num = 8): # loops a color fromD node 0 to 7
    for x in range(num):
        print(x)
        ws[x] = color
        ws.write()
        t.sleep(wait)
        off(ws)

def t_randBlink(ws, wait, num = 8): # picks a random color and a random node and sets the node to that color for a given time
    ws[r.randint(0, 7)] = [r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)]
    ws.write()
    t.sleep(wait)
    off(ws)

# input thread function

global ledType # global values to control what t function play
ledType = 0

def selectTypeThread(): # when the button is pressed ledType is stepped by 1 with a range of 0-2
    # when ledType == 3 it is reset to 0
    global ledType
    prevLedType = 5
    while True:
        if prevLedType != button.value(): # checks for a new input
            if button.value() == 1: # checks for a button input
                ledType += 1

                if ledType == 3: # keeps ledType in range
                    ledType = 0
        
        prevLedType = button.value()
        print(ledType)
        t.sleep(.02)

# main threads

_t.start_new_thread(selectTypeThread, ()) # starts the second thread which handles the inputs

while True: # the main loop which handles which t functions play during different ledTypes
    if ledType == 0:
        print(ledType)
        t_bounce(ws, [255, 75, 200], .1)
    elif ledType == 1:
        print(ledType)
        t_swipe(ws, [255, 130, 0], .1)
    else:
        print(ledType)
        t_randBlink(ws, .3)
    t.sleep(.05)