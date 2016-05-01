#!/usr/bin/python

import logging
logging.basicConfig(level=logging.DEBUG)

import Turbo_I2C.BMP180 as BMP180

#sensor = BMP180(mode=BMP180_OSAMPLE_16)
sensor = BMP180.BMP180()


degrees = sensor.read_temperature()
pascals = sensor.read_pressure()
hectopascals = pascals / 100

print 'Temp      = {0:0.3f} deg C'.format(degrees)
print 'Pressure  = {0:0.2f} hPa'.format(hectopascals)
print 'Altitude = {0:0.2f} m'.format(sensor.read_altitude())
print 'Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure())
