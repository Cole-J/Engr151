import machine
import utime

out = machine.Pin(15, machine.Pin.OUT)

out.value(1)
utime.sleep(1)
out.value(0)