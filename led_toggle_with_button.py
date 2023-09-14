#Micropython script for ESP32

#toggle the state of the led with each button press

from machine import Pin

#create object for led Pin

led = Pin(2,Pin.OUT)

#create object for button pin

button = Pin(0,Pin.IN)

#run forever

while True:
    if not button.value():
        led.value(not led.value())
        print("LED turned on" if led.value() else "LED turned off")
        
        #wait till the button is pressed
        while not button.value():
            pass