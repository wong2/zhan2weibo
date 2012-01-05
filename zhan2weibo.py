#-*-coding:utf-8-*-

from google.appengine.api import memcache
from google.appengine.ext import db
import sys, os
from zhan  import Zhan
from weibo import Weibo
from config import *

class MyData(db.Model):
    last_id = db.StringProperty(required=True)

if __name__ == "__main__":
    data = MyData.get_or_insert(key_name='mydata', last_id="feed_3674946092032508824")
    last_post_id = data.last_id

    weibo = Weibo()
    zhan = Zhan("ishoothust")
    new_posts = zhan.get_new_posts(last_post_id)

    for post in new_posts:
        image_url = post["image_url"]
        msg = "#我们爱拍华科#%s " % post["title"].encode("utf-8")
        count = post["photo_count"] - 1
        msg += "还有%d张精彩照片呦:" % count if count else " "
        msg += post["link"].encode("utf-8")
        weibo.send(msg, image_url.encode("utf-8"))
        last_post_id = post["id"]

    data.last_id = last_post_id
    data.put()
