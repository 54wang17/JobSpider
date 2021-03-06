# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_type = scrapy.Field()
    name = scrapy.Field()
    company = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field() 
    category = scrapy.Field()
    url = scrapy.Field()
    source = scrapy.Field()


    pass
