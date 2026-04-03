# Bài 2: Ghi 1 đoạn văn bản vào một tập tin và hiển thị nội dung đó
# Hướng dẫn sử dụng:
# 1) Chạy chương trình.
# 2) Nhập tên file để ghi (ví dụ: output.txt). Nếu file đã tồn tại sẽ ghi đè.
# 3) Nhập nội dung văn bản (Enter kết thúc dạng đa dòng, nhập dòng trống để kết thúc nhập).

file_name = input("Nhập tên file để ghi (ví dụ: output.txt): ").strip()

print("Nhập nội dung văn bản. Nhập một dòng trống để kết thúc:")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

if not lines:
    print("Không có nội dung để ghi.")
else:
    try:
        with open(file_name, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"\nĐã ghi {len(lines)} dòng vào file: {file_name}")

        print(f"\n--- Nội dung file '{file_name}' ---")
        with open(file_name, "r", encoding="utf-8") as f:
            print(f.read())
    except IOError as e:
        print(f"Lỗi khi ghi/đọc file: {e}")
