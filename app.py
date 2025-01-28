from http.server import BaseHTTPRequestHandler, HTTPServer
import os

# Define HTTP server ports
port = int(os.getenv('PORT', 3000))
port2 = int(os.getenv('PORT2', 3001))

# Define the handler for HTTP requests
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.server.server_port == port:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Hello from Python App!\n")
        elif self.server.server_port == port2:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Hello again from Python!\n")

# Start server on PORT
def start_server(port):
    serv
