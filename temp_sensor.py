import time

from ds18b20 import DS18B20
import I2C_LCD_driver


class Monitor:

    def __init__(self):
        self.sensor = DS18B20()
        self.display = I2C_LCD_driver.lcd()

    def activate(self):
        try:
            while True:
                temp_f = self.sensor.read_temp_f()
                temp_output = "{}F".format(temp_f)
                print(temp_output)
                self.display.lcd_display_string(temp_output, 1)
                time.sleep(60)
                self.display.lcd_clear()
        except KeyboardInterrupt:
            pass
        finally:
            self.display.lcd_clear()


