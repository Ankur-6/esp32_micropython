#esp32 code for dht11 sensor

import machine
import time
import dht

led = machine.Pin(2,machine.Pin.OUT)

#object for dht11

d = dht.DHT11(machine.Pin(15))

while True:
    try:
        d.measure()
        t = d.temperature()
        h = d.humidity()
        
        print("Temperature {}".format(t))
        print("Humidity {}".format(d))
        time.sleep(5)
    except Exception as e:
        print("Error",e)
        