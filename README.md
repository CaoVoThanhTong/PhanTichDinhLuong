# PTDL

data engineer

# PhongTro123Crawler

test

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

### 2 . Xây dựng Docker image cho ứng dụng crawler

Sử dụng Dockerfile để xây dựng Docker image cho ứng dụng:

```bash
docker build -t phongtro123crawler .
```

Xoá

```bash
docker rm phongtro123crawler .
```

### 3.Chạy ứng dụng crawler

Chạy ứng dụng crawler và kết nối với MongoDB container:

```bash
docker run -d --name phongtro123crawler --network mynetwork -e Mongo_HOST=mymongodb phongtro123crawler
```

### 4.Kiểm tra logs

Kiểm tra logs để xem crawler có hoạt động đúng không:

```bash
docker logs phongtro123crawler

```

### Kiểm tra dữ liệu MongoDB

Sau khi crawler đã chạy, bạn có thể kiểm tra dữ liệu trong MongoDB:

```bash
docker exec -it mymongodb mongosh
show dbs
use mycrawlerdb
```
