#multiple LEDs fade using PWM

from machine import Pin, PWM
from time import sleep_ms

class LEDfader:
    def __init__(self,pin,pwm):
        self.pin = pin
        
        