from glob import glob
from os.path import splitext
import Image
import math

import os

import tornado.ioloop
import tornado.web

import pprint
pp = pprint.PrettyPrinter(indent=4)

import final

class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("static/index.html")

    def post(self):
        print self.request.arguments
        #jpg_temp = splitext(jpg1)[0]+"_Resized1.jpg"
        #nim.save(jpg_temp, quality = 100)


settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static")
}

application = tornado.web.Application([
    (r"/", MainHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

