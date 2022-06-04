import uasyncio
import re
import config

async def callback(input, output):
     first_line = await input.readline()
     first_line= first_line.decode("utf-8")
     print('first_line : ' + first_line)
     first_line = first_line.split()
     method = first_line[0]
     path = first_line[1]
     protocol_version= first_line[2]
     header = []
     while True:
          line = await input.readline()
          line = line.decode("utf-8") 
          print('header : *' + line + '*')
          content_length = re.search('Content-Length: (\d+)')
          if (content_length):
               content_length = content_length.group(0)
          if not line or line == '\r\n' or line == '':
               print('tada')
               break
          header.append(line)
          
     print('content_length ' + content_length)

     if (line):
          body = ''

          print('content_length ' + content_length)
          if (content_length):
               body = await input.read(content_length)
               body = body.decode('utf-8')
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
               res = func(body, headers)
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


async def main():
     uasyncio.create_task(start())
     await uasyncio.sleep_ms(1_000)

async def wait_60_s():
    print('wait for 60s')
    await uasyncio.sleep(60)
    print('60 s over')

print('start')
loop = uasyncio.get_event_loop()
loop.create_task(uasyncio.start_server(callback, "0.0.0.0", 8080))
try: 
#    loop.run_forever()
    loop.run_until_complete(wait_60_s())
except KeyboardInterrupt:
    print("closing")
    loop.close()

print('that s all folks...')