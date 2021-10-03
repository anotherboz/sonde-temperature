import _thread
import config
import network


def wait_for_temperature():
     print('waiting for temperature...')

def send_temperature():
     print('send temperature')


def start_server():
     ap_if = network.WLAN(network.AP_IF)
     ap_if.active(True)
     print('config server : ' + ap_if.config())
     import socket
     addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

     s = socket.socket()
     s.bind(addr)
     s.listen(1)
     print('listening on', addr)

     while config.Wifi.ssid:
          cl, addr = s.accept()
          print('client connected from', addr)
          cl_file = cl.makefile('rwb', 0)
          while True:
               line = cl_file.readline()
               print('read : ' + line)
               if not line or line == b'\r\n':
                    break
          response = '{}'
          cl.send('HTTP/1.0 200 OK\r\nContent-type: application/json\r\n\r\n')
          cl.send(response)
          cl.close()


if (config.Wifi.ssid):
    wait_for_temperature()
    send_temperature()
else:
     start_server()


