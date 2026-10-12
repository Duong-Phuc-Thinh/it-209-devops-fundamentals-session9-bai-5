# Bài 5: Khởi chạy dịch vụ đơn giản với Docker Compose

Thư mục nộp bài: `homework/session_09/ex5/`

## Giới thiệu
Bài tập thực hành cấu hình và vận hành một dịch vụ web Nginx đơn giản thông qua công cụ Docker Compose CLI v2 thay vì sử dụng câu lệnh `docker run` thủ công.

## Cấu trúc thư mục
- `docker-compose.yml`: Cấu hình định nghĩa service `web` chạy container `nginx:alpine` và ánh xạ cổng `8082:80`.
- `main.py`: Script Python tự động hóa quy trình chạy `docker compose up -d`, kiểm tra HTTP request tới `http://localhost:8082` và dọn dẹp bằng `docker compose down`.
- `README.md`: Hướng dẫn cấu hình và thực thi.

## Hướng dẫn sử dụng

### 1. Sử dụng trực tiếp bằng Docker Compose CLI
1. Khởi chạy dịch vụ ở chế độ nền (detached mode):
   ```bash
   docker compose up -d
   ```
2. Kiểm tra danh sách dịch vụ đang chạy:
   ```bash
   docker compose ps
   ```
3. Kiểm tra trang web qua curl hoặc trình duyệt:
   ```bash
   curl http://localhost:8082
   ```
4. Dừng và gỡ bỏ container:
   ```bash
   docker compose down
   ```

### 2. Sử dụng kịch bản kiểm tra tự động (Python)
Chạy script Python để tự động thực hiện toàn bộ chu trình trên:
```bash
python main.py
```
