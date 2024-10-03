'''
in this circuit the thermistor gives an adc input in 0-3.3v. the pico is then taking that input and converting it
to celsius using the ReadTemperature function (which returns the temp)

the other function, writefiledata takes 2 inputs (1 int and 1 float) and writes them to the thermData.txt file.
it does this by converting both parameters to strings. it then writes the string to the file, goes to the next line
using \n, and the flushes the file.
(flushing will act like f.close without actually closing the file as it gets rid of the buffer / updates the file.
i does this by writing the current RAM data to the disk, or flushing the RAM)
'''

import machine
import utime
import math

therm = machine.ADC(28) # creates the adc pin object for the thermistor input

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
Ts = 5 # delay of each loop
while True:
    degC = ReadTemperature() # gets the current temp
    writefiledata(k*Ts, degC) # calls writefiledata function with the parameters k*Ts which is how much time has
    # passed and degC which is the current temp measured by thetermistor
    k = k + 1 # adds 1 to k
    utime.sleep(Ts) # delay for Ts 