import machine
import utime

led_pin = Pin(2, Pin.OUT)
led = Signal(led_pin, invert=True)

def blink_3_times():
    led.off(1)
    for i in range (3):
        utime.sleep(1)
        led.on()
        utime.sleep(1)
        led.off()

        
