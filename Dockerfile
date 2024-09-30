# Scrapy setup
FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y iputils-ping net-tools
COPY . .
CMD ["sh", "-c", "sleep 60 && python -m scrapy runspider PhanTichDinhLuong/spiders/PhongTro123Crawler.py"]

# Spark setup
FROM apache/spark:latest
USER root
WORKDIR /opt/spark
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip3 install -r requirements.txt
CMD ["jupyter-lab", "--allow-root", "--no-browser", "--ip=0.0.0.0"]
