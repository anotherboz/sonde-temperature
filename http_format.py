import json as JSON

routes = []  # tuple of (method, path, func)

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
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: *

''' + JSON.dumps(body)  

def error404(body):
     return '''
HTTP/1.0 404 Not Found
Content-Length: ''' + str(len(body)) + '''

''' + body  

def error500(body):
     return '''
HTTP/1.0 500 Internal Server Error
Content-Length: ''' + str(len(body)) + '''

''' + body  

def error(code, body):
     return '''
HTTP/1.0 ''' + code + '''
Content-Length: ''' + str(len(body)) + '''

''' + body  