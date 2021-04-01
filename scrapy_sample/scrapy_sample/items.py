# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapySampleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Book(scrapy.Item):
  title = scrapy.Field()
  description = scrapy.Field()
  file_urls = scrapy.Field()
  files = scrapy.Field()

class WeatherItem(scrapy.Item):
    city = scrapy.Field()
    temp = scrapy.Field()
    air_quality = scrapy.Field()
    cond = scrapy.Field()
