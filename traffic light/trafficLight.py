import machine
from machine import time_pulse_us
import utime
import _thread
import time

#lights

street1_led_green = machine.Pin(1,machine.Pin.OUT)
street1_led_yellow = machine.Pin(2, machine.Pin.OUT)
street1_led_red = machine.Pin(3, machine.Pin.OUT)

street2_led_green = machine.Pin(4, machine.Pin.OUT)
street2_led_yellow = machine.Pin(5, machine.Pin.OUT)
street2_led_red = machine.Pin(6, machine.Pin.OUT)

croswalk_led = machine.Pin(8, machine.Pin.OUT)

buzzer = machine.PWM(machine.Pin(10))

#sensors

FSR = machine.ADC(28)

ultra_trig = machine.Pin(12, machine.Pin.OUT) 
ultra_echo = machine.Pin(13, machine.Pin.IN)


# switches

switch = machine.Pin(14, machine.Pin.IN)

# functions

def interval_mapping(x, in_min, in_max, out_min, out_max):
    if (in_min > x):
        return out_min
    elif (in_max < x):
        return out_max
    else:
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    
# led functions

def set_street_led (street,R,Y,G):
    if street == 1:
        street1_led_green.value(G)
        street1_led_yellow.value(Y)
        street1_led_red.value(R)
    else:
        street2_led_green.value(G)
        street2_led_yellow.value(Y)
        street2_led_red.value(R)

# ultrasonic       
SOUND_SPEED=340 # Speed ​​of sound in air
TRIG_PULSE_DURATION_US=10

def distance(pin_T, pin_E):
    # Prepare the signal
    pin_T.value(0)
    time.sleep_us(10)
    # Create a 10 µs pulse
    pin_T.value(1)
    time.sleep_us(TRIG_PULSE_DURATION_US)
    pin_T.value(0)

    ultrason_duration = time_pulse_us(pin_E, 1, 30000) # Returns the wave propagation time (in µs)
    distance_cm = SOUND_SPEED * ultrason_duration / 20000

    return distance_cm

#FSR

Voltage = 3.3
Resistance = 3230

def force():
        # Read the FSR value 
    fsr_value = FSR.read_u16()
    
    # Calculate voltage using the ADC reading
    voltage = interval_mapping(fsr_value, 0, 65535, 0, Voltage)

    # Calculate FSR resistance
    FSR_resistance = Resistance * (Voltage / voltage - 1)



    # Guesstimate force based on slopes of figure 3
    FSR_g = 1 / Resistance

    # Break the parabolic curve down into two linear slopes
    if FSR_resistance <= 600:
        force = (FSR_g - 0.00075) / 0.00000032639
        return force
    else:
        force = FSR_g / 0.000000642857
        return force

# globals
 
global req_crosswalk
req_crosswalk = 0 
global req_bikelane
req_bikelane = 0
global req_street2
req_street2 = 0

# irqs

def req_crosswalk_f():
    global req_crosswalk
    req_crosswalk1 = 1

switch.irq(trigger = machine.Pin.IRQ_RISING, handler = req_crosswalk_f)

# secondary thread for irq

def secondary():
    while True:
        global req_bikelane
        global req_crosswalk
        global req_street2
    
        if(force()>0): # fsr requests
            req_bikelane = 1

        if(distance(ultra_trig, ultra_echo) <10):
            req_street2 = 1
            
            '''??? do we need and else to check if a car turns after they stopped'''
        

# primary thread

primaryThreadDelay = .02
frameCount = 0
quarterSecond = 0
halfSecondCount = 0
secondCount = 0

while True:
    # globals
    global req_bikelane
    global req_crosswalk
    global req_street2
    # frames and seconds timers
    frameCount += 1
    if frameCount % 12.5 == 0:
        quarterSecond += 1
    if frameCount % 25 == 0:
        halfSecondCount += 1
    if frameCount % 50 == 0:
        secondCount += 1
        
    '''
    if pedestrian and ??? :
        open pedestrian
        close pedestrian
        reset s
    else if bike lane and s > 120:
        open secondary street
        close secondary street
        reset s
    else if car and s > 120:
        open secondary street
            if no car in secondary lane for 10 seconds
                close secondary street
            else if s > 240
                close secondary street
    else:
        open main street
                
    '''

    
    
    time.sleep(primaryThreadDelay)
    
 
 
 
 
 
 
 
 