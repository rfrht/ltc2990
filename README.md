# LTC2990

**I2C comms with Linear LTC 2990 Quad I2C Voltage, Current and Temperature Monitor**

This project describes how to access and obtain register data from a LTC2990 IC.
It is preconfigured to run on mode `0b1011111`, it means: V1, V2, V3, V4; All Measurements per Mode, Single Acquisition and Temperature reported in Celsius.

Don't forget to read the [datasheet](http://www.linear.com/product/LTC2990)!

Sample output:

~~~
root@raspberrypi:~# python i2c-ltc2990.py
Int. Temp. : 30 C
Voltage V1 : 3.29624918 V
Voltage V2 : 3.29624918 V
Voltage V3 : 3.29624918 V
Voltage V4 : 3.29624918 V
Vin        : 3.2949939 V
~~~

*[RepRap Ltd](https://github.com/RepRapLtd/Walking-robots/tree/main/Petoi) created a [forked version](https://github.com/RepRapLtd/Walking-robots/blob/main/Petoi/Software/Pi/rrlpetoi.py) that provides continous readings*
