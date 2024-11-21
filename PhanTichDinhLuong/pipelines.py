import scrapy
import pymongo
import json
# from bson.objectid import ObjectId
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import csv
import os

class MongoDBPhanTichDinhLuongPipeline:
    def __init__(self):
        # Connection String
        # econnect = str(os.environ['Mongo_HOST'])
        self.client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
        # self.client = pymongo.MongoClient('mongodb://'+econnect+':27017')
        self.db = self.client['dbmycrawler'] #Create Database     
        pass
    
    def process_item(self, item, spider):
        collection = self.db['tblphongtro123'] #Create Collection or Table
        try:
            item.pop('link', None)  # Drop link item
            collection.insert_one(dict(item))
            return item
        except Exception as e:
            raise DropItem(f"Error inserting item: {e}")       
        pass

class CSVDBPhanTichDinhLuongPipeline:
    def open_spider(self, spider):
        self.file = open('phongtro.csv', 'w', encoding='utf-8')
        self.file.write('diachi;phanloai;dientich;gia;goitin;giogiactudo;tulanh;maylanh;Daydunoithat;maygiat;gac;khongchungchu\n')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = f"{item['address']}; {item['category']}; {item['acreage']}; {item['price']}; {item['package']}; {item['freetime']}; {item['refrigerator']}; {item['airConditioning']}; {item['fullyfurnished']}; {item['washer']}; {item['attic']}; {item['ownerless']}\n"
        self.file.write(line)
        return item