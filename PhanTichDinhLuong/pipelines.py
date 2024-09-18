import json
import pymongo
import os 

class MongoDBPhanTichDinhLuongPipeline:
    def __init__(self):
        econnect = os.environ.get('MONGO_HOST')
        if not econnect:
            raise ValueError("MONGO_HOST environment variable is not set.")
        
        print(f"Connecting to MongoDB at: mongodb://{econnect}:27017")
        
        try:
            self.client = pymongo.MongoClient(f'mongodb://{econnect}:27017')
            self.db = self.client['dbmycrawler']
            print("Successfully connected to MongoDB")
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")
            raise e
        
    def process_item(self, item, spider):
        collection = self.db['tblphongtro']
        try:
           
            if not isinstance(item, dict):
                item = dict(item)
                
            collection.insert_one(item)
            print("Item inserted successfully")
            return item
        except Exception as e:
            print(f"Error inserting item into MongoDB: {e}")
            return None

class CSVDBPhanTichDinhLuongPipeline:
    def open_spider(self, spider):
        self.file = open('phongtro.csv', 'w', encoding='utf-8')
        self.file.write('link;title;address;price;acreage;published;hashtag;description\n')  # Điều chỉnh tiêu đề nếu cần

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        description = " ".join(item['description'])  # Nối danh sách mô tả thành một chuỗi
        line = f"{item['link']}; {item['title']}; {item['address']}; {item['price']}; {item['acreage']}; {item['published']}; {item['hashtag']}; {description}\n"
        self.file.write(line)
        return item
    
class JsonDBPhanTichDinhLuongPipeline:
    def process_item(self, item, spider):
        with open('phongtro.json', 'a', encoding='utf-8') as file:
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            file.write(line)
        return item