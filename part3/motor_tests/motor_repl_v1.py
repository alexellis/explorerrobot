import sys, time
from motors_v1 import Motors

last = None
motors = Motors()
move_delay = 1
turn_delay = 0.5

def evaluate(line):
    if(line == "w"):
        motors.forwards()
        time.sleep(move_delay)
        motors.stop()
    if(line == "a"):
        motors.left()
        time.sleep(turn_delay)
        motors.stop()
    if(line == "s"):
        motors.backwards()
        time.sleep(move_delay)
        motors.stop()
    if(line == "d"):
        motors.right()
        time.sleep(turn_delay)
        motors.stop()

while(last != 'q'):
    sys.stdout.write("Command: ")
    sys.stdout.flush()
    last = raw_input()
    evaluate(last)
