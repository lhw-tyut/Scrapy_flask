# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobspidersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jobPosition = scrapy.Field()
    jobCompany = scrapy.Field()
    jobAddress = scrapy.Field()
    jobSalary = scrapy.Field()
    jobPublicDate = scrapy.Field()
    jobSource = scrapy.Field()
    pass
