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

Sau khi crawler đã chạy, bạn có thể kiểm tra dữ liệu traong MongoDB:

```bash
docker exec -it mymongodb mongosh
show dbs
use mycrawlerdb
show collections
```

### Setup postgres và pgAdmin 4
### 1.

```bash
docker pull postgres

```

### 2. Khơi động container postgres 

```bash
docker run --name sqltutorial -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres

```

### 3. 

```bash
docker pull dpage/pgadmin4

```

### 4.
```bash
docker run --name pgadmin-container -p 5050:80 -e PGADMIN_DEFAULT_EMAIL=user@domain.com -e PGADMIN_DEFAULT_PASSWORD=postgres -d dpage/pgadmin4

```




