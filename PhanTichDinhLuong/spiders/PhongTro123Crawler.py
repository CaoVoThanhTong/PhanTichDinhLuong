import scrapy
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
        'https://phongtro123.com/cho-thue-mat-bang', #6
        ]
    
    def start_requests(self):
        for j in range(0, 1):
            for i in range(1, 2):
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
        # item['title'] = response.xpath('//h1[@class="page-h1"]/a/@title').get()
        # item['address'] = response.xpath('//address[@class="post-address"]/text()').get()
        # item['price'] = response.xpath('//div[@class="item price"]/span/text()').get()
        # item['acreage'] = response.xpath('//div[@class="item acreage"]/span/text()').get()
        # item['published'] = response.xpath('//div[@class="item published"]/span/text()').get()
        # item['description'] = response.xpath('//section[@class="section post-main-content"]/div/p/text()').getall()
        # item['phone_number'] = response.xpath('//section[@class="section post-contact"]/div[@class="section-content"]/table/tr[2]/td[2]/text()').get()
        # item['package'] = response.xpath('//table[@class="table"]//tr[td[contains(text(), "Gói tin:")]]/td/span/text()').get()
        # item['category'] = response.xpath('//table[@class="table"]//tr[td[contains(text(), "Chuyên mục:")]]/td/a/@title').get()
        # item['public_date'] = response.xpath('//table[@class="table"]//tr[td[contains(text(), "Ngày đăng:")]]/td/time/@title').get()
        # item['expired_date'] = response.xpath('//table[@class="table"]//tr[td[contains(text(), "Ngày hết hạn:")]]/td/time/@title').get()
        # item['ad_type'] = response.xpath('//table[@class="table"]//tr[td[contains(text(), "Loại tin rao:")]]/td[2]/text()').get()
        # item['target_renter'] = response.xpath('//table[@class="table"]//tr[td[contains(text(), "Đối tượng thuê:")]]/td[2]/text()').get()
        
        item['address'] = response.xpath('//address/text()').get()
        item['category'] = response.xpath('//a[@class="fs-6 d-flex h-100 border-bottom border-2 border-orange text-orange"]/text()').get()
        item['acreage'] = response.xpath('//span[contains(sup/text(), "2")]/text()').get()
        item['price'] = response.xpath('//span[@class="text-green fw-bold"]/text()').get()
        item['package'] = response.xpath('//div[contains(text(), "Gói tin:")]/span/text()').get()
        item['features'] = response.xpath('//i[@class="icon check-circle-fill green me-2"]/following-sibling::text()').getall()
        yield item
