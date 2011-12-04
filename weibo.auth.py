#-*-coding:utf-8-*-
from weibopy.auth import OAuthHandler
from weibopy.api import API

#此应用的开发者密钥(此处应替换为创建应用时获取到的开发密钥)
APP_KEY = '1060838085'
APP_SECRET = 'eacff61d8ba3ea693369b6edb126d787'

#设定网页应用回调页面(桌面应用设定此变量为空)
BACK_URL = ""
#验证开发者密钥.
auth = OAuthHandler( APP_KEY, APP_SECRET, BACK_URL )
#获取授权页面网址.
auth_url = auth.get_authorization_url()
print auth_url
#引导用户输入授权码
verifier = raw_input("Please input the verify code: ")
#获取用户令牌密钥.
access_token = auth.get_access_token( verifier );
atKey = access_token.key;
atSecret = access_token.secret;

print atKey, atSecret
