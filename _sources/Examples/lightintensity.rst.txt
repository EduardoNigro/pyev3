Light Intensity
===============

During the loop execution of this example :ref:`code <codelight>`, ambient
light intensity is displayed on the screen and recorded, at two distinct
sampling periods. A cell phone flahslight was swept in front of the sensor,
producing the results below.

.. image:: ../../images/Color-Example.png

.. _codelight:

.. code-block:: python

    """ lightintensity.py 

    Use the color sensor to record ambient light intensity.

    Setup:
        Connect color sensor to port number 1.

    """
    # Importing modules and classes
    import time
    import numpy as np
    from pyev3.utils import plot_line
    from pyev3.brick import LegoEV3
    from pyev3.devices import Color

    # Defining parameters
    tstop = 5 # Execution loop duration (s)
    tsample = 0.02 # Data sampling period (s)
    tdisp = 0.2 # Screen display period (s)

    # Pre-allocating output arrays
    t = []
    ambint = []

    # Creating LEGO EV3 objects
    ev3 = LegoEV3()
    color = Color(ev3, portnum=1, inputmode='ambient')

    # Initializing current time stamp and starting clock
    tprev = 0
    tcurr = 0
    tstart = time.perf_counter()
    # Changing EV3 status light
    ev3.set_statuslight(mode='pulsing')
    # Running execution loop
    ambprev = color.output
    print('Running for', tstop, 'seconds ...')
    while tcurr <= tstop:
        # Getting current ambient light intensity
        ambcurr = color.output
        # Updating previous time and getting current time (s)
        tprev = tcurr
        tcurr = time.perf_counter() - tstart
        # Displaying light intensity every `tdisp` seconds
        if (np.floor(tcurr/tdisp) - np.floor(tprev/tdisp)) == 1:
            print('Intensity = ', ambcurr)
            ambprev = ambcurr
        # Acquiring data every `tsample` seconds
        # and appending values to output arrays
        if (np.floor(tcurr/tsample) - np.floor(tprev/tsample)) == 1:
            t.append(tcurr)
            ambint.append(ambcurr)
    print('Done.')
    # Closing brick connection
    ev3.set_statuslight(mode='solid')
    ev3.close()

    # Plotting results
    plot_line([t], [ambint], yname=['Ambient Light Int. (%)'], marker=True)
