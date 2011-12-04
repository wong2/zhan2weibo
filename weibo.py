#-*-coding:utf-8-*-
from weibopy.auth import OAuthHandler
from weibopy.api import API
from weibopy.error import WeibopError

class Weibo:
    def __init__(self):
        #此应用的开发者密钥(此处应替换为创建应用时获取到的开发密钥)
        APP_KEY = '1060838085'
        APP_SECRET = 'eacff61d8ba3ea693369b6edb126d787'

        #设定网页应用回调页面(桌面应用设定此变量为空)
        BACK_URL = ""
        #验证开发者密钥.
        auth = OAuthHandler( APP_KEY, APP_SECRET, BACK_URL )
        #用户的TOKEN数据
        TOKEN_KEY = "7fcedfb06dc2bb266e2d91fba5767a4a"
        TOKEN_SECRET = "1da42d9a9053c680621ec0081a05eb6a"
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
