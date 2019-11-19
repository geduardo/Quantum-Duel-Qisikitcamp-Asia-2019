import tornado.ioloop
import tornado.web

from tornado.options import define, options

define("port", default=5000, help="run on the given port", type=int)
tornado.options.parse_command_line()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Quantum Duel")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
