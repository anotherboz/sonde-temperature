import blink
import config
import server

# At startup led blink 3 times slowly
blink_3_times()
conf = config.load()

if conf['server'] == '':
    server.add_route('OPTION', '.*', option)
    server.add_route('GET', '/', index)
    server.start()
