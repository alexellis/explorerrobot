import sys, time
from motors_v1 import Motors

last = None
motors = Motors()
move_delay = 1
turn_delay = 0.5

def evaluate(line):
    if(line == "f")
        motors.forwards()
        time.sleep(move_delay)
    if(line == "l")
        motors.left()
        time.sleep(turn_delay)
    # Also fill in code for turning right and backwards

while(last != 'q'):
    sys.stdout.write("Command: ")
    sys.stdout.flush()
    last = raw_input()
    evaluate(last)

