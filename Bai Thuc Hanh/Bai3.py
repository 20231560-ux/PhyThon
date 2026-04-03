# Bài 3: Tạo file 'demo_file1.txt' với nội dung đã cho, rồi in ra:
# a) in toàn bộ nội dung trên một dòng
# b) in nội dung theo từng dòng

file_path = "demo_file1.txt"
content = "Thuc\nhanh\nvoi\nfile\nIO\n"

# Tạo/ghi nội dung file
with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Đã tạo file: {file_path}")

# a) In toàn bộ nội dung trên một dòng (thay thế newline bằng khoảng trắng hẹp)
with open(file_path, "r", encoding="utf-8") as f:
    raw = f.read()
    one_line = raw.replace("\n", " ").strip()
    print("\n(a) Nội dung trên một dòng:")
    print(one_line)

# b) In nội dung theo từng dòng
print("\n(b) Nội dung theo từng dòng:")
with open(file_path, "r", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
        print(f"{i}: {line.rstrip()}")
