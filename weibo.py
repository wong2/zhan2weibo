#-*-coding:utf-8-*-
from weibopy.auth import OAuthHandler
from weibopy.api import API
from weibopy.error import WeibopError
from config import *

class Weibo:
    def __init__(self):
        #设定网页应用回调页面(桌面应用设定此变量为空)
        BACK_URL = ""
        #验证开发者密钥.
        auth = OAuthHandler( APP_KEY, APP_SECRET, BACK_URL )
        #设定用户令牌密钥.
        auth.setToken( TOKEN_KEY, TOKEN_SECRET )
        #绑定用户验证信息.
        self.api = API(auth);

    def send(self, message, image_path=None):
        try:
            if image_path:
                self.api.upload(image_path, message);
            else:
                self.api.update_status(message);
        except WeibopError, e:
            print e.reason

if __name__ == "__main__":
    weibo = Weibo()
    weibo.send("", "x_large_TKZK_361c0000b66a1269.jpg")
