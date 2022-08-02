import time

from ds18b20 import DS18B20
import I2C_LCD_driver


ds18b20 = DS18B20()

display = I2C_LCD_driver.lcd()

while True:
    temp_f = ds18b20.read_temp_f()
    temp_output = "{}F".format(temp_f)
    print(temp_output)
    display.lcd_display_string(temp_output, 1)
    time.sleep(60)
    display.lcd_clear()
