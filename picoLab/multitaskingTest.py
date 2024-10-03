import machine
import utime
import _thread # import thread library




def button_thread(): # secondary thread function
    while True:
        print("t")
        utime.sleep(.02)
_thread.start_new_thread(button_thread, ()) # starts the second thread

while True: # starts the main thread
    
    # default sequence
    print("m")
    utime.sleep(1)
