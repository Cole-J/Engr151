'''
the tone function is given the parameters pin frequency and duration. the duty is at 50% so the pulse is on 50% of the time.
the frequency (in hz) is the actual frequency that will be outputed. the duration is then the amount of time that tone 
will play (in ms).
'''
import machine # imports
import utime

buzzer = machine.PWM(machine.Pin(15)) # sets the buzzer to pin 15

def tone(pin,frequency,duration): # creates the function
    pin.freq(frequency) # sets the frequency of the current going out in hz
    pin.duty_u16(30000) # has the duty be 50% on 50% off
    utime.sleep_ms(duration) # sleeps
    pin.duty_u16(0) # turns off the buzzer (duty is 100% off)

tone(buzzer,440,250) # set the freq to 440 hz for 250 ms
utime.sleep_ms(500) # waits 500 ms
tone(buzzer,494,250) # set the freq to 494 hz for 250 ms
utime.sleep_ms(500) # waits 500 ms
tone(buzzer,523,250) # set the freq to 523 hz for 250 ms