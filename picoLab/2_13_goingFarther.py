import machine
import utime
import math

# defines leds / visual output
led_g = machine.Pin(13,machine.Pin.OUT)
led_y = machine.Pin(14,machine.Pin.OUT)
led_r = machine.Pin(15,machine.Pin.OUT)
# defines inputs
therm = machine.ADC(28)
poten = machine.ADC(27)
# constants
thresholdPercent = 0.9 # the percent that the yellow light turns on at
midPoint = 70 # in farenheight
# the poten range will be the mid +/- 50
# ex: for midpoint 70 the min is 20 and max is 120

def getFah(thermistor): # function made with code from 2.13
    # gets the temp in Fah when called
    # pass an ADC to the function
    temperature_value = thermistor.read_u16() # reads the value with the domain 0 - 65535
    Vr = 3.3 * float(temperature_value) / 65535 #converts 0 - 65535 domain of the termistor to cel and fah degrees
    Rt = 10000 * Vr / (3.3 - Vr)
    temp = 1/(((math.log(Rt / 10000)) / 3950) + (1 / (273.15+25)))
    Cel = temp - 273.15
    Fah = Cel * 1.8 + 32
    return Fah # returns fah temperature when called

while True: # main loop
    fah = getFah(therm) # gets current temp in fah
    
    potenValue = poten.read_u16() # gets poten value
    
    desiredTemp = potenValue/655-50+midPoint # converts the poten output to a range of 20-120 F (or 70 +/- 50)
    
    print('desired: %.f actual: %.f' % (desiredTemp,fah)) # print to shell for testing
    
    # green on when below desired temp
    # yellow when below desired temp AND within 10% of the desired temp
    # red on above the desired temp
    if (fah < desiredTemp): # below desired temp
        led_r.value(0) # r off
        led_g.value(1) # g on
        
        if (fah > desiredTemp * thresholdPercent): # if temp is above a given % of the desired
            led_y.value(1) # y turns on
        else:
            led_y.value(0) # off when no within given %
        
    else: # above desired temp
        led_g.value(0) # g and y off
        led_y.value(0)
        led_r.value(1) # r on
    
    utime.sleep_ms(200) # delay for 200 ms