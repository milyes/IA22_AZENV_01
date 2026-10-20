import json, socket, os
from http.server import BaseHTTPRequestHandler, HTTPServer

HASH = "89b6df2e-v24"
VERSION = "v1_10 IA22-BRIDGE"
STATUS = "NON DEPENDANCE VALIDEE"
IA22_FILE = os.path.expanduser("~/IA22_AZENV_01/IA22_AZENV_01/core/IA22_STATECHANNEL_01.json")

class H(BaseHTTPRequestHandler):
    def _h(self, c=200, t="application/json"):
        self.send_response(c)
        self.send_header("Content-Type", t)
        self.send_header("X-ZCore-Hash", HASH)
        self.end_headers()
    def log_message(self, *a): return
    def do_GET(self):
        if self.headers.get('X-ZCORE-Token') != HASH:
            self.send_response(401)
            self.end_headers()
            self.wfile.write(b'{"error":"ZeroTrust 401 Filter"}')
            return
        if "/api/ia22" in self.path:
            try:
                with open(IA22_FILE) as f:
                    d=json.load(f)
                self._h(200)
                self.wfile.write(json.dumps(d).encode())
            except Exception as e:
                self._h(500)
                self.wfile.write(json.dumps({"error":str(e)}).encode())
            return
        d={"version":VERSION,"hash":HASH,"port":self.server.server_port,"status":STATUS,"logics":23,"ia22_file":IA22_FILE}
        self._h(200)
        self.wfile.write(json.dumps(d).encode())

def free_port():
    for p in [8000,8001,8002]:
        try:
            s=socket.socket(); s.bind(("0.0.0.0",p)); s.close(); return p
        except: continue
    return 8000

port=free_port()
httpd=HTTPServer(("0.0.0.0",port),H)
print(f'LIVE {port} {VERSION}')
httpd.serve_forever()
