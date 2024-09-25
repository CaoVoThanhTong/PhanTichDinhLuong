import scrapy

class PhongTroItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    address = scrapy.Field()
    acreage = scrapy.Field()
    published = scrapy.Field()
    description = scrapy.Field()
    phone_number = scrapy.Field()
    package = scrapy.Field()
    category = scrapy.Field()
    public_date = scrapy.Field()
    expired_date = scrapy.Field()