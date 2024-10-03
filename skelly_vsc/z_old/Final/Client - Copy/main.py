# network imports
import network
import time
import config
import socket
import _thread
# output imports
import motor
import tone
import led
# notes file to pass to tone

# board setup
print("startup, def o pins")
# motor setup
o_motor_left = motor.create_motor(config.p_m_l)
o_motor_right = motor.create_motor(config.p_m_r)
# led setup
o_led = led.create_led(config.p_led_r, config.p_led_g, config.p_led_b)
# buz setup
o_buz = tone.create_tone(config.p_buz_pin, config.p_buz_duty)
print("out pins defined")

print("connecting to server")
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(config.ssid, config.password)
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
    i_led_type = ss[9]
    i_led_on = ss[15]
    i_buz_type = ss[12]
    i_buz_on = ss[18]

    # motor drive control
    if i_left_v == 1:
        o_motor_left.move()
    else:
        o_motor_left.stop()

    if i_right_v == 1:
        o_motor_right.move()
    else:
        o_motor_right.stop()
    
    
    # led control
    o_led.set_color(255, 130, 0)

    # buz control
    if i_buz_on == 1 and o_buz.isPlaying() == False:
        _thread.start_new_thread(o_buz.play, ())

    
    time.sleep(0.2)    # wait