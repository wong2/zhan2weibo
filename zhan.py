#-*-coding:utf-8-*-
import sys
from google.appengine.api import urlfetch
from BeautifulSoup import BeautifulSoup


class Zhan:
    def __init__(self, zhan_name):
        self.url = "http://zhan.renren.com/" + zhan_name

    def get_new_posts(self, last_post_id):
        _now_page = 0
        new_posts = []
        while True:
            html = urlfetch.fetch("%s?page=%d" % (self.url, _now_page)).content
            soup = BeautifulSoup(html)
            posts = soup.findAll("article", {"class" : "post-photo post"})
            for post in posts:
                post_id = post["id"]
                try:
                    if post_id == last_post_id:
                        new_posts.reverse()
                        return new_posts
                    new_post = {}
                    new_post["id"] = post_id
                    new_post["link"] = self.url + "?gid=" + post_id[5:]
                    _title = post.find("h4").string
                    _first_photo = post.find("div", {"class" : "photo"})
                    new_post["image_url"] = _first_photo.find("img")["data-src"]
                    if not _title:
                        _title = _first_photo.nextSibling.nextSibling.string.strip()
                    new_post["title"] = _title.strip()
                    new_posts.append(new_post)
                except:
                    continue
            _now_page += 1
            print "Page %d" % _now_page
    
if __name__ == "__main__":
    zhan = Zhan("ishoothust")
    new_posts = zhan.get_new_posts("feed_3674946092032248595")
    for new_post in new_posts:
        print new_post["title"]
