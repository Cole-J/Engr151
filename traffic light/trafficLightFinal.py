import machine
from machine import time_pulse_us
import utime
import _thread
import time

#lights

street1_led_green = machine.Pin(4,machine.Pin.OUT)
street1_led_yellow = machine.Pin(3, machine.Pin.OUT)
street1_led_red = machine.Pin(2, machine.Pin.OUT)

street2_led_green = machine.Pin(7, machine.Pin.OUT)
street2_led_yellow = machine.Pin(6, machine.Pin.OUT)
street2_led_red = machine.Pin(5, machine.Pin.OUT)

croswalk_led1 = machine.Pin(0, machine.Pin.OUT)
croswalk_led2 = machine.Pin(1, machine.Pin.OUT)

buzzer = machine.PWM(machine.Pin(10))

#sensors

FSR = machine.ADC(28)

ultra_trig = machine.Pin(17, machine.Pin.OUT) 
ultra_echo = machine.Pin(16, machine.Pin.IN)

# switches

switch = machine.Pin(8, machine.Pin.IN)

# functions

def interval_mapping(x, in_min, in_max, out_min, out_max):
    if (in_min > x):
        return out_min
    elif (in_max < x):
        return out_max
    else:
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

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

#buzzer

def tone(pin,frequency, duty):
    pin.freq(frequency)
    pin.duty_u16(duty)

# globals
 
global req_crosswalk
req_crosswalk = 0 
global req_street2
req_street2 = 0
global mainOpen
mainOpen = False
global secoOpen
secoOpen = False

# secondary thread for fsr and ultra readings

def secondary():
    while True:
        global req_street2
        global req_crosswalk
    
        if(force()>0) or (distance(ultra_trig, ultra_echo) < 10): # fsr and ultra requests
            req_street2 = 1
            print("rs")
        if switch.value() == 1:
            req_crosswalk = 1
            print("rc")
        utime.sleep_ms(20)
        
_thread.start_new_thread(secondary, ())

primaryThreadDelay = .02
frameCount = 0
secondCount = 0



while True:
    # globals
    global mainOpen
    global secoOpen
    global req_crosswalk
    global req_street2
    # frames and seconds timers
    frameCount += 1
    if frameCount % 50 == 0:
        secondCount += 1
    
    if req_crosswalk == 1 and secondCount > 0:
        print("cw op")
        if mainOpen == True:
            set_street_led(1,0,1,0)
            utime.sleep(1)
            set_street_led(1,1,0,0)
        if secoOpen == True:
            set_street_led(2,0,1,0)
            utime.sleep(1)
            set_street_led(2,1,0,0)
        # now both lanes are closed
        mainOpen = False
        secoOpen = False
        for x in range(5):
            tone(buzzer, 500, 30000)
            croswalk_led1.value(1)
            croswalk_led2.value(1)
            utime.sleep(1)
            tone(buzzer, 500, 0)
            croswalk_led1.value(0)
            croswalk_led2.value(0)
            utime.sleep(1)
            
        secondCount = 0
        req_crosswalk = 0
        
    elif req_street2 == 1 and secondCount > 0:
        print("ss op")
        if mainOpen == True:
            set_street_led(1,0,1,0)
            utime.sleep(1)
            set_street_led(1,1,0,0)
            utime.sleep(1)
        mainOpen = False
        secoOpen = True
        set_street_led(2,0,0,1)
        utime.sleep(5)
        
        secondCount = 0
        req_street2 = 0
    else:
        #utime.sleep(1)
        if req_crosswalk == 0 and req_street2 == 0:
            if secoOpen == True:
                set_street_led(2,0,1,0)
                utime.sleep(1)
                set_street_led(2,1,0,0)
                utime.sleep(1)
                secoOpen = False
            mainOpen = True
            set_street_led(1,0,0,1)
            print("ms op")

    time.sleep(primaryThreadDelay)