import http.server
import route


class HTTPHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.wfile.write(route.index("","").encode("utf-8"))


if __name__ == '__main__':
    PORT = 8888
    server_address = ("", PORT)

    server = http.server.HTTPServer
    handler = HTTPHandler
    print("Serveur actif sur le port :", PORT)

    httpd = server(server_address, handler)
    httpd.serve_forever()