# src/monitor.py

from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
from src.detect import detector
from src.mitigate import should_rate_limit

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        ip = self.client_address[0]
        if should_rate_limit(ip):
            self.send_response(429)
            self.end_headers()
            self.wfile.write(b"Rate limit exceeded. Try again later.")
            return

        detector.log_request(ip)
        logging.info(f"Received request from {ip}")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
