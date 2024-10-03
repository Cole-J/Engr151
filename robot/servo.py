import machine
import utime

class servoClass:
    def __init__(self, pin, freq):
        self.pin = pin
    
    def port(): # return GPIO port number
        return self.pin

    def create_servo_obj():
        self.servo = machine.PWM(machine.Pin(self.pin))
        self.servo.freq(self.freq)


'''
servo based functions

servo = machine.PWM(machine.Pin(15))
servo.freq(50)
'''


def write(servoObj,angle): # servo_write function
    pulse_width=interval_mapping(angle, 0, 180, 0.5,2.5)
    duty=int(interval_mapping(pulse_width, 0, 20, 0,65535))
    servoObj.duty_u16(duty)


