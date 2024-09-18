# PTDL

data engineer

# PhongTro123 Crawler

PhongTro123 Crawler là một ứng dụng Scrapy để crawl dữ liệu từ trang phongtro123.com và lưu trữ dữ liệu vào MongoDB.

## Yêu cầu

Để chạy ứng dụng này, bạn cần cài đặt:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Chạy ứng dụng với Docker

### 1. Tạo Docker Network và MongoDB container

Tạo Docker network để các container giao tiếp với nhau, sau đó khởi chạy MongoDB container:

```bash
docker network create mynetwork
docker run -d --name mymongodb --network mynetwork -p 27017:27017 mongo
```
