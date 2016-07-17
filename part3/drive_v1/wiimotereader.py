import cwiid, time
from commands import *

class WiimoteReader:
    def __init__(self):
        self.wii = cwiid.Wiimote()
        self.wii.rpt_mode = cwiid.RPT_BTN

    def read(self):
        buttons = self.wii.state['buttons']
        command = None
        if buttons & cwiid.BTN_A:
            command = Forwards()
        elif buttons & cwiid.BTN_B:
            command = Backwards()
        else:
            command = Stop()

        return command
