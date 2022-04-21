from gevent import monkey
monkey.patch_all()

from flask import Flask
from flask import request, session
import cleverbotfree
from cachetools import cached, LRUCache, TTLCache


class Ficker(TTLCache):
    def __init__(self, maxsize, ttl, timer=time.monotonic, getsizeof=None):
        LRUCache.__init__(self, maxsize, missing, getsizeof)
        self.__evict = evict

    def popitem(self):
      print("hello")  
      key, val = TTLCache.popitem(self)
      val.close()
      return key, val

app = Flask(__name__)
roffler = Ficker(ttl=30)

@app.route('/')
def hello_world():
    data = request.json
    lol = request.headers.get('fick')
    message = data['message']
    botMessage = roffler[lol].single_exchange(message)
    return botMessage

@app.before_request
def before_request_func():
  lol = request.headers.get('fick')
  if lol in roffler:
    return
  roffler[lol] = cleverbotfree.Cleverbot(p_w)

if __name__ == "__main__":
  pw = cleverbotfree.sync_playwright():
  pw = pw.__enter__()
  app.run(host="0.0.0.0")
  pw.__exit__()
