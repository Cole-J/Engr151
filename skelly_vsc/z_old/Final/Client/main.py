# network imports
import network
import time
import socket
import machine

# output imports

# notes file to pass to tone

# board setup
print("startup, def o pins")
# motor setup
o_motor_left = machine.Pin(0, machine.Pin.OUT)
o_motor_right = machine.Pin(1, machine.Pin.OUT)

print("out pins defined")

print("connecting to server")
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("beeroj", "G0Huskies!")
while not wlan.isconnected() and wlan.status() >= 0:
    print("Waiting to connect:")
    time.sleep(1)
 
# Should be connected and have an IP address
wlan.status() # 3 == success
wlan.ifconfig()
print(wlan.ifconfig())
while not wlan.isconnected(): pass

print("connected")

while True:
    ai = socket.getaddrinfo("192.168.5.71", 80) # Address of Web Server
    addr = ai[0][-1]
    

    # Create a socket and make a HTTP request
    s = socket.socket() # Open socket
    s.connect(addr)
    s.send(b"GET Data") # Send request
    ss=str(s.recv(512)) # Store reply
    # Print what we received
    print(ss)
    s.close()          # Close socket

    # unpacking data
    i_left_v = ss[3]
    i_right_v = ss[6]
    #i_led_type = ss[9]
    #i_led_on = ss[15]
    #i_buz_type = ss[12]
    #i_buz_on = ss[18]

    # motor drive control

    

    
    time.sleep(0.2)    # wait
