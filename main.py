import blink
import config

// At startup led blink 3 times slowly
blink_3_times()
conf = config.getConfig
print('sid: ' + conf['sid'] +'\n')
print('password: ' + conf['password'] +'\n')
print('server: ' + conf['password'] +'\n')


conf['sid'] = '1234'

config.setConfig(conf)
