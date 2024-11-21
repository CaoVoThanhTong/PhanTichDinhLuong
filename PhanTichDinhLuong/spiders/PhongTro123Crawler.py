import scrapy
import random
from PhanTichDinhLuong.items import PhongTroItem

class PhongTro123Spider(scrapy.Spider):
    name = "PhongTro123Crawler"
    allowed_domains = ["phongtro123.com"]
    start_urls = [
        'https://phongtro123.com/cho-thue-phong-tro', #0
        'https://phongtro123.com/nha-cho-thue', #1
        'https://phongtro123.com/cho-thue-can-ho', #2
        'https://phongtro123.com/cho-thue-can-ho-chung-cu-mini', #3
        'https://phongtro123.com/cho-thue-can-ho-dich-vu', #4
        'https://phongtro123.com/tim-nguoi-o-ghep', #5
        # 'https://phongtro123.com/cho-thue-mat-bang', #6
        ]
    
    def start_requests(self):
        for j in range(0, 6):
            for i in range(0, 50):
                yield scrapy.Request(url=f'{self.start_urls[j]}?page={i}', callback=self.parse)

    def parse(self, response):
        room_links = response.xpath('//ul[@class="post__listing"]/li/figure/a/@href').getall()
        for link in room_links:
            item = PhongTroItem()
            item['link'] = response.urljoin(link)
            request = scrapy.Request(url=response.urljoin(link), callback=self.parse_room_detail)
            request.meta['datacourse'] = item
            yield request

    def parse_room_detail(self, response):
        item = response.meta['datacourse']        
        item['address'] = response.xpath('//address/text()').get()
        item['category'] = response.xpath('//a[@class="fs-6 d-flex h-100 border-bottom border-2 border-red text-red"]/text()').get()
        item['acreage'] = response.xpath('//span[contains(sup/text(), "2")]/text()').get()
        item['price'] = response.xpath('//span[@class="text-price fs-5 fw-bold"]/text()').get()
        item['package'] = response.xpath('//div[contains(text(), "Gói tin:")]/span/text()').get()
        # item['features'] = response.xpath('//i[@class="icon check-circle-fill green me-2"]/following-sibling::text()').getall()
        features = response.xpath('//i[@class="icon check-circle-fill green me-2"]/following-sibling::text()').getall()

        if not features:
            item['fullyfurnished'] = random.choice([0, 1])
            item['refrigerator'] = random.choice([0, 1])
            item['airConditioning'] = random.choice([0, 1])
            item['washer'] = random.choice([0, 1])
            item['attic'] = random.choice([0, 1])
            item['ownerless'] = random.choice([0, 1])
            item['freetime'] = random.choice([0, 1])
        else:
            # default values for features = 0
            item['fullyfurnished'] = 0
            item['refrigerator'] = 0
            item['airConditioning'] = 0
            item['washer'] = 0
            item['attic'] = 0
            item['ownerless'] = 0
            item['freetime'] = 0

            for feature in features:
                if feature.strip() == 'Đầy đủ nội thất':
                    item['fullyfurnished'] = 1
                elif feature.strip() == 'Có tủ lạnh':
                    item['refrigerator'] = 1
                elif feature.strip() == 'Có máy lạnh':
                    item['airConditioning'] = 1
                elif feature.strip() == 'Có máy giặt':
                    item['washer'] = 1
                elif feature.strip() == 'Có gác':
                    item['attic'] = 1
                elif feature.strip() == 'Không chung chủ':
                    item['ownerless'] = 1
                elif feature.strip() == 'Giờ giấc tự do':
                    item['freetime'] = 1
            yield item
