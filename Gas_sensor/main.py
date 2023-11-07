import machine
import time

# Define the pin to which the gas sensor is connected
analog_pin = machine.ADC(machine.Pin(18))

def read_gas_sensor():
    value = analog_pin.read()  # Read analog value
    return value

while True:
    gas_value = read_gas_sensor()
    print("Gas Sensor Value:", gas_value)
    time.sleep(2)  # Adjust the sleep duration as needed
