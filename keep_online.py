from flask import Flask
from threading import Thread, ThreadError

app = Flask('app')

def run():
  app.run(host='0.0.0.0', port=8080) # KEEP THIS AS DEFAULT FOR BEST PERFORMANCE.
  
def startWs():
  t = Thread(target=run)
  t.start()

return;
