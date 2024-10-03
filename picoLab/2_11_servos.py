'''
in the while true it is trying to turn the servo from 0 to 180 degrees. to do this it uses the interval mapping function to first
get the puslse width of the current (mapped from 0 - 180 to .5 - 2.5) an then mapped from the pulse width to the duty, getting how
much voltage is being sent every 20 ms for each degree (ish) that it needs to move.
'''
import machine
import utime

servo = machine.PWM(machine.Pin(12)) # sets the servo / output to pin 15
servo.freq(50) # sets the freq of the out signal to 50 hz / one period every 20 ms about

def interval_mapping(x, in_min, in_max, out_min, out_max): # interval mapping function
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def servo_write(pin,angle):
    pulse_width=interval_mapping(angle, 0, 180, 0.5,2.5) # maps the angle to be between .5ms and 2.5ms for the servo
    # that gets you the width of the pulse
    duty=int(interval_mapping(pulse_width, 0, 20, 0,65535)) # use pulse width to get the duty
    # int() gets rid of decimals 
    pin.duty_u16(duty) # sets the duty to the servo pins duty
    # remember that this is done for each degree

while True:
    for angle in range(180): # angle starts at 0 and goes to 180
        servo_write(servo,angle)
        utime.sleep_ms(20) # short delay
    for angle in range(180,-1,-1): # angle starts at 180 and goes to 0
        servo_write(servo,angle)
        utime.sleep_ms(20)
    # the for loops causes servo to go to 0 to 180, then back to 0
    # the while loop loops the 2 nested for loops