import machine

class create_motor:
    def __init__(self, pin):
        self.pin = pin
        self.motor = machine.Pin(self.pin, machine.Pin.OUT)

    def move(self):
        self.motor.value(1)
    def stop(self):
        self.motor.value(0)
    def value(self):
        return self.motor.value()