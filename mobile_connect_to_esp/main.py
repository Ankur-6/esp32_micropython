#mobile connect to esp
import network
import time
import sys

try:
    #object for wlan
    wlan = network.WLAN(network.AP_IF)
    #active the wlan driver
    wlan.active(False)
    time.sleep(1)
    wlan.active(True)
    wlan.config(essid ="triesp", password="priyam@123", authmode=network.AUTH_WPA_WPA2_PSK)
    #scan nearby networks
    networks = wlan.scan()
    #print the available networks
  #  print(networks)
except Exception as e:
    print(f"error > {e}")
    
sys.exit()