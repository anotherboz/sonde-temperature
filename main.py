import blink
import config

// At startup led blink 3 times slowly
blink_3_times()
conf = config.get_config
print('sid: ' + conf['ssid'] +'\n')
print('password: ' + conf['password'] +'\n')
print('server: ' + conf['password'] +'\n')


conf['ssid'] = '1234'

config.set_config(conf)
