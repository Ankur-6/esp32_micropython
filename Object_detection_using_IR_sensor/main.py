import machine
import time

# Define the GPIO pin for the IR sensor
ir_sensor_pin = machine.Pin(18)  # Replace with the appropriate GPIO pin

# Initialize a counter
object_count = 0

# Variable to track the previous state of the IR sensor
previous_state = 0

while True:
    # Read the current state of the IR sensor
    current_state = ir_sensor_pin.value()
    
    # Check for a change in state (object detected or not detected)
    if current_state != previous_state:
        if current_state == 0:
            object_count += 1
            print("Object detected. Count:", object_count)
            time.sleep_ms(500)
        previous_state = current_state
