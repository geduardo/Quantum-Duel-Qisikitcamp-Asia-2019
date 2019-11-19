import os
import tornado.ioloop
import tornado.web
from tornado.web import url
from tornado.options import define, options
from handler import MultiHandler

define("port", default=5000, help="run on the given port", type=int)
tornado.options.parse_command_line()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

def make_app():
    return tornado.web.Application([
        url(r"/", MainHandler, name='index'),
        url(r'/multi', MultiHandler, name='multi'),
    ],
    template_path=os.path.join(os.getcwd(),  "templates"),
    static_path=os.path.join(os.getcwd(),  "static"),
    )

if __name__ == "__main__":
    app = make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
