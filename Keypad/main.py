#code for 4x4 keypad with esp32s3

import machine

rows = [machine.Pin(14), machine.Pin(11), machine.Pin(10), machine.Pin(46)]
cols = [machine.Pin(13), machine.Pin(12), machine.Pin(9), machine.Pin(3)]

keypad = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D']
]

for col_pin in cols:
    col_pin.init(machine.Pin.OUT)
    col_pin.value(1)

for row_pin in rows:
    row_pin.init(machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    for i in range(4):
        cols[i].value(0)
        for j in range(4):
            if rows[j].value() == 0:
                print(keypad[j][i])
                # You can perform actions based on the keypress here
        cols[i].value(1)
