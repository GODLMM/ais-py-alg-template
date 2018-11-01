from tornado import gen
from tornado import web
from tornado.concurrent import run_on_executor
import os

from utils.BaseHandler import BaseHandler
from alg.eg.main import mainAlg

class egHandler(BaseHandler):
    @gen.coroutine
    def get(self, *args, **kwargs):
        response = yield self.ping("www.baidu.com")
        print('reponse', response)
        self.finish('It works')

    @run_on_executor
    def ping(self, url):
        mainAlg(url)