
pyev3
=====

.. toctree::
   :hidden:

   LegoEV3
   Motor
   Touch
   Color
   Ultrasonic
   Infrared
   Gyro


Send direct commands to the **EV3** from your PC using a USB or WiFi connection.
**pyev3** is an alternative to `pybricks <https://docs.pybricks.com/en/stable/index.html#>`__,
which requires booting the EV3 brick from an SD card, and where micropython programs run
in the brick's memory. With **pyev3** you can use Python to run the EV3 as is. Just connect
it to a USB port, or create a WiFi connection, and you're good to go!


Step 1: Install pyev3
---------------------

If you already have *Python* and an *IDE* (*Integrated Development Environment*)
to go along with it, just install the **pyev3** package:

>>> py -m pip install pyev3

Otherwise, start by installing `Python <https://www.python.org/downloads/>`__ and then an IDE.
Want to code like a pro? I strongly encourage `VSCode <https://code.visualstudio.com/download>`__.


Step 2: Code away!
------------------

Once the ``pip`` installation has finished, reference the different classes in the menu
on the left to see how to interact with motors, sensors and the EV3 brick itself.

Below is an example code where you can also start and stop the motor using the touch
sensor. The motor speed is proportional to the ambient light intensity!

.. code-block:: python

   # Importing modules and classes
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


Issues and questions
--------------------

If you have a feature request, a bug report, or even a question, please open an
`issue on GitHub <https://github.com/EduardoNigro/pyev3/issues/new>`__.