# -*- coding: utf-8 -*-

import scrapy
from scrapy.loader import ItemLoader

from .items import MoavaItem
from .utils import youtube

class MoavaSpider(scrapy.Spider):
    name = "moava"

    def start_requests(self):
        settings = self.settings.get("CUSTOM_SETTINGS")
        for setting in settings:
            for url in reversed(setting["page_urls"]):
                request = scrapy.Request(url=url, callback=self.parse_list, meta={"setting": setting})
                yield request

    def parse_list(self, response):
        setting = response.meta["setting"]
        post_hrefs = response.css(setting["post_href_query"]).extract()
        for href in reversed(post_hrefs):
            if href is not None:
                request = response.follow(url=href, callback=self.parse_post, meta={"setting": setting})
                yield request

    def parse_post(self, response):
        setting = response.meta["setting"]
        loader = ItemLoader(item=MoavaItem(), setting=setting, response=response)
        loader.add_value("site", setting["site"])
        loader.add_value("post_id", response.url)
        loader.add_css("title", setting["title_query"])
        loader.add_css("youtube_ids", setting["iframe_srcs_query"])
        item = loader.load_item()
        return item

        # yield {
        #     "site": setting["site"],
        #     "post": response.url,
        #     "title": response.css(setting["title_query"]).extract_first().strip(),
        #     "youtubes": response.css(setting["iframe_srcs_query"]).extract()
        # }
