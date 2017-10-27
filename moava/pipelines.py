# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import time
import pyrebase
from scrapy.exceptions import DropItem

class YoutubePipeline(object):
    def process_item(self, item, spider):
        if "youtube_ids" in item:
            return item
        else:
            raise DropItem()

class FirebasePipeline(object):
    def __init__(self, firebase_config):
        self.firebase_config = firebase_config

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            firebase_config=crawler.settings.get("FIREBASE_CONFIG")
        )

    def open_spider(self, spider):
        self.firebase = pyrebase.initialize_app(self.firebase_config)
        self.db = self.firebase.database()

    def process_item(self, item, spider):
        for youtube_id in item["youtube_ids"]:
            uid = item["site"] + item["post_id"] + youtube_id
            self.db.child("videos").child(uid).set({
                "site": item["site"],
                "post_id": item["post_id"],
                "title": item["title"],
                "youtube_id": youtube_id,
                "created": time.time()
            })
        raise DropItem()
        #return item
