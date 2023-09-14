#micropython script for ESP32

#blink the two leds together

from machine import Pin
from time import sleep

#create object for led pin

led1 = Pin(2,Pin.OUT)
led2 = Pin(4,Pin.OUT)

led1_state = True
led2_state = False

while True:
    if True():
        led1_state=not led1_state
        led1.value(led1_state)
        sleep(0.2)
    else:
        led2_state=not led2_state
        led2.value(led2_state)
        sleep(0.2)
        

    
    
    