#!/usr/bin/python2
# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import os.path
import tornado.options
import tornado.httpserver
from datetime import datetime

class LoginHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.Islogin = False
    def get(self):
        self.render("templates/index.html")
    def post(self):
        if self.get_argument("Username") == "wangyufei" and\
                self.get_argument("Password")=="19920820" :
            self.render("templates/index.html")

class EmailHandler(tornado.web.RequestHandler):
    def get(self):
        mails = [
            {
                "title":"这傻B是谁",
                "touserid":"LTaoist",
                "fromuserid":"gcc",
                "posttime":"刚刚",
                "read":False,
                },
            ]
        mails = mails * 20
        self.render("templates/mail.html", mails=mails)

class BoardHandler(tornado.web.RequestHandler):
    def get(self):
        post = [
            {
                "title":"这傻b是谁",
                "owner":"LTaoist",
                "replyid":3,
                "posttime": '刚刚',
                "read":False,
                "gmark":True,
                "mmark":True,
                },
            {
                "title":"Re: 这傻b是谁",
                "owner":"LTaoist",
                "replyid":4,
                "posttime": '刚刚',
                "read":False,
                "gmark":False,
                "mmark":False,
                },
            {
                "title":"Re: 这傻b是谁",
                "owner":"LTaoist",
                "replyid":3,
                "posttime": '刚刚',
                "read":True,
                "gmark":True,
                "mmark":False,
                },
            {
                "title":"老了",
                "owner":"gcc",
                "replyid":7,
                "posttime": '刚刚',
                "read":False,
                "gmark":False,
                "mmark":True,
                },
            {
                "title":"这傻b是谁",
                "owner":"LTaoist",
                "replyid":3,
                "posttime": '刚刚',
                "read":False,
                "gmark":False,
                "mmark":False,
                },
            {
                "title":"Re: 这傻b是谁",
                "owner":"LTaoist",
                "replyid":4,
                "posttime": '刚刚',
                "read":False,
                "gmark":False,
                "mmark":False,
                },
            {
                "title":"Re: 这傻b是谁",
                "owner":"LTaoist",
                "replyid":3,
                "posttime": '刚刚',
                "gmark":False,
                "mmark":False,
                "read":True,
                },
            {
                "title":"老了",
                "owner":"gcc",
                "replyid":7,
                "posttime": '刚刚',
                "gmark":False,
                "mmark":False,
                "read":False,
                },
            {
                "title":"Re: 这傻b是谁",
                "owner":"LTaoist",
                "replyid":3,
                "posttime": '刚刚',
                "gmark":False,
                "mmark":False,
                "read":True,
                },
            {
                "title":"老了",
                "owner":"gcc",
                "replyid":7,
                "posttime": '刚刚',
                "gmark":False,
                "mmark":False,
                "read":False,
                },
            ]
        post = post * 3
        self.render("templates/board.html", post=post)

class Application(tornado.web.Application):
   def __init__(self):
        handlers = [
             (r"/", LoginHandler),
             (r"/mail", EmailHandler),
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
