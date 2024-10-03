import machine
import utime




NOTE_E3 =  161
NOTE_E4 =  329
NOTE_D4 = 294
NOTE_G4 = 392
NOTE_B4 = 494
NOTE_A4 = 440
NOTE_C4 = 262
NOTE_B3 = 247
NOTE_G3 = 196
NOTE_D3 = 147
NOTE_E5 = 659
NOTE_D5 = 587
NOTE_A3 = 220
NOTE_FS3 = 40
NOTE_E1 = 41
NOTE_A2 = 110
a=0



melody = [NOTE_E3, NOTE_E4, NOTE_D4, NOTE_E4, NOTE_G4, NOTE_D4, NOTE_B4, NOTE_A4, NOTE_G4, NOTE_D4, NOTE_D4, NOTE_C4, NOTE_B3, NOTE_G3, NOTE_E3, NOTE_D3, NOTE_E3, NOTE_E5, NOTE_E5, NOTE_E5, NOTE_E5, NOTE_B4, NOTE_G4, NOTE_E4, NOTE_D5,NOTE_E4, NOTE_D4, NOTE_E4, NOTE_G4, NOTE_D4, NOTE_B4, NOTE_A4, NOTE_G4, NOTE_D4, NOTE_D4, NOTE_C4, NOTE_B3, NOTE_G3, NOTE_E3, NOTE_D3, NOTE_E3, NOTE_E5, NOTE_E5, NOTE_E5, NOTE_E5, NOTE_B4, NOTE_G4, NOTE_E4, NOTE_D5,NOTE_G3, NOTE_G3, NOTE_G3, NOTE_D4, NOTE_B3, NOTE_B3, NOTE_B3, NOTE_B3, NOTE_G3, NOTE_A3, NOTE_B3, NOTE_D4, NOTE_B3, NOTE_G3, NOTE_G3, NOTE_G3, NOTE_D4, NOTE_G3, NOTE_G3, NOTE_G3, NOTE_G3,NOTE_G3, NOTE_G3, NOTE_G3, NOTE_A3, NOTE_G3, NOTE_FS3, NOTE_E3,NOTE_G3, NOTE_G3, NOTE_G3, NOTE_D4, NOTE_B3, NOTE_B3, NOTE_B3, NOTE_B3, NOTE_G3, NOTE_A3, NOTE_B3, NOTE_D4, NOTE_B3, NOTE_G3, NOTE_G3, NOTE_G3, NOTE_D4, NOTE_G3, NOTE_G3, NOTE_G3, NOTE_G3,NOTE_G3, NOTE_G3, NOTE_G3, NOTE_A3, NOTE_G3, NOTE_G3, NOTE_G3, NOTE_G3,a,NOTE_E1, NOTE_A2, NOTE_E1, NOTE_E1, NOTE_E1, NOTE_E1,NOTE_E1, NOTE_A2, NOTE_E1, NOTE_E1, NOTE_E1, NOTE_E1,]

noteDurations = [6,6,6,6,3,6,6,6,6,3,6,6,6,6,6,6,6,6,6,6,6,6,6,6,2,6,6,6,3,6,6,6,6,3,6,6,6,6,6,6,6,6,6,6,6,6,6,6,2,6,6,6,2,2,6,6,6,6,8,8,8,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,2,2,6,6,6,6,8,8,8,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,2,2,1,2,4,4,1,1,1,2,4,4,1,1]


buzzer = machine.PWM(machine.Pin(16))

def tone(pin,frequency,duration):
    pin.freq(frequency)
    pin.duty_u16(30000)
    utime.sleep_ms(duration)
    pin.duty_u16(0)
    

for x in range(119):
    tone(buzzer, melody[x], noteDurations[x]*50)

'''
tone(buzzer,100,250)
utime.sleep_ms(500)
tone(buzzer,200,250)
utime.sleep_ms(500)
tone(buzzer,300,250)
utime.sleep_ms(500)
tone(buzzer,400,250)
utime.sleep_ms(500)
tone(buzzer,500,250)
utime.sleep_ms(500)
tone(buzzer,600,250)
utime.sleep_ms(500)
tone(buzzer,700,250)
utime.sleep_ms(500)
tone(buzzer,800,250)
utime.sleep_ms(500)
tone(buzzer,900,250)
utime.sleep_ms(500)
tone(buzzer,1000,250)
utime.sleep_ms(500)
tone(buzzer,1100,250)
utime.sleep_ms(500)
tone(buzzer,1200,250)
utime.sleep_ms(500)
tone(buzzer,1300,250)
utime.sleep_ms(500)
tone(buzzer,1400,250)
utime.sleep_ms(500)
tone(buzzer,1500,250)
utime.sleep_ms(500)
tone(buzzer,1600,250)
utime.sleep_ms(500)
tone(buzzer,1700,250)
'''
















