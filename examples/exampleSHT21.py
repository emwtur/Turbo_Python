#!/usr/bin/python
import Turbo_I2C.SHT21 as SHT21
import logging
logging.basicConfig(level=logging.DEBUG)


sensor = SHT21.SHT21()


degrees = sensor.read_temperature()
humidity = sensor.read_humidity()

print 'Temp      = {0:0.3f} deg C'.format(degrees)
print 'Humidity  = {0:0.2f} %'.format(humidity)
