#two leds consecutively

import machine
import time

#variable
Led_state1 = 0
Last_change1 = 0
Led_state2 = 0
Last_change2 = 0

def led1_toggle(pin1,on_time,off_time):
    global Led_state1
    global Last_change1
    #create object for led1
    Led1 = machine.Pin(pin1,machine.Pin.OUT)
 
    if (time.ticks_ms()-Last_change1)>=off_time and Led_state1 is 0:
        Last_change1 = time.ticks_ms()
        Led_state1 = 1
        Led1.value(Led_state1)
        print("LED1 is on")
    elif (time.ticks_ms()-Last_change1)>=on_time and Led_state1 is 1:
        Last_change1 = time.ticks_ms()
        Led_state1 = 0
        Led1.value(Led_state1)
        print("LED1 is off")
def led2_toggle(pin2,on_time,off_time):
      global Led_state2
      global Last_change2
      #object for led2
      Led2 = machine.Pin(pin2,machine.Pin.OUT)
      if(time.ticks_ms()-Last_change2)>=on_time and Led_state2 is 0:
        Last_change2 = time.ticks_ms()
        Led_state2 = 1
        Led2.value(Led_state2)
        print("LED2 is on")
      elif(time.ticks_ms()-Last_change2)>=off_time and Led_state2 is 1:
        Last_change2 = time.ticks_ms()
        Led_state2 = 0
        Led2.value(Led_state2)
        print("LED2 is off")
        
while True:
    try:
        led1_toggle(2,500,900)
        led2_toggle(4,1000,1500)
    except KeyboardInterrupt:
        print("Exit")
        break
