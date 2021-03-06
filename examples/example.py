""" Example Code """
# Importing modules
import time
from pyev3.brick import LegoEV3
from pyev3.devices import Motor, Touch, Color
# Creating LEGO EV3 objects
ev3 = LegoEV3(commtype='usb')
motor = Motor(ev3, port='A')
touch = Touch(ev3, portnum=1, inputmode='bump')
color = Color(ev3, portnum=2, inputmode='ambient')
# Initializing system
motor.outputmode = 'speed'
motor.output = 0
motor.start()
touch.reset_count()

# Changing EV3 status light
ev3.set_statuslight(mode='pulsing')
# Running for 30 seconds
print('Running ...')
tcurr = 0
tstart = time.perf_counter()
while tcurr <= 30:
    # Getting current time (s)
    tcurr = time.perf_counter() - tstart
    # Checking for even/odd number of 'bumps'
    if (touch.output % 2) == 0:
        # Assigning ZERO speed output
        motor.output = 0
    else:
        # Assigning output proportional to ambient light
        motor.output = color.output

# Stopping motor and closing EV3 connection
motor.stop()
ev3.set_statuslight(mode='solid')
ev3.close()
print('Done.')