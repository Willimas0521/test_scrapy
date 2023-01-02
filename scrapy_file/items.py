# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    area = scrapy.Field()
    price = scrapy.Field()
    address = scrapy.Field()
    name = scrapy.Field()
    total = scrapy.Field()
    type = scrapy.Field()



print('编译完成')