mport time
from motors_v1 import Motors

motors = Motors()

motors.forwards()
time.sleep(1)
motors.stop()
time.sleep(1)
motors.backwards()
time.sleep(1)
motors.stop()
