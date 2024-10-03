import machine
import utime as ut

class create_song:
    
    def __init__(self, pin, melodyArr, durationArr):
        self.melodyArr = melodyArr
        self.durationArr = durationArr
        
        self.pin = pin
        self.buzzer = machine.PWM(machine.Pin(self.pin))
        
    def __tone__(frequency, duration):
        self.buzzer.freq(frequency)
        self.buzzer.duty_u16(30000)
        ut.sleep_ms(duration)
        self.buzzer.duty_u16(0)
    
    def play(self):
        for x in len(melodyArr):
            __tone__(self.melodyArr[x], self.durationArr[x])