from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import json, sqlite3, urllib.parse, datetime, os
BASE=Path(__file__).resolve().parent
DB=BASE/'data.sqlite3'
FIELDS=['learner', 'skill', 'answer']
PROJECT='SeekhoSaath'
def db():
 c=sqlite3.connect(DB); c.row_factory=sqlite3.Row
 c.execute('CREATE TABLE IF NOT EXISTS records (id INTEGER PRIMARY KEY AUTOINCREMENT, payload TEXT NOT NULL, created_at TEXT NOT NULL)')
 return c
class Handler(SimpleHTTPRequestHandler):
 def __init__(self,*a,**kw): super().__init__(*a,directory=str(BASE),**kw)
 def send_json(self,code,obj):
  data=json.dumps(obj,ensure_ascii=False).encode(); self.send_response(code); self.send_header('Content-Type','application/json; charset=utf-8'); self.send_header('Content-Length',str(len(data))); self.send_header('Cache-Control','no-store'); self.end_headers(); self.wfile.write(data)
 def do_GET(self):
  if self.path.split('?')[0]=='/api/records':
   c=db(); rows=c.execute('SELECT * FROM records ORDER BY id DESC LIMIT 100').fetchall(); c.close()
   self.send_json(200,{'project':PROJECT,'records':[{'id':r['id'],'created_at':r['created_at'],**json.loads(r['payload'])} for r in rows]}); return
  if self.path.split('?')[0]=='/api/health': self.send_json(200,{'ok':True,'project':PROJECT}); return
  super().do_GET()
 def do_POST(self):
  if self.path!='/api/records': self.send_json(404,{'error':'Route not found'}); return
  try: data=json.loads(self.rfile.read(int(self.headers.get('Content-Length','0'))))
  except Exception: self.send_json(400,{'error':'Send a valid JSON object'}); return
  if not isinstance(data,dict) or any(not str(data.get(k,'')).strip() for k in FIELDS): self.send_json(400,{'error':'Complete all required fields'}); return
  clean={k:str(data[k]).strip()[:1200] for k in FIELDS}
  c=db(); cur=c.execute('INSERT INTO records(payload,created_at) VALUES(?,?)',(json.dumps(clean,ensure_ascii=False),datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'))); c.commit(); rid=cur.lastrowid; c.close()
  self.send_json(201,{'id':rid,'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'),**clean})
 def log_message(self,fmt,*args): print('%s - %s'%(self.address_string(),fmt%args))
if __name__=='__main__':
 host=os.environ.get('HOST','127.0.0.1'); port=int(os.environ.get('PORT','8014'))
 print(f'{PROJECT} running at http://{host}:{port}  •  SQLite: {DB.name}')
 ThreadingHTTPServer((host,port),Handler).serve_forever()
