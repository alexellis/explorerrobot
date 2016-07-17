import time
reader = WiimoteReader()
while(True):
    cmd = reader.read()
    print(cmd)
    time.sleep(0.25)
