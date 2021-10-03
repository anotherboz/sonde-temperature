import machine
import utime

led = machine.Pin(2, machine.Pin.OUT)
while(1):
    led.value(1)
    utime.sleep(1)
    led.value(0)
    utime.sleep(1)
