import spidev
import os
import time


class MoistureSensor:

    def __init__(self, delay=0.2):
        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)
        self.spi.max_speed_hz = 1000000
        self.delay = delay

    def read_channel(self, channel):
        val = self.spi.xfer2([1, (8 + channel) << 4, 0])
        data = ((val[1] & 3) << 8) + val[2]
        return data

    def delay(self):
        time.sleep(self.delay)


