#fire base real time data management
#LED control using ultrasonic distance sensor
#reciever for firebase

import machine
import network
import time
import urequests
import ujson

# Initialize onboard LED (Pin 2)
led = machine.Pin(2, machine.Pin.OUT)

# Connect to Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("Boss", "123456789")  # Replace with your Wi-Fi SSID and password

while not wlan.isconnected():
    pass

print("Wi-Fi connected")

# Firebase configuration
FIREBASE_URL = "https://esp32-f4164-default-rtdb.firebaseio.com/"  # Replace with your Firebase URL
FIREBASE_API_KEY = "AIzaSyCYG_1U5z9HAQqf51ZkqxeBJPdYKD4CJnY"  # Replace with your Firebase API Key
NODE_PATH = "2"  # Node path to store button state

previous_state = -1  # Initialize to an invalid state

# Helper function to read the button state from Firebase
def read_firebase():
    auth_url = f"{FIREBASE_URL}{NODE_PATH}.json?auth={FIREBASE_API_KEY}"
    response = urequests.get(auth_url)
    data = ujson.loads(response.text)
    response.close()
    return data.get(NODE_PATH, -1)

# Helper function to update the Firebase database
def update_firebase(value):
    data = {NODE_PATH: value}
    headers = {'Content-Type': 'application/json'}
    auth_url = f"{FIREBASE_URL}{NODE_PATH}.json?auth={FIREBASE_API_KEY}"
    response = urequests.put(auth_url, data=ujson.dumps(data), headers=headers)
    response.close()

# Main loop
while True:
    current_state = read_firebase()
    
    if current_state == 1:
        led.value(1)
        update_firebase(1)
        print("LED is turned on")
    elif current_state == 0:
        led.value(0)
        update_firebase(0)
        print("LED is turned off")
