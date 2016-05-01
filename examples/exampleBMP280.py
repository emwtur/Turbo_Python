#!/usr/bin/python

#import logging
#logging.basicConfig(level=logging.DEBUG)

import Turbo_I2C.BMP280 as BMP280

#sensor = BMP280(mode=BMP280_OSAMPLE_16)
sensor = BMP280.BMP280()


degrees = sensor.read_temperature()
pascals = sensor.read_pressure()
hectopascals = pascals / 100

print 'ChipID    = 0x{0:2x} '.format(sensor.ChipID )
print 'Version   = 0x{0:2x}'.format(sensor.Version )
print 'Timestamp = {0:0.3f}'.format(sensor.t_fine)
print 'Temp      = {0:0.3f} deg C'.format(degrees)
print 'Pressure  = {0:0.2f} hPa'.format(hectopascals)
if sensor.HasHumidity :
    humidity = sensor.read_humidity()
    print 'Humidity  = {0:0.2f} %'.format(humidity)
else:
    print 'Sensor does not have Humidity'
