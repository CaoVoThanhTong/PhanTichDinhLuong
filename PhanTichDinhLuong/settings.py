ITEM_PIPELINES = {
   'PhanTichDinhLuong.pipelines.CSVDBPhanTichDinhLuongPipeline': 100,
   # 'PhanTichDinhLuong.pipelines.JsonDBPhanTichDinhLuongPipeline': 200,
   'PhanTichDinhLuong.pipelines.MongoDBPhanTichDinhLuongPipeline': 300,
}
SPIDER_MODULES = ['PhanTichDinhLuong.spiders']
NEWSPIDER_MODULE = 'PhanTichDinhLuong.spiders'
