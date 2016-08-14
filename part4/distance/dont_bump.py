import explorerhat
from ultrasonic import ultrasonic_sensor

# trigger = output 1
# echo = input 1

# For other output or inputs consult http://pinout.xyz
trigger_pin = 23
echo_pin = 6

ultrasonic1 = ultrasonic_sensor(echo_pin, trigger_pin)
ultrasonic1.setup()
print("Ping..")
while(True):
    sensor_settle_time = 0.1
    cm = ultrasonic1.measure(sensor_settle_time)
    safe_distance_cm = 30
    if(cm <= safe_distance_cm):
        explorerhat.motor.one.stop()
        explorerhat.motor.two.stop()
    else:
        move_power_percent = 50
        explorerhat.motor.one.forwards(move_power_percent)
        explorerhat.motor.two.forwards(move_power_percent)

    print("%.1fcm" % cm)
