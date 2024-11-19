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

    features_freetime = scrapy.Field(); #Giờ giất tự do
    features_refrigerator = scrapy.Field(); #Tủ lạnh
    features_airConditioning = scrapy.Field(); #Máy lạnh
    features_interiorFull = scrapy.Field(); #Đầy đủ nội thất
    features_washer = scrapy.Field(); #Máy giặt
    features_Attic = scrapy.Field(); #Có gác
    features_ownerless = scrapy.Field(); #Không chung chủ