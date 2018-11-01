from tornado import gen
from tornado import web
from tornado.concurrent import run_on_executor
import os
import json

from utils.BaseHandler import BaseHandler
from alg.FaceDetect.main import alg_process
from api.FaceDetect.jsonFormat import jsonFormat

class detectHandler(BaseHandler):
    @gen.coroutine
    def post(self, *args, **kwargs):
        self.prepare()
        result = yield self.process()
        res = jsonFormat(*result)
        self.set_default_headers()
        self.write(json.dumps(res))

    @run_on_executor
    def process(self):
        return alg_process(self.json_args['image'])
        