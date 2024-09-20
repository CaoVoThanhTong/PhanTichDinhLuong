FROM python:3

# Đặt thư mục làm việc
WORKDIR /usr/src/app

# Sao chép file requirements.txt và cài đặt các package
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ mã nguồn vào container
COPY . .

# Chạy scrapy spider sau khi chờ 60 giây (nếu cần)
CMD ["sh", "-c", "sleep 60 && python -m scrapy runspider MongoDBPhongTro/spiders/PhongTro123Crawler.py"]
