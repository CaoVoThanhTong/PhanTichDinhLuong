import scrapy
from PhanTichDinhLuong.items import PhongTroItem

class PhongTro123Spider(scrapy.Spider):
    name = "PhongTro123Crawler"
    allowed_domains = ["phongtro123.com"]
    start_urls = ['https://phongtro123.com/']

    def parse(self, response):
        room_links = response.xpath('//ul[@class="post-listing aside clearfix"]/li/a/@href').getall()
        for link in room_links:
            yield scrapy.Request(url=response.urljoin(link), callback=self.parse_room_detail)

    def parse_room_detail(self, response):
        item = PhongTroItem()
        item['title'] = response.xpath('//span[@class="post-title"]/text()').get()
        item['price'] = response.xpath('//span[@class="post-price"]/text()').get()
        item['address'] = response.xpath('//div[@class="address"]/text()').get()
        item['description'] = response.xpath('//div[@class="post-main-content"]/p/text()').getall()
        yield item