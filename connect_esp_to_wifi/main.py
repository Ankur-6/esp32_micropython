#esp connect with wifi
import network
import time
import sys
ssid = "Redmi 9 Power"
psk = "abcd3456"


try:
    #object for wlan
    wlan = network.WLAN(network.STA_IF)
    #active the wlan driver
    wlan.active(False)
    time.sleep(1)
    wlan.active(True)
    wlan.connect(ssid,psk)
    timeout = 10
    t = 0
    while (timeout-t > 0)and(wlan.isconnected() == False):
        t += 1
        print(t)
        time.sleep(1)
    if wlan.isconnected() == True:
        print("connected with wifi")
        print(wlan.ifconfig())
    else:
        print("Timeout, could not connect")
except Exception as e:
    print(f"error > {e}")
    
sys.exit()
        