import time
from wiimotereader import WiimoteReader

class Robot:
    def __init__(self, reader):
        self.reader = reader
        self.live = True
    def control_loop(self):
        while(self.live == True):
            cmd = reader.read()
            self.live = cmd.Execute()
            time.sleep(0.025)

reader = WiimoteReader()
robot = Robot(reader)

robot.control_loop()
