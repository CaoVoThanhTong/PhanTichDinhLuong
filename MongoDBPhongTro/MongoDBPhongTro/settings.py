ITEM_PIPELINES = {
   'PhanTichDinhLuong.pipelines.CSVDBPhanTichDinhLuongPipeline': 100,
   'PhanTichDinhLuong.pipelines.JsonDBPhanTichDinhLuongPipeline': 200,
   'PhanTichDinhLuong.pipelines.MongoDBPhanTichDinhLuongPipeline': 300,
}
SPIDER_MODULES = ['MongoDBPhongTro.spiders']
NEWSPIDER_MODULE = 'MongoDBPhongTro.spiders'
