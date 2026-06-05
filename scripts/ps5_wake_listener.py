#!/usr/bin/env python3
"""Simple HTTP server that runs ps5_auto_login.sh when called via POST /wake-ps5"""
import http.server
import json
import subprocess
import signal
import sys

class WakePS5Handler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/wake-ps5':
            try:
                # Run the ps5_auto_login.sh script
                result = subprocess.run(
                    ['/Users/tonmoyrahman/ps5_auto_login.sh'],
                    capture_output=True, text=True, timeout=60
                )
                if result.returncode == 0:
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({
                        'status': 'ok',
                        'message': 'PS5 wake signal sent via Chiaki'
                    }).encode())
                else:
                    self.send_response(500)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({
                        'status': 'error',
                        'message': f'Script failed: {result.stderr[:200]}'
                    }).encode())
            except subprocess.TimeoutExpired:
                self.send_response(504)
                self.end_headers()
                self.wfile.write(json.dumps({'status': 'error', 'message': 'Script timed out'}).encode())
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(json.dumps({'status': 'error', 'message': str(e)}).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'status': 'running'}).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        # Quiet logging
        pass

if __name__ == '__main__':
    port = 8899
    server = http.server.HTTPServer(('0.0.0.0', port), WakePS5Handler)
    print(f'PS5 wake listener running on http://0.0.0.0:{port}')
    signal.signal(signal.SIGTERM, lambda *args: sys.exit(0))
    server.serve_forever()
