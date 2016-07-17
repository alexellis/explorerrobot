import sys

last = None
while(last != 'q'):
    sys.stdout.write("Command: ")
    sys.stdout.flush()
    last = raw_input()
    print("You said: " + last)
