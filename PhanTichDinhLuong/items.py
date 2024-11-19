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

    freetime = scrapy.Field()  # Giờ giấc tự do
    refrigerator = scrapy.Field()  # Tủ lạnh
    airConditioning = scrapy.Field()  # Máy lạnh
    elevator = scrapy.Field()  # Thang máy
    washer = scrapy.Field()  # Máy giặt
    attic = scrapy.Field()  # Có gác
    ownerless = scrapy.Field()  # Không chung chủ