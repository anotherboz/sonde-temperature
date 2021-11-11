import blink
import config
import server

// At startup led blink 3 times slowly
blink_3_times()
conf = config.load()

print('ssid: ' + conf['ssid'] +'\n')
print('server: ' + conf['server'] +'\n')
print('password: ' + conf['password'] +'\n')


if conf['server'] == '':
    server.add_route('OPTION', '.*', option)
    server.add_route('GET', '/', index)
    server.start()
