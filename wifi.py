import network
import json
import re

routes = []  // tuple of (method, path, func)

def ok(body):
     return '''
HTTP/1.0 200 OK
Content-Type: text/html
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: *
Content-Length: ''' + str(len(body)) + '''

''' + body  

def json(body):
     return '''
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: ''' + str(len(body)) + '''

''' + json.dumps(body)  

def error404(body):
     print('tada3')
     return '''
HTTP/1.0 404 Not Found
Content-Length: ''' + str(len(body)) + '''

''' + body  

def error500(body):
     return '''
HTTP/1.0 500 Internal Server Error
Content-Length: ''' + str(len(body)) + '''

''' + body  

def start_server():
     global routes
     ap_if = network.WLAN(network.AP_IF)
     ap_if.active(True)
     
     ap_if.config(essid='THERMO')
     ap_if.ifconfig(('192.168.4.1', '255.255.255.0', '192.168.4.1', '8.8.8.8'))
     print(ap_if.ifconfig())
     import socket
     addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

     s = socket.socket()
     s.bind(addr)
     s.listen(1)
     print('listening on', addr)

     while True: # config.Wifi.ssid:
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

def index(body, headers):
     return ok('Sonde temperature')

def option(body, headers):
     return ok('')

add_route('GET', '/', index)
add_route('OPTION', '.*', option)
start_server()

