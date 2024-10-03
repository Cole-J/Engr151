import machine
import utime
import math

thermistor = machine.ADC(28) # makes the thermistor object connected 

while True:
    temperature_value = thermistor.read_u16() # reads the value with the domain 0 - 65535
    Vr = 3.3 * float(temperature_value) / 65535 #converts 0 - 65535 domain of the termistor to cel and fah degrees
    Rt = 10000 * Vr / (3.3 - Vr)
    temp = 1/(((math.log(Rt / 10000)) / 3950) + (1 / (273.15+25)))
    Cel = temp - 273.15 # convert to cel
    Fah = Cel * 1.8 + 32 # convert from cel to F
    print ('Celsius: %.2f C  Fahrenheit: %.2f F' % (Cel, Fah)) # prints the numbers rounded to the second decimal place
    utime.sleep_ms(200) # delay 200 ms