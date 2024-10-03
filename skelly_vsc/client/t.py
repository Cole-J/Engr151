import network
import time
import machine
import socket

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("beeroj", "G0Huskies!")
while not wlan.isconnected() and wlan.status() >= 0:
    print("Waiting to connect:")
    time.sleep(1)

m_left = machine.Pin(0, machine.Pin.OUT)
m_right = machine.Pin(1, machine.Pin.OUT)

# Should be connected and have an IP address
wlan.status() # 3 == success
wlan.ifconfig()
print(wlan.ifconfig())

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

    if ss[3] == True:
        print("l")
    if ss[6] == True:
        print("r")
    print()

    s.close()          # Close socket
    time.sleep(0.2)    # wait