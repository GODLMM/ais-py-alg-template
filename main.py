import tornado.ioloop
import tornado.web
import tornado.httpserver
from tornado.options import define,options
import os 
import logging
from concurrent.futures import ThreadPoolExecutor
from api import handlers 
from utils.State import state
from utils.Config import config

define("port",default=config['serverPort'],help='algorithm api port,using 29000-29010',type=int)
define("ip",default=config['serverIp'],help='the ip to access the server,using 29000-29010',type=str)
define("threads",default=10,help='the python threads in tornado for async io',type=int)
def main():
    tornado.options.parse_command_line()
    state.settings={
        "static_path":os.path.join(os.path.dirname(__file__),"static")
    }
    state.executor=ThreadPoolExecutor(options.threads)
    application=tornado.web.Application(handlers,**state.settings)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)

    logging.basicConfig()
    logging.info('Start threads:%d'%options.threads)
    logging.getLogger().setLevel(logging.DEBUG)
    logging.debug('start server as :http://%s:%d'%(options.ip,options.port))
    tornado.ioloop.IOLoop.current().start()
if __name__=='__main__':
    main()
