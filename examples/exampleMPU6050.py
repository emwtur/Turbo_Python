#!/usr/bin/python

# Can enable debug output by uncommenting:
#import logging
#logging.basicConfig(level=logging.DEBUG)
import math
import Turbo_I2C.MPU6050 as MPU6050

sensor = MPU6050.MPU6050()

sensor.read_raw_data()


print 'Temp  = {0:0.2f} *C'.format(sensor.read_temp())
print 'Pitch = {0:0.2f} grader '.format(sensor.read_pitch()/ math.pi *180)
print 'Roll  = {0:0.2f} grader '.format(sensor.read_roll()/ math.pi *180)
