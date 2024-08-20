import scrapy

class PhongTroItem(scrapy.Item):
    link = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    address = scrapy.Field()
    acreage = scrapy.Field()
    published = scrapy.Field()
    hashtag = scrapy.Field()
    description = scrapy.Field()