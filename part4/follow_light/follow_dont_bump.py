import explorerhat
import time
from ultrasonic import *
ultrasonic1 = ultrasonic_sensor(6, 23)
ultrasonic1.setup()

bump_buffer_cm = 20

def get_percentage(left, right):
   if(left > right):
      return (20, 50, "<")
   return (50, 20, ">")

def escape():
    backup_time = 0.3
    turn_time = 0.15
    explorerhat.motor.one.backwards(50)
    explorerhat.motor.two.backwards(50)
    time.sleep(backup_time)
    explorerhat.motor.two.forwards(50)
    time.sleep(turn_time)

while(True):
    if(ultrasonic1.measure(0.10) <= bump_buffer_cm):
        explorerhat.motor.one.stop()
        explorerhat.motor.two.stop()

        escape()

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

