#micropython script for ESP32

#blink the two leds together

from machine import Pin
from time import sleep

#create object for led pin

led1 = Pin(2,Pin.OUT)
led2 = Pin(4,Pin.OUT)

#function to toggle the state of the LEDs

def toggle_leds():
    led1.value(not led1.value())
    led2.value(not led2.value())
    
    
#blink the LEDs in a loop
while True:
    toggle_leds()
    sleep(0.2)
