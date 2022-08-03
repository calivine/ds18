import spidev
import os
import time

delay = 0.2

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000


def readChannel(channel):
    val = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((val[1] & 3) << 8) + val[2]
    return data


try:
    while True:
        val = readChannel(0)
        if val != 0:
            print(val)
        time.sleep(delay)

except KeyboardInterrupt:
    print("Cancel.")

