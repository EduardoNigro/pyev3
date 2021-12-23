""" obstacle.py 

Use the ultrasonic sensor to detect a distance threshold.

This example shows how to use the ultrasonic sensor to detect an obstacle
and sound an alarm as well as change the EV3 brick light color.

Setup:
    Connect ultrasonic sensor to port number 1.

"""
# Importing modules and classes
import time
import numpy as np
from pyev3.brick import LegoEV3
from pyev3.devices import Ultrasonic

# Defining parameters
tstop = 10  # Execution loop duration (s)
talarm = 0.5 # Alarm beeping interval (s)
distmin = 10 # Minimum distance for alarm (cm)

# Creating LEGO EV3 objects
ev3 = LegoEV3()
usonic = Ultrasonic(ev3, portnum=1, inputmode='distance')

# Initializing current time stamp and starting clock
tprev = 0
tcurr = 0
tstart = time.perf_counter()
# Running execution loop
print('Running for', tstop, 'seconds ...')
while tcurr <= tstop:
    # Getting current distance to obstacle
    distcurr = usonic.output
    # Checking for distance threshold
    if distcurr < distmin:
        ev3.set_statuslight(color='red')
    else:
        ev3.set_statuslight(color='green')
    # Updating previous time and getting current time (s)
    tprev = tcurr
    tcurr = time.perf_counter() - tstart
    # Sounding alarm every `talarm` seconds if minimum distance is violated
    if (np.floor(tcurr/talarm) - np.floor(tprev/talarm)) == 1:
        print('Distance = ', distcurr)
        if distcurr < distmin:
            ev3.play_tone(volume=20, frequency=880, duration = 0.1)
print('Done.')
# Closing brick connection
ev3.set_statuslight(color='green')
ev3.close()
