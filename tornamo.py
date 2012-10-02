import tornado.ioloop
import tornado.web
import os.path
import tornado.options
import tornado.httpserver

class LoginHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.Islogin = False
    def get(self):
        self.render("templates/index.html" , IsLogin = self.Islogin)
    def post(self):
        if self.get_argument("Username") == "wangyufei" and self.get_argument("Password")=="19920820" :
            self.Islogin = True 
        self.render("templates/index.html" , IsLogin = self.Islogin )

class EmailHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/email.html", IsLogin = True)

class BoardHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/board.html", IsLogin = True)



class Application(tornado.web.Application):
   def __init__(self):
        handlers = [
             (r"/", LoginHandler),
             (r"/email", EmailHandler),
             (r"/board", BoardHandler)
        ]
        settings = dict(
           static_path=os.path.join(os.path.dirname(__file__), "static"),
           debug=True ,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
