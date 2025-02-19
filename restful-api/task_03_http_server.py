#!/usr/bin/python3
"""task_03_http_server.py"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class Simple_API(BaseHTTPRequestHandler):
    """A Subclass from BaseHTTP....."""

    def _set_response(self, data, status_code=200):
        """
        Method that is called by do_GET to set the headers,
        and send it to the user
        """

        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))

    def do_GET(self):
        """Method that is used to adapt the DATA to show"""

        if self.path == '/' or self.path == "/status":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            if self.path == '/':
                self.wfile.write("Hello, this is a simple API!"
                                 .encode('utf-8'))
            else:
                self.wfile.write("OK".encode('utf-8'))

        elif self.path == '/data':
            self._set_response(
                {"name": "John", "age": 30, "city": "New York"})

        elif self.path == '/info':
            self._set_response({"version": "1.0", "description":
                                "A simple API built with http.server"})

        else:
            self._set_response({"error": "Not found"}, 404)


def run():
    """The function that run the localhost API"""

    server_address = ('', 8000)
    httpd = HTTPServer(server_address, Simple_API)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stop Listening")


if __name__ == '__main__':
    run()
