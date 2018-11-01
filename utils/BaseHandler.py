import tornado.web
from utils.State import state
import json

class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(BaseHandler,self).__init__(application, request, **kwargs)
        self.executor = state.executor
        
    def prepare(self):
        if self.request.headers.get("Content-Type","").startswith("application/json"):
            self.json_args=json.loads(self.request.body)
        else:
            self.json_args=None
            
    def set_default_headers(self):
        self.set_header("Content-Type","application/json")
            