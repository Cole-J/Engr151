import machine
import utime

from notes import melody

class create_tone:
    
    def __init__(self, pin, duty):
        self.pin = pin
        self.duty = duty
        self.playTone = False
        self.playingTone = False

        self.buz = machine.PWM(machine.Pin(self.pin))

    def play(self):
        self.playTone = True
        self.playingTone = True
        for num in range(len(melody)):
            if self.playTone == True:
                note_hz = melody[0][num] # gets the hz, duration, and rest
                note_duration = melody[1][num]
                note_rest = melody[2][num]

                tone(self.buz, note_hz, note_duration, note_rest) # plays the tone
            else:
                break
        self.playingTone = False

    def isPlaying(self):
        if self.playingTone:
            return True
        else:
            return False
        
    def stop(self):
        self.playingTone = False
        self.playTone = False

def tone(para_buzzer, para_hz, para_duration, para_rest = 0): # plays a given hz for a given duration
    para_buzzer.freq(para_hz) # sets the freq in hz
    para_buzzer.duty_u16(30000) # sets duty to about 50% on
    utime.sleep_ms(para_duration) # waits
    para_buzzer.duty_u16(0) # stops by setting duty to 0%
    utime.sleep_ms(para_rest) # waits again