import machine
import utime

potentiometer = machine.ADC(27) # creates the potentiometer object using the anolog input pin 28
led = machine.PWM(machine.Pin(15)) # sets the pin for the led using PWM
led.freq(1000) # hz freq for PWM

while True:
    value=potentiometer.read_u16() # reads the value of the potentiometer with the range of 0 - 65535
    print(value)
    led.duty_u16(value) # sets the led to the value of the potentiometer
    utime.sleep_ms(200) # delay 200 ms