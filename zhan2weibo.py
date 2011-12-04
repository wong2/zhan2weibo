#-*-coding:utf-8-*-

from zhan  import Zhan
from weibo import Weibo
import sys
import os
from google.appengine.api import memcache
from google.appengine.ext import db

class MyData(db.Model):
    last_id = db.StringProperty(required=True)

if __name__ == "__main__":
    data = MyData.get_or_insert(key_name='mydata', last_id="feed_3674946092032508824")
    last_post_id = data.last_id

    weibo = Weibo()
    zhan = Zhan("ishoothust")
    new_posts = zhan.get_new_posts(last_post_id)

    length = len(new_posts)
    for i, post in enumerate(new_posts):
        image_url = post["image_url"]
        weibo.send("#我们爱拍华科#" + post["title"].encode("utf-8") + " " + post["link"].encode("utf-8"), 
                image_url.encode("utf-8"))
        last_post_id = post["id"]
    data.last_id = last_post_id
    data.put()
