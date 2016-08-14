from ultrasonic import ultrasonic

# trigger = output 1
# echo = input 1

# For other output or inputs consult http://pinout.xyz
trigger_pin = 6
echo_pin = 23

ultrasonic1 = ultrasonic(echo_pin, trigger_pin)
ultrasonic1.setup()
while(True):
    sensor_settle_time = 0.1
    cm = ultrasonic1.measure(sensor_settle_time)
    print(str(cm) + " cm")
