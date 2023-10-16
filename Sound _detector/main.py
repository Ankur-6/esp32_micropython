import machine
import time

# Define the ADC pin for the sound sensor
sound_sensor_pin = machine.ADC(machine.Pin(4))

# Define the LED pin
led_pin = machine.Pin(2, machine.Pin.OUT)

# Set the threshold for sound activation
threshold = 600  # Adjust this value based on your sound sensor and environment

while True:
    sound_level = sound_sensor_pin.read()  # Read the analog value from the sound sensor

    if sound_level > threshold:
        led_pin.on()  # Turn on the LED when the sound level is above the threshold
        print("Led is turned on")
    else:
        led_pin.off()  # Turn off the LED when the sound level is below the threshold
        print("Led is turned off")
    time.sleep(4)