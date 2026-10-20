import json, socket, os
from http.server import BaseHTTPRequestHandler, HTTPServer
HASH="89b6df2e-v24"
VERSION="v1_11 HUD-SERVER"
IA22_FILE=os.path.expanduser("~/IA22_AZENV_01/IA22_AZENV_01/core/IA22_STATECHANNEL_01.json")
HUD_FILE=os.path.expanduser("~/IA22_AZENV_01/IA22_AZENV_01/terminal/IA22_TERMINAL_OS_V2.html")

class H(BaseHTTPRequestHandler):
 def _h(self,c=200,t="application/json"):
  self.send_response(c)
  self.send_header("Content-Type",t)
  self.send_header("X-ZCore-Hash",HASH)
  self.send_header("Access-Control-Allow-Origin","*")
  self.send_header("Access-Control-Allow-Headers","X-ZCORE-Token, Content-Type")
  self.send_header("Access-Control-Allow-Methods","GET, OPTIONS")
  self.end_headers()
 def do_OPTIONS(self):
  self._h(200)
  self.wfile.write(b'')
 def log_message(self,*a): return
 def do_GET(self):
  # CORS preflight déjà géré
  if "/api/ia22" in self.path or "/api/status" in self.path:
   if self.headers.get('X-ZCORE-Token')!=HASH:
    self._h(401); self.wfile.write(b'{"error":"ZeroTrust 401 Filter - add header X-ZCORE-Token: 89b6df2e-v24"}'); return
   if "/api/ia22" in self.path:
    try: d=json.load(open(IA22_FILE)); self._h(200); self.wfile.write(json.dumps(d).encode())
    except Exception as e: self._h(500); self.wfile.write(json.dumps({"error":str(e)}).encode())
    return
   else:
    d={"version":VERSION,"hash":HASH,"port":self.server.server_port,"status":"NON DEPENDANCE VALIDEE","logics":23}
    self._h(200); self.wfile.write(json.dumps(d).encode()); return
  # Servir le HUD sur / et /terminal
  if self.path=="/" or "terminal" in self.path or self.path.endswith(".html"):
   try:
    html=open(HUD_FILE,'r').read() if os.path.exists(HUD_FILE) else "<h1>HUD not found</h1>"
    self._h(200,"text/html"); self.wfile.write(html.encode()); return
   except: pass
  # Dashboard par défaut
  h=f'<html><body style="background:#000;color:#0f0;font-family:monospace;padding:20px"><h1>Z-CORE {HASH} {VERSION} LIVE {self.server.server_port}</h1><p><a href="/api/status" style="color:#0f0">/api/status</a> | <a href="/api/ia22" style="color:#0f0">/api/ia22</a> | <a href="/" style="color:#0f0">/ HUD</a></p><p>{VERSION} | 23 logics | Bridge ACTIVE</p></body></html>'
  self._h(200,"text/html"); self.wfile.write(h.encode())

httpd=HTTPServer(("0.0.0.0",8000),H)
print(f'LIVE 8000 {VERSION}')
httpd.serve_forever()
