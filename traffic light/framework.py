import machine
#from lcd1602 import LCD
import time
import utime

import _thread


def interval_mapping(x, in_min, in_max, out_min, out_max):
    if (in_min > x):
        return out_min
    elif (in_max < x):
        return out_max
    else:
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min




class create_traffic_light:
    
    def __init__(self, __red_led_pin, __yellow_led_pin, __green_led_pin):
        self.__red_led_pin = __red_led_pin
        self.__yellow_led_pin = __yellow_led_pin
        self.__green_led_pin = __green_led_pin # sets each passed pin as its own variable in the class
        
        self.__redLED = machine.Pin(self.__red_led_pin, machine.Pin.OUT) # sets each led as its own variable in the calss bassed off the passed pins
        self.__yelLED = machine.Pin(self.__yellow_led_pin, machine.Pin.OUT)
        self.__greLED = machine.Pin(self.__green_led_pin, machine.Pin.OUT)
        
    def __set(r, y, g): # sets the r, y, and g leds to a given value
        self.__redLED.value(r)
        self.__yelLED.value(y)
        self.__greLED.value(g)
        
    def STOP(self): # stop light, red only
        __set(1,0,0)
    def SLOW(self): # slow light, yellow only
        __set(0,1,0)
    def GO(self): # go / green light, green only
        __set(0,0,1)
        
class create_pedestrian_light:

    def __init__(self, __ledpin, __buzzerpin, __ledpin1, __ledpin2):
        self.__lcd = LCD(ledpin1, ledpin2)
        self.__buzzer = machine.PWM(machine.Pin(self.__buzzerpin))
        self.__led = machine.Pin(self.__ledpin, machine.Pin.OUT)
        
    def ledON(self):
        self.__led.value(1)
    def ledOFF(self):
        self.__led.value(0)
    def ledToggle(self):
        if self.__led.value() == 0:
            self.__led.value(1)
        else:
            self.__led.value(0)
            
    def lcd(self, message):
        self.__lcd.message(message)
    def clearlcd(self):
        self.__lcd.clear()

class create_ultra:
    
    def __init__(self, __trig_pin, __echo_pin, __SOUND_SPEED = 340, __TRIG_PULSE_DURATION_US = 10):
        self.__trig_pin = __trig_pin
        self.__echo_pin = __echo_pin
        self.__SOUND_SPEED = __SOUND_SPEED
        self.__TRIG_PULSE_DURATION_US = __TRIG_PULSE_DURATION_US
        
    def get_nonasync_distance_cm(self):
        __trig_pin.value(0)
        time.sleep_us(10)
        
        __trig_pin.value(1)
        time.sleep_us(__TRIG_PULSE_DURATION_US)
        __trig_pin.value(0)
        
        self.__ultrason_duration = time_pulse_us(__echo_pin, 1, 30000)
        self.__distance_cm = __SOUND_SPEED * __ultrason_duration / 20000

        return self.__distance_cm  

class create_fsr:

    def __init__(self, __pin, __base_volt = 3.3, __resistance = 3230, __min_duty = 0, __max_duty = 65535):
        self.__pin = __pin
        self.__base_volt = __base_volt
        self.__resistance = __resistance
        self.__min_duty = __min_duty
        self.__max_duty = __max_duty
        
        self.__fsr = machine.ADC(self.__pin)
        
    def value(self):
        self.__fsr_value = __fsr.read_u16()
        __out_volt = interval_mapping(self.__fsr_value, self.__min_duty, self.__max_duty, 0, self.__volt)
        
        __fsr_resistance = __resistance * (__base_volt / __out_volt - 1)
        
        # check if we need the fsr_g or if the fsr_r is enough
        
'''
    print("Resistance:", FSR_resistance, "ohms.")

    # Guesstimate force based on slopes of figure 3
    FSR_g = 1 / Resistance

    # Break the parabolic curve down into two linear slopes
    if FSR_resistance <= 600:
        force = (FSR_g - 0.00075) / 0.00000032639
    else:
        force = FSR_g / 0.000000642857

    print("Force:", force, "g.")
'''

class create_thread:
    
    def __init__(self, __thread_function):
        self.__thread_function = __thread_function
        
    def start(self):
        _thread.start_new_thread(__thread_function, ())

class create_irq:
    pass










































