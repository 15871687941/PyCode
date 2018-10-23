# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhaoxiaoshuoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 小说类别
    book_category = scrapy.Field()
    # 小说书名
    book_name = scrapy.Field()
    # 小说作者
    book_author = scrapy.Field()
    # 小说字数
    book_words = scrapy.Field()
    # 小说投票数
    book_vote = scrapy.Field()
    # 小说收藏数
    book_collection = scrapy.Field()
    # 小说状态
    book_status = scrapy.Field()

