import subprocess
import sys
import time
import urllib.request

def run_command(command):
    print(f"Executing: {' '.join(command)}")
    result = subprocess.run(command, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout.strip())
    if result.stderr:
        print(result.stderr.strip())
    if result.returncode != 0:
        print(f"Command failed with exit code {result.returncode}")
        sys.exit(result.returncode)
    return result

def main():
    url = "http://localhost:8082"
    try:
        print("=== Bắt đầu khởi chạy dịch vụ với Docker Compose ===")
        run_command(["docker", "compose", "up", "-d"])

        print("\n=== Kiểm tra trạng thái dịch vụ (docker compose ps) ===")
        run_command(["docker", "compose", "ps"])

        print("\n=== Chờ dịch vụ khởi động và kiểm tra HTTP request ===")
        time.sleep(2)
        
        req = urllib.request.urlopen(url, timeout=5)
        status_code = req.getcode()
        content = req.read().decode('utf-8')
        
        print(f"HTTP Status: {status_code}")
        if "Welcome to nginx!" in content:
            print("Test thành công: Nginx welcome page đã được phục vụ tại cổng 8082!")
        else:
            print("Cảnh báo: Nội dung phản hồi không chứa chuỗi chào mừng mặc định của Nginx.")

    except Exception as e:
        print(f"Lỗi trong quá trình kiểm tra: {e}")
    finally:
        print("\n=== Hạ dịch vụ (docker compose down) ===")
        run_command(["docker", "compose", "down"])
        print("Hoàn tất quy trình.")

if __name__ == "__main__":
    main()
