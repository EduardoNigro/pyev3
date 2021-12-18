"""
Mock brick.py file for documentation purposes
"""


class LegoEV3:
    """
    Agh! The class to represent the LEGO EV3 brick.
    You can use LegoEV3 to interact with the EV3 brick.

    Set up USB connection between host and EV3 brick.

        >>> from pyev3.brick import LegoEV3
        >>> myev3 = LegoEV3(commtype='usb')
        >>> myev3.display_info()
        >>> myev3.close()

    Set up WiFi connection between host and EV3 brick

        >>> myev3 = LegoEV3(commtype='wifi', IPaddress='192.168.0.19, deviceID='001653470e58')
        >>> myev3.display_info()
        >>> myev3.close()

    :param commtype: The type of communication with the brick. ``'usb'`` or ``'wifi'``.
    :type commtype: str
    :param IPaddress: The IP address assigned to the EV3 brick.
    :type IPaddress: str
    :param deviceID:
        The individual device ID of the EV3 brick.
        Connect to the brick using `commtype='usb'` and use the
        `display_info()` method to retrieve the ID of the brick.
    :type deviceID: str

    .. note::
        1. Always use the `close()` method before opening a new connection.
        2. Try a USB connection first. It's easier to set up and much faster.

    """
    def __init__(self, commtype='usb', IPaddress=None, deviceID=None):
        """
        Class constructor.

        """
        pass

    # GET/SET METHODS (PUBLIC PROPERTIES)
    @property
    def devmode(self):
        """
        Contains a developer mode flag. Default is ``False``. 
        When ``True``, communication info is displayed after
        each direct command (`read/write`).
        
        """
        pass

    @devmode.setter
    def devmode(self, value):
        pass

    @property
    def batterylevel(self):
        """
        Contains the EV3 battery level in `%` (`read only`).
        
        """
        pass

    @batterylevel.setter
    def batterylevel(self, _):
        pass

    @property
    def connectedsensors(self):
        """
        Contains a list with the sensors connected to the EV3 (`read only`).
        
        """
        pass

    @connectedsensors.setter
    def connectedsensors(self, _):
        print('"connectedsensors" is a read only attribute.')

    # BRICK PUBLIC METHODS
    def close(self):
        """
        Close the EV3 brick connection.

        >>> myev3.close()

        """
        pass

    def display_info(self):
        """
        Displays a summary with the brick information.
        
        """
        pass

    def set_statuslight(self, mode='solid', color='green'):
        """
        Set the status light of the EV3 brick.

        :param mode: The light mode: ``'solid'``, ``'pulsing'``, ``'off'``
        :type mode: str
        :param color: The light color: ``'green'``, ``'orange'``, ``'red'``
        :type color: str

        >>> myev3.set_statuslight(mode='pulsing', color='orange')

        """
        pass

    def play_tone(self, volume=10, frequency=440, duration=1):
        """
        Play a tone on the EV3 brick.

        :param volume: The volume of the played tone: ``0`` to ``100``
        :type volume: int
        :param frequency: The frequency (Hz) of the played tone: ``0`` to ``10000``
        :type frequency: int
        :param duration: The duration (s) of the played tone: ``0`` to ``5``
        :type duration: float

        >>> myev3.play_tone(volume=5, frequency=880, duration=0.5)

        """
        pass

