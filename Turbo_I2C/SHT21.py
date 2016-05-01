# Copyright (c) 2014 Adafruit Industries
import logging
import time


# SHT21 default address.
SHT21_I2CADDR = 0x40


# Operating Modes

# SHT21 Registers

SHT21_TempHoldCmd	 = 0xE3
SHT21_RHumidityHoldCmd	 = 0xE5
SHT21_TempNoHoldCmd      = 0xF3
SHT21_RHumidityNoHoldCmd = 0xF5
SHT21_SOFTRESET          = 0xFE

SHT21_TEMPERATURE_WAIT_TIME = 0.086  # (datasheet: typ=66, max=85)
SHT21_HUMIDITY_WAIT_TIME = 0.030     # (datasheet: typ=22, max=29)

class SHT21(object):
    def __init__(self, address=SHT21_I2CADDR, i2c=None,
                 **kwargs):
        self._logger = logging.getLogger('TURBO_I2C.SHT21')
        if i2c is None:
            import Adafruit_GPIO.I2C as I2C
            i2c = I2C
        self._device = i2c.get_i2c_device(address, **kwargs)
        self._device.writeRaw8(SHT21_SOFTRESET)

    def read_temperature(self):
        self._device.writeRaw8(SHT21_TempNoHoldCmd)
        time.sleep(SHT21_TEMPERATURE_WAIT_TIME)
        data1 = self._device.readRaw8()
        data2 = self._device.readRaw8()
        data3 = self._device.readRaw8()
        return 1.2