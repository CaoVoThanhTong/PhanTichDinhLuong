import scrapy

class PhongTroItem(scrapy.Item):
    link = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    address = scrapy.Field()
    acreage = scrapy.Field()
    description = scrapy.Field()
    phone_number = scrapy.Field()
    package = scrapy.Field()
    category = scrapy.Field()
    public_date = scrapy.Field()
    expired_date = scrapy.Field()
    ad_type = scrapy.Field()
    target_renter = scrapy.Field()
    features = scrapy.Field()