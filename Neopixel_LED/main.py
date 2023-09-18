#micropython script

#controlling the neopixel led

import machine
import neopixel
import time

#object for neopixel LED

np = neopixel.NeoPixel(machine.Pin(48),1)

while True:
    try:
        np[0]=[255,0,255]
        np.write()
        time.sleep(0.2)
    except KeyboardInterrupt:
        print("Exit")
        break