#micropython script

#led blinking script

import machine
import time

#create object for led pin

#led_pin = machine.Pin(8,machine.Pin.OUT)

led = machine.Pin(8,machine.Pin.OUT)

while True:
    try:
        '''led_pin.on()
        #led_pin.value(1)
        print("LED is on")
        time.sleep(1)
        led_pin.off()
        #led_pin.value(0)
        print("LED is off")
        time.sleep(1)'''
        led.value(not led.value())
        print("LED is on" if led.value() else "LED is off")
        time.sleep(1)
    except KeyboardInterrupt:
        print("Exit")
        break
    