import network
import time
import sys
ssid = "Redmi 9 power"
psk = "abcd3456"

try:
    #object for wlan
    wlan = network.WLAN(network.STA_IF)
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