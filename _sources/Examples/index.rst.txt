
Examples
========

The examples in this section intend to show additional aspects of coding for
the **EV3** motors and sensors. To that end, they introduce the concept of
execution loops and sampling period. The sensor data is often *recorded* to be
plotted at the end.

Always try to *see* what the sensors are *seeing*. Looking at your data as a
function of time is a good starting point. It will help understand why things
work (or sometimes don't) as expected.

=======================================  ===================================================
Example                                  Brief Description
=======================================  ===================================================
:doc:`One Motor <onemotor>`              Run a sinusoidal motor speed output
:doc:`Two Motors <twomotors>`            Run a sinusoidal speed output for two motors
:doc:`Event Counter <counter>`           Use the touch sensor as an event counter
:doc:`Light Intensity <lightintensity>`  Detect the relative light intensity of a flashlight
:doc:`Obstacle Detection <obstacle>`     Detect an obstacle using the ultrasonic sensor
:doc:`Infrared Tracking <tracking>`      Track the LEGO® infrared beacon 
:doc:`Gyro Data <gyrodata>`              Measure angular position and velocity using a gyro
=======================================  ===================================================


.. note::
   For best graphic display of the results, consider running them in an interactive
   Jupyter notebook session (instead of a plain old terminal window).


.. toctree::
   :hidden:

   onemotor
   twomotors
   counter
   lightintensity
   obstacle
   tracking
   gyrodata
