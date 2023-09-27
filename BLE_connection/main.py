import ubluetooth as bluetooth

ble = bluetooth.BLE()

ble.active(True)

# Example advertisement data
adv_data = bytearray(
    b'\x02\x01\x06' +   # Flags indicating BLE general discoverable mode
    b'\x03\x03\x12\x18' +  # Complete list of 16-bit Service UUIDs (Generic Access Service UUID)
    b'\x0A\x09MyDevice'  # Local name of the device (change "MyDevice" to your desired name)
)

ble.gap_advertise(100, adv_data, connectable=True)

while True:
    pass  # Add your code here if needed
