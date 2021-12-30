import network
import re
import config

def start():
     global routes
     ap_if = network.WLAN(network.AP_IF)
     ap_if.active(True)
     
     config = config.get()
     if config['ssid'] == '':
          config['ssid'] = 'THERMO'
          config.set(config)
     ap_if.config(essid=config['ssid'])
     ap_if.ifconfig(('192.168.4.1', '255.255.255.0', '192.168.4.1', '8.8.8.8'))
     print(ap_if.ifconfig())
     import socket
     addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

     s = socket.socket()
     s.bind(addr)
     s.listen(1)
     print('listening on', addr)

     while True: # !config.Wifi.ssid:
          cl, addr = s.accept()
          print('client connected from', addr)
          cl_file = cl.makefile('rwb', 0)
          first_line = cl_file.readline().strip().decode('utf-8')
          print('first_line : ' + first_line)
          first_line = first_line.split()
          method = first_line[0]
          path = first_line[1]
          protocol_version= first_line[2]
          header = []
          while True:
               line = cl_file.readline().strip().decode('utf-8')
               print('header : *' + line + '*')
               if not line or line == '\r\n' or line == '':
                    print('tada')
                    break
               header.append(line)
          
          if (line):
              body = cl_file.read()
              print('body: ' + body.strip().decode('utf-8'))

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
          
          cl.send(res)
          cl.close()

def add_route(method, path, func):
     global routes
     routes.append(tuple((method, path, func)))

def remove_route(method, path):
     global routes
     routes = [ r for r in routes if r[0] != method or r[1] != path ]

