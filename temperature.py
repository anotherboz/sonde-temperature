import time
import machine
import onewire, ds18x20
import binascii

# the device is on GPIO12
dat = machine.Pin(22)

# create the onewire object
ds = ds18x20.DS18X20(onewire.OneWire(dat))

# scan for devices on the bus
roms = ds.scan()
print('found devices:', list(map(lambda a: binascii.hexlify(a[6:]), roms)))

# loop 10 times and print all temperatures
for i in range(10):
    print('temperatures:', end=' ')
    ds.convert_temp() # takes around 250 ms
    time.sleep_ms(750)
    for rom in roms:
        print(binascii.hexlify(rom[6:]), ds.read_temp(rom), end=' ')
    print()