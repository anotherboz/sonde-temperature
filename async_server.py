import uasyncio
import re
import config

running = False

async def start():
     global routes
     global running
     # ap_if = network.WLAN(network.AP_IF)
     # ap_if.active(True)
     
     # config = config.get()
     # if config['ssid'] == '':
     #      config['ssid'] = 'THERMO'
     #      config.set(config)
     # ap_if.config(essid=config['ssid'])
     # ap_if.ifconfig(('192.168.4.1', '255.255.255.0', '192.168.4.1', '8.8.8.8'))
     # print(ap_if.ifconfig())

     addr='127.0.0.1'

     while True: # !config.Wifi.ssid:
          server = uasyncio.start_server(callback, addr, 8080)
          # await server.wait_closed()

async def callback(input, output):
     first_line = input.readline()
     print('first_line : ' + first_line)
     first_line = first_line.split()
     method = first_line[0]
     path = first_line[1]
     protocol_version= first_line[2]
     header = []
     while True:
          line = await input.readline()
          print('header : *' + line + '*')
          if not line or line == '\r\n' or line == '':
               print('tada')
               break
          header.append(line)
          
     if (line):
          body = await input.read()
          print('body: ' + body)

          func = None
          print('methode : ' + method + '  path : ' + path)
          for r in routes:
               print ('r0 : ' + r[0] +  '   r1 : ' + r[1])
               if (r[0] == method and re.match(r[1], path)):
                    func = r[2]
                    print('got it')
                    break

          if (func):
               res = func('', '')
          else:
               res = error404('')
          print('tada4')
          
          output.write(res)
          input.close()
          output.close()

def add_route(method, path, func):
     global routes
     routes.append(tuple((method, path, func)))

def remove_route(method, path):
     global routes
     routes = [ r for r in routes if r[0] != method or r[1] != path ]

print('coucou')
uasyncio.run(start())