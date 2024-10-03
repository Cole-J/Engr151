'''
Want to see how the temperature changes by my window as the sun goes down, I set it up at 2 and let it run
for a while looping every 10 minutes.

this main file is the same as the lab 6 task 1 with a few changes. those changes are to give a bit of input
so I know its running and changing the time of each loop. the lab 6 going farther file is the same as lab 6 task 2
with some changes to the graph.
'''

import machine
import utime
import math

therm = machine.ADC(28) # creates the adc pin object for the thermistor input
led = machine.Pin("LED", machine.Pin.OUT) # done on a pico w so different pins
led.value(1) # show that the board is on / program is running

def ReadTemperature(): # function to read the resistance from the thermistor and convert it to a temp value
    # returns the temp value in cel
    temperature_value = therm.read_u16() # reads value
    Vr = 3.3 * float(temperature_value) / 65535
    Rt = 10000 * Vr / (3.3 - Vr)
    temp = 1/(((math.log(Rt / 10000)) / 3950) + (1 / (273.15+25))) # convert to temp
    Cel = temp - 273.15
    print(Cel)
    return Cel # return temp

f = open('thermData.txt', 'w') # opens the folder in write mode

def writefiledata(t, x): # file to write 2 integers to a text file
    # first (t) is the time and second (x) is the int or float value
    time = str(t) # converts both to strings 
    value = str(round(x, 2)) # rounds the x value before converting it to a string
    f.write(time + "\t" + value) # passes a string formated, 'time    value' as \t is to add a tab or 4 spaces
    f.write("\n") # adds and enter / goes to the next line
    f.flush()

k = 0 # count variable to count how many loops have passed
Ts = 600 # delay of each loop, 10 minutes
while True:
    degC = ReadTemperature() # gets the current temp
    writefiledata(k*Ts, degC) # calls writefiledata function with the parameters k*Ts which is how much time has
    # passed and degC which is the current temp measured by thetermistor
    k = k + 1 # adds 1 to k
    utime.sleep(Ts) # delay for Ts 