FROM python:3

# Đặt thư mục làm việc
WORKDIR /usr/src/app

# Sao chép file requirements.txt và cài đặt các package
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

# Cài đặt các công cụ mạng nếu cần
RUN apt-get update && apt-get install -y iputils-ping net-tools

# Sao chép toàn bộ mã nguồn vào container
COPY . .

# Chạy scrapy spider sau khi chờ 60 giây (nếu cần)
CMD ["sh", "-c", "sleep 60 && python -m scrapy runspider PhanTichDinhLuong/spiders/PhongTro123Crawler.py"]
