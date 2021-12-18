LegoEV3
=======

The LEGO® MINDSTORMS® EV3 brick is at the core of the **pyev3** package.
Once the brick is powered up, you can use a PC to communicte with it in two ways:

* **USB** (*fastest*) 

    * requires a USB cable (that comes with the set)
    * very repeatable *command/reply* round-trip times of approx. 5 ms

* **WiFi** (*free to move around!*)

    * requires a `WiFi dongle <https://www.edimax.com/edimax/merchandise/merchandise_detail/data/edimax/global/home_legacy_wireless_adapters/ew-7811un/>`__ (purchased separately)
    * not very repeatable *command/reply* round-trip times between 10 to 20 ms


.. image:: ../images/LegoEV3.png


.. autoclass:: brick.LegoEV3
    :members:
    :private-members:
