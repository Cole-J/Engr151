'''
this program has 2 parts, the main loop, and the irq.

the main loop steadily increases the led brightness and buzzer tone when bell_flag is true and when its
false it turns off the led and the buzzer.

the irq calls the toggle function when pressed it swaps the bool variable bell_flag and seems a bit overkill compared to
what could be used in this situation.
'''
import machine # imports
import time


buzzer = machine.PWM(machine.Pin(15)) # defines the outputs
led = machine.PWM(machine.Pin(16))
led.freq(1000)

switch = machine.Pin(17,machine.Pin.IN) # defines the inputs

def noTone(pin): # a function to set a pins duty to 0
    pin.duty_u16(0)


def tone(pin,frequency): # function to set a pins freq and sets its duty to 50%
    pin.freq(frequency)
    pin.duty_u16(30000)

def interval_mapping(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def toggle(pin): # a callback function able to toggle bell_flag via recursion
    # why is pin being passed if its not used?
    global bell_flag
    bell_flag = not bell_flag # toggles bell_flag (bell_flag is a bool)
    print(bell_flag)
    if bell_flag:
        switch.irq(trigger=machine.Pin.IRQ_FALLING, handler=toggle)
    else:
        switch.irq(trigger=machine.Pin.IRQ_RISING, handler=toggle)


bell_flag = False
switch.irq(trigger=machine.Pin.IRQ_RISING, handler=toggle) # sets up the irq using the built in irq handler



while True:
    if bell_flag == True:
        for i in range(0,100,2):
            led.duty_u16(int(interval_mapping(i,0,100,0,65535))) # increasing brightness led
            tone(buzzer,int(interval_mapping(i,0,100,130,800))) # increasing tone buzzer
            time.sleep_ms(10)
    else: # when bell_flag is false it turns off the led and buzzer
        noTone(buzzer)
        led.duty_u16(0)