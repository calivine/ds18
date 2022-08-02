import time

from ds18b20 import DS18B20


ds18b20 = DS18B20()

while True:
    print(ds18b20.read_temp_f())
    time.sleep(60)
