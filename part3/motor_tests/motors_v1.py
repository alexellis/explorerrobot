import time
import explorerhat

class Motors:
  def forwards(self):
      explorerhat.motor.one.forwards()
      explorerhat.motor.two.forwards()
  def stop(self):
      explorerhat.motor.one.stop()
      explorerhat.motor.two.stop()
  def backwards(self):
      explorerhat.motor.one.backwards()
      explorerhat.motor.two.backwards()
  def left(self):
      explorerhat.motor.one.backwards()
      explorerhat.motor.two.forwards()
  def left(self):
      explorerhat.motor.one.forwards()
      explorerhat.motor.two.backwards()


