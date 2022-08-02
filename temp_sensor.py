import time

from ds18b20 import DS18B20


ds18b20 = DS18B20()

while True:
    temp_f = ds18b20.read_temp_f()
    print("{}".format(temp_f))
    time.sleep(60)
