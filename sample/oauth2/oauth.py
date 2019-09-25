# -*- coding: utf-8 -*-

import requests
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler

appid = 1
secret = ""

def get_access_token(auth_code):
    url = "https://ad.toutiao.com/open_api/oauth2/access_token/"
    params = {
        "appid":appid,
        "secret":secret,
        "grant_code":"auth_code",
        "auth_code":auth_code
    }
    rsp = requests.post(url, json=params)
    rsp_data = rsp.json()
    return rsp_data

class MainHandler(RequestHandler):

    def get(self):
        self.write("hello oauth2")

class CallbackHandler(RequestHandler):

    def get(self):
        #TODO 获取参数中的 auth_code
        #TODO auth_code 转 access_token refresh_token
        #TODO 存入 reids

        self.write("success")

def make_app():
    return Application(
        [
            (r"/", MainHandler),
        ]
    )

if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    IOLoop.current().start()
