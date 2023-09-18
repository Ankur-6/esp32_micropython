#micropython script for ESP32

#blink the two leds together

from machine import Pin
from time import sleep

#create object for led pin

led1 = Pin(2,Pin.OUT)
led2 = Pin(4,Pin.OUT)

led1_state = True
led2_state = False
