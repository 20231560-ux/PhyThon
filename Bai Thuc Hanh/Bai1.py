# Bài 1: Đọc n dòng đầu tiên của một tập tin theo n nhập từ bàn phím
# Hướng dẫn sử dụng:
# 1) Cần có file ví dụ, ví dụ: "input.txt" (ở cùng thư mục hoặc đường dẫn đầy đủ).
# 2) Chạy chương trình và nhập tên file, sau đó nhập số n.

file_name = input("Nhập tên file (ví dụ: input.txt): ").strip()
try:
    n = int(input("Nhập số dòng cần đọc (n): ").strip())
    if n <= 0:
        raise ValueError("n phải là số nguyên dương")
except ValueError as e:
    print("Giá trị n không hợp lệ:", e)
    raise SystemExit(1)

try:
    with open(file_name, "r", encoding="utf-8") as f:
        print(f"\n--- Nội dung {n} dòng đầu tiên của file '{file_name}' ---")
        for i in range(n):
            line = f.readline()
            if line == "":
                print(f"[Hết file sau {i} dòng]")
                break
            print(f"{i+1}: {line.rstrip()}")
except FileNotFoundError:
    print(f"Không tìm thấy file: {file_name}")
except IOError as e:
    print(f"Lỗi đọc file: {e}")
