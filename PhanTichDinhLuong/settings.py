ITEM_PIPELINES = {
   'PhanTichDinhLuong.pipelines.CSVDBUnitopPipeline': 100,
   # 'PhanTichDinhLuong.pipelines.JsonDBUnitopPipeline': 200,
}
SPIDER_MODULES = ['PhanTichDinhLuong.spiders']
NEWSPIDER_MODULE = 'PhanTichDinhLuong.spiders'