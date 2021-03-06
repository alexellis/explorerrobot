import time
import os

class Shutdown:
    def Execute(self, motors, move_delay, turn_delay):
        os.system("sudo halt")
        return False

class Stop:
    def Execute(self, motors, move_delay, turn_delay):
        motors.stop()
        return True

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
        motors.right()
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
