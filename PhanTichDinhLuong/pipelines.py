class CSVDBUnitopPipeline:
    def open_spider(self, spider):
        self.file = open('phongtro.csv', 'w', encoding='utf-8')
        self.file.write('title,price,address,description\n')  # Điều chỉnh tiêu đề nếu cần

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        description = " ".join(item['description'])  # Nối danh sách mô tả thành một chuỗi
        line = f"{item['title']},{item['price']},{item['address']},{description}\n"
        self.file.write(line)
        return item