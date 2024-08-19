import scrapy

class PhongTroItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    address = scrapy.Field()
    description = scrapy.Field()