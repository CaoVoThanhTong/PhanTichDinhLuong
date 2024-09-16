import json
import pymongo

class MongoDBPhanTichDinhLuongPipeline:
    def __init__(self):
        
        self.client = pymongo.MongoClient('mongodb://localhost:27017')
        self.db = self.client['dbmycrawler'] #Database      
        pass
    
    def process_item(self, item, spider):
        
        collection =self.db['tblphongtro'] #Table
        try:
            collection.insert_one(dict(item))
            return item
        except Exception as e:
            print(f"Error inserting item: {e}")       
        pass

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