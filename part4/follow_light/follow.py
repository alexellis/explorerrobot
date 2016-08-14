import explorerhat
import time
from ultrasonic import *
dm = distanceMeasure(6, 23)
dm.setup()

def evade(cm):
    while(cm < 20):        
        explorerhat.motor.two.backwards(0.5*100)
        explorerhat.motor.one.backwards(0.5*100)
        time.sleep(0.6)
        explorerhat.motor.two.forwards(0.5*100)
        explorerhat.motor.one.backwards(0.5*100)
        time.sleep(0.6)
        explorerhat.motor.two.stop()
        explorerhat.motor.one.stop()
        time.sleep(0.3)
        cm = dm.measureDistance(0.01)

while(True):
    left = explorerhat.analog.one.read()
    right = explorerhat.analog.two.read()
    print( str(left) + " " + str(right) )

    diff = abs(left-right)
    bias = "left"
    tolerance = 0.025
    if(right>left):
       bias = "right"
    if(diff < tolerance):
       bias = None

    percentage_left = 1.0    
    percentage_right = 1.0    
    if(bias=="left"):
        percentage_left = 0.4
    if(bias=="right"):
        percentage_right = 0.4
    if(bias == "left"):
        print("<")
    elif(bias == "right"):
        print(">")
    else:
        print("^")
    modifier = 0.5
    # one - right
    # two - left
    explorerhat.motor.two.forwards((percentage_left * modifier) * 100)
    explorerhat.motor.one.forwards((percentage_right * modifier) * 100)
    cm = dm.measureDistance(0.01)
    if(cm < 20):
        evade(cm)
    print(str(cm))
    time.sleep(0.1)

