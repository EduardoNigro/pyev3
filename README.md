# Project Description
**pyev3** can be used to interact with the **LEGO Mindstorms EV3**.

Send direct commands to the EVR from your PC (local host) using a USB or WiFi connection. **pyev3** is an alternative to [pybricks](https://pybricks.com/ev3-micropython/), which requires booting your EV3 brick from an SD card, and where micropython programs run in the EV3 memory. With **pyev3** you can run the EV3 as is. Just connect it to a USB port, or create a WiFi connection, and you're good to go!

## Classes
Interact with each one of the EV3 devices through simple methods and properties, implemented in the following classes:
* LegoEV3
* Motor
* Touch
* Color
* Ultrasonic
* Infrared
* Gyro

## Example Code
Start and stop a motor using the touch sensor. The motor speed is proportional to ambient light intensity.

```python
from pyev3.brick import LegoEV3
ev3 = LegoEV3()
```
