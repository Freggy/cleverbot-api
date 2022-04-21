
# to access cache and pw those
# two lines HAVE to be in this
# position, because python fuckery
import gevent import monkey
monkey.patch_all()

import time
import cleverbotfree
from flask import Flask, request, session, jsonify
from cachetools import TTLCache

class TTL(TTLCache):
   def popitem(self):
      key, val = TTLCache.popitem(self)
      val.close()
      return key, val

app = Flask(__name__)
# cache ttl is in seconds
cache = TTL(maxsize=int(os.environ['CLEVERBOT_CACHE_MAX_SIZE']), ttl=int(os.environ['CLEVERBOT_CACHE_TTL']))
pw = {}

@app.route('/')
def hello_world():
    session_key = request.headers.get('Session-Key')
    botMessage = cache[session_key].single_exchange(request.json['message'])
    return jsonify({'response': botMessage})

@app.before_request
def before_request_func():
  session_key = request.headers.get('Session-Key')
  if session_key in cache:
    new = cache.pop(session_key)
    cache[session_key] = new # reset ttl
    return
  cache[session_key] = cleverbotfree.Cleverbot(pw)

if __name__ == "__main__":
  pw = cleverbotfree.sync_playwright()
  pw = pw.start()
  app.run(host="0.0.0.0")
  pw.stop()
