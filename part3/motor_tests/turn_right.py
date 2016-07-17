import explorerhat
import time

explorerhat.motor.one.forwards()
explorerhat.motor.two.backwards()
time.sleep(1)
explorerhat.motor.one.stop()
explorerhat.motor.two.stop()

