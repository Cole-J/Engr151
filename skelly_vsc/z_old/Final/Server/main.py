# Webserver to send RGB data
# Tony Goodhew 5 July 2022
import network
import socket
import time
from machine import Pin, ADC
import config
import random
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(config.ssid, config.password)

b_left = Pin(15, Pin.IN)
b_right = Pin(16, Pin.IN)
l = Pin("LED", Pin.OUT)
l.value(0)
       
# Wait for connect or fail
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )

# Open socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

# Listen for connections
while True:
    try:
        cl, addr = s.accept()
        print('client connected from', addr)
        request = cl.recv(1024)
        print(request)

        response = [False,False]

        if b_left.value() == 0:
            response[0] = True
        if b_right.value() == 0:
            response[1] = True

        cl.send(response)
        print("Sent:" + str(response))
        cl.close()

        time.sleep(.05)
        l.toggle()

    except OSError as e:
        cl, addr = s.accept()
        cl.close()
        print('connection closed')
