#code for pis sensor with esp32s3

import machine
import time

# Create objects for PIR sensor and relay
pir_pin = machine.Pin(17, machine.Pin.IN)
relay_pin = machine.Pin(18, machine.Pin.OUT)
#potentiometer_pin = machine.ADC(machine.Pin(32))  # ADC pin for potentiometer

relay_pin.off()  # Make sure the relay is initially off

def activate_solenoid():
    while True:
        #sensitivity = potentiometer_pin.read()  # Read the potentiometer value
        if pir_pin.value() == 1:  # Check the value of the PIR pin
            print("Motion Detected")
            print("Activating Solenoid")
            relay_pin.on()  # Turn on the relay and activate the solenoid
            print("Solenoid activated")
            time.sleep(2)   # Wait for 5 seconds
            print("Deactivating the Solenoid")
            relay_pin.off()  # Turn off the relay and deactivate the solenoid
            print("Solenoid Deativated")
        time.sleep(2)

if __name__ == "__main__":
    activate_solenoid()
