import explorerhat
import time
from ultrasonic import *

def get_percentage(left, right):
   if(left > right):
      return (20, 50, "<")
   return (50, 20, ">")

while(True):
    left = explorerhat.analog.one.read()
    right = explorerhat.analog.two.read()

    tolerance = 0.10
    delta = abs(left - right)
    if(delta >= tolerance):
        percentage_power = get_percentage(left, right)
        explorerhat.motor.two.forwards(percentage_power[0])
        explorerhat.motor.one.forwards(percentage_power[1])
        print(percentage_power[2])
    else:
        percentage_power = (50, 50)
        print("^")
        explorerhat.motor.two.forwards(percentage_power[0])
        explorerhat.motor.one.forwards(percentage_power[1])

    time.sleep(0.1)

