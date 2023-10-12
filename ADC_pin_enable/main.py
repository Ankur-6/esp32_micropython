import machine

adc = machine.ADC(machine.Pin(4))  # Pin number for ADC
value = adc.read()
print("ADC Value:", value)