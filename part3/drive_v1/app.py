import time
from motors import Motors
from wiimotereader import WiimoteReader

class Robot:
    def __init__(self, reader):
        self.reader = reader
        self.live = True
        self.move_delay = 0.7
        self.turn_delay = 0.25
        self.motors = Motors()

    def control_loop(self):
        while(self.live == True):
            cmd = reader.read()
            self.live = cmd.Execute(self.motors, self.move_delay, self.turn_delay)
            time.sleep(0.025)

reader = WiimoteReader()
robot = Robot(reader)

robot.control_loop()
