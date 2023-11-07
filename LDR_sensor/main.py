#code for ldr sensor with esp32s3 for neopixel led

import machine
import neopixel
import time

# Define the LDR module and NeoPixel LED pins
LDR_PIN = machine.ADC(machine.Pin(18))
np = neopixel.NeoPixel(machine.Pin(48), 1)  # 1 NeoPixel LED connected to GPIO pin 13

while True:
    # Read the LDR value
    ldr_value = LDR_PIN.read()

    # Map the LDR value to an RGB color
    r = int((ldr_value / 4095) * 255)
    g = 255 - r
    b = 0

    # Set the NeoPixel LED color
    np[0] = (r, g, b)
    np.write()

    # Print the LDR value to the console
    print("LDR Value:", ldr_value)

    # Sleep for a short time to avoid rapid value changes
    time.sleep(1)