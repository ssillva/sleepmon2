#!/usr/bin/env python
#####################################################################

import mraa
import time

DEV_ADDR   = 0x23   # Default device I2C address
POWER_DOWN = 0x00   # Power-off state
POWER_ON   = 0x01   # Power-on state
RESET      = 0x07   # Device reset

# Start measurement at 4lx resolution. Time typically 16ms.
CONTINUOUS_LOW_RES_MODE = 0x13

# Start measurement at 1lx resolution. Time typically 120ms
CONTINUOUS_HIGH_RES_MODE_1 = 0x10

# Start measurement at 0.5lx resolution. Time typically 120ms
CONTINUOUS_HIGH_RES_MODE_2 = 0x11

# Start measurement at 1lx resolution. Time typically 120ms
# Device is automatically set to Power Down after measurement.
ONE_TIME_HIGH_RES_MODE_1 = 0x20

# Start measurement at 0.5lx resolution. Time typically 120ms
# Device is automatically set to Power Down after measurement.
ONE_TIME_HIGH_RES_MODE_2 = 0x21

# Start measurement at 1lx resolution. Time typically 120ms
# Device is automatically set to Power Down after measurement.
ONE_TIME_LOW_RES_MODE = 0x23

class bh1750(object):
    def __init__(self, i2c_bus=None, mode=ONE_TIME_HIGH_RES_MODE_1, **kwargs):
        self.bus = i2c_bus
        self.mode = mode
        self.readLight()

    def readLight(self):
        data = self.bus.readBytesReg( self.mode, 2 )
        return ((data[1] + (256 * data[0])) / 1.2)

if __name__=="__main__":
    bus = mraa.I2c( 0 )      # use '/dev/i2c-0'
    bus.address( DEV_ADDR )  # I2C slave address = 0x23
    sensor = bh1750( i2c_bus=bus, mode=CONTINUOUS_HIGH_RES_MODE_1 )
    try:
        print 'BH1750 light sensor'
        while True:
            print "Light Level: %.1f lx" % sensor.readLight()
            time.sleep(1.0)
    except KeyboardInterrupt:
        print 'Terminated..'

#####################################################################
