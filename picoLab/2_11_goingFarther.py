'''
'''
import machine
import utime
import _thread

# port definitions (p)

p_led_white = machine.Pin(13, machine.Pin.OUT)
p_led_blue = machine.Pin(14, machine.Pin.OUT)
p_buzzer = machine.PWM(machine.Pin(15))
p_servo = machine.PWM(machine.Pin(12))
p_servo.freq(50)

# variables

'''
notes c3-b3 and c4-b4 for octives 3 and 4
'''
# octive 3
note_c3 = 131
note_d3 = 147
note_e3 = 165
note_f3 = 175
note_g3 = 196
note_a3 = 220
note_b3 = 247
# octive 4
note_c4 = 262
note_d4 = 294
note_e4 = 330
note_f4 = 349
note_g4 = 392
note_a4 = 440
note_b4 = 494

note_fs3 = 185
note_ds4 = 394

midHz = 255 # the hz number between octive 3 and 4

buzzer_duty = 30000 # the duty of the buzzer

# melody array
melody = [[note_c4, note_c4, note_b3, note_b3, note_e3, note_g3, note_e3, note_e3, note_c4, note_c4, note_b3, note_b3, note_e3,     
           note_c4, note_c4, note_b3, note_b3, note_e3, note_g3, note_e3, note_g3, note_a3, note_fs3, note_g3, note_e3,     
           note_c4, note_c4, note_b3, note_b3, note_e3, note_g3, note_e3, note_e3, note_c4, note_c4, note_b3, note_b3, note_e3,     
           note_c4, note_c4, note_b3, note_b3, note_e3, note_g3, note_e3, note_g3, note_a3, note_fs3, note_g3, note_e4,              
           
           note_b3, note_c4, note_b3, note_b3, note_d3, note_e4, note_d3, note_c4, note_b3, note_c4, note_b3, note_a3, note_g3, note_g3,    
           note_a3, note_b3, note_a3, note_b3, note_c4, note_d3, note_b3, note_a3, note_b3, note_c4, note_e4, note_ds4, note_c3, note_c3], # note hz

          [100, 100, 100, 100, 100, 50, 150, 100, 100, 100, 100, 100, 400,      
           100, 100, 100, 100, 100, 100, 200, 100, 100, 100, 100, 300,    
           100, 100, 100, 100, 100, 50, 150, 100, 100, 100, 100, 100, 400,      
           100, 100, 100, 100, 100, 100, 200, 100, 100, 100, 100, 300,             
           
           100, 100, 100, 100, 100, 50, 150, 100, 100, 100, 100, 100, 200, 100,    
           100, 100, 100, 100, 100, 50, 150, 100, 100, 100, 100, 200, 200, 200], # note duration in ms

          [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,     
           100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 200,    
           100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,     
           100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 200,             
           
           100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 200, 100,   
           100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 300]] # rest in ms

# global variables

global voctive
voctive = 0 # variable to keep track of the curret octive for the servo movement


# functions

def octive(para_noteHz, para_mid = midHz):
    # function to return what octive a note is in by checking what its freq is compared to the midpoint
    if para_noteHz > para_mid:
        return 4
    else:
        return 3

def tone(para_buzzer, para_hz, para_duration, para_rest = 0):
    para_buzzer.freq(para_hz)
    para_buzzer.duty_u16(30000)
    utime.sleep_ms(para_duration)
    para_buzzer.duty_u16(0)
    utime.sleep_ms(para_rest)

# servo

def interval_mapping(x, in_min, in_max, out_min, out_max): # interval mapping function
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def servo_write(pin,angle):
    pulse_width=interval_mapping(angle, 0, 180, 0.5,2.5) # maps the angle to be between .5ms and 2.5ms for the servo
    # that gets you the width of the pulse
    duty=int(interval_mapping(pulse_width, 0, 20, 0,65535)) # use pulse width to get the duty
    # int() gets rid of decimals 
    pin.duty_u16(duty) # sets the duty to the servo pins duty
    # remember that this is done for each degree

def servo():
    print("\nstarting secondary thread")
    prev_voctive = 2 # variable to save the previous octive variable to check for only new inputs
    while True:
        if prev_voctive != voctive: # if its a new voctive input
            if voctive == 3: # octive 3
                for angle in range(0, 180, 1):
                    servo_write(p_servo,angle)
                    utime.sleep_ms(1) # short delay
            elif voctive == 4: # octive 4
                for angle in range(180, -1, -1):
                    servo_write(p_servo,angle)
                    utime.sleep_ms(1) # short delay

        if voctive == 1: # voctive == 1 indicates that the program is done and shutting off
            break # breaks the secondary threads loop to prevent errors
        prev_voctive = voctive
        utime.sleep(.02)
    print("secondary thread off")
_thread.start_new_thread(servo, ())

print("starting main")
for num in range(len(melody[0])):
    note_hz = melody[0][num]
    note_duration = melody[1][num]
    note_rest = melody[2][num]

    if octive(note_hz) == 3:
        voctive = 3
        p_led_blue.value(0)
        p_led_white.value(1)
    else:
        voctive = 4
        p_led_white.value(0)
        p_led_blue.value(1)

    tone(p_buzzer, note_hz, note_duration, note_rest)

# shutdown

print("done with main, shutting down")
voctive = 1
utime.sleep(1) # gives some time for the secondary thread to shut down to prevent core1 active error
p_led_blue.value(0)
p_led_white.value(0)
p_buzzer.duty_u16(0)
p_servo.duty_u16(0)
print("off")