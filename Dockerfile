# Sử dụng Python 3 slim
FROM python:3-slim

# Không ghi đè bytecode và tắt buffering để dễ dàng kiểm soát log
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Đặt thư mục làm việc
WORKDIR /app

# Copy file requirements.txt và cài đặt các thư viện cần thiết
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy mã nguồn vào container
COPY . /app

# Chạy ứng dụng crawler
CMD ["python", "PhanTichDinhLuong/spiders/PhongTro123Crawler.py"]