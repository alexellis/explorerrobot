import sys, time
from motors_v1 import Motors

import time
import os

class Backwards:
    def Execute(self, motors, move_delay, turn_delay):
        motors.backwards()
        time.sleep(move_delay)
        motors.stop()
        return True

class Forwards:
    def Execute(self, motors, move_delay, turn_delay):
        motors.forwards()
        time.sleep(move_delay)
        motors.stop()
        return True

class Right:
    def Execute(self, motors, move_delay, turn_delay):
        motors.left()
        time.sleep(turn_delay)
        motors.stop()
        return True

class Left:
    def Execute(self, motors, move_delay, turn_delay):
        motors.left()
        time.sleep(turn_delay)
        motors.stop()
        return True

class Quit:
    def Execute(self, motors, move_delay, turn_delay):
        return False

class TerminalReader:
    def read(self):
        sys.stdout.write("> ")
        sys.stdout.flush()
        return self.parse(raw_input())

    def parse(self, line):
        if(line=="w"):
            return Forwards()
        elif(line=="s"):
            return Backwards()
        elif(line=="d"):
            return Right()
        elif(line=="a"):
            return Left()
        elif(line=="q"):
            return Quit()

class Robot:
    def __init__(self):
        self.move_delay = 0.6
        self.turn_delay = 0.2
        self.terminalReader = TerminalReader()
        self.motors = Motors()

    def repl(self):
        result = True
        while(result != False):
            cmd = self.terminalReader.read()
            if(cmd != None):
                result = cmd.Execute(self.motors, self.move_delay, self.turn_delay)

robot1 = Robot()
robot1.repl()
