from email.policy import HTTP
from http.server import BaseHTTPRequestHandler, HTTPServer
from lib2to3.pytree import Base
import time

HostName = 'localhost'
serverPort = 5002


class httpServ(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>write something</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == '__main__':
    webserver = HTTPServer((HostName, serverPort), httpServ)
    print("Server started http://%s:%s" % (HostName, serverPort))

    try:
        webserver.serve_forever()
    except KeyboardInterrupt:
        pass

webserver.close()
print("Server stopped")