import time

from ds18b20 import DS18B20
import I2C_LCD_driver
from moisture_sensor import MoistureSensor


class Monitor:

    def __init__(self, moisture=True):
        self.sensor = DS18B20()
        self.display = I2C_LCD_driver.lcd()
        self.moisture_sensor = MoistureSensor() if moisture else None
        # Make list called sensors which holds each
        # sensor object.

    def activate(self):
        try:
            while True:
                temp_f = self.sensor.read_temp_f()
                temp_output = "{}{}F".format(temp_f, chr(223))
                print(temp_output)
                # Check if moisture sensor is connected
                self.display.lcd_display_string(temp_output, 1)
                # If moisture sensor is connected
                if self.moisture_sensor is not None:
                    moisture = self.moisture_sensor.read_channel(0)
                    print(moisture)
                    moisture_output = "Moisture level: {}".format(moisture)
                    self.display.lcd_display_string(moisture_output, 2)
                time.sleep(60)
                self.display.lcd_clear()
        except KeyboardInterrupt:
            pass
        finally:
            self.display.lcd_clear()


