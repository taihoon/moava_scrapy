# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import re
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from urllib.parse import urlparse, parse_qs
from w3lib.html import remove_tags

def filter_youtube(url):
    query = urlparse(url)
    if "youtube" in query.hostname:
        if query.path == "/watch":
            return parse_qs(query.query)["v"][0]
        elif query.path.startswith(("/embed/", "/v/")):
            return query.path.split("/")[2]
    elif "youtu.be" in query.hostname:
        return query.path[1:]

def parse_post_id(url, loader_context):
    setting = loader_context.get("setting")
    m = re.match(setting["id_match_reg"], url)
    if m is not None:
        return m.group(1)

class MoavaItem(scrapy.Item):
    site = scrapy.Field(
        output_processor=TakeFirst()
    )
    post_id = scrapy.Field(
        input_processor=MapCompose(parse_post_id),
        output_processor=TakeFirst()
    )
    title = scrapy.Field(
        input_processor=MapCompose(remove_tags, lambda string: string.strip()),
        output_processor=Join()
    )
    youtube_ids = scrapy.Field(
        input_processor=MapCompose(filter_youtube)
    )
    pass
