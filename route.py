import http_format as http

def index(body, headers):
     return http.ok('Sonde temperature')

def option(body, headers):
     return http.ok('')


