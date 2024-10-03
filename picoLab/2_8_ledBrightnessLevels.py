import machine
import utime

led = machine.PWM(machine.Pin(15)) # sets pin 15 to PWM output
led.freq(1000) # sets frequency to 1000hz

for brightness in range(0,65535,50): # calls each number from 0 to 65535 in increments of 50
    led.duty_u16(brightness) # sets the led to a given brightness
    utime.sleep_ms(10) # delay in ms rather than s
    print(brightness) # added this so that I could see the brightness count
led.duty_u16(0) # turns the led off when the for loop ends