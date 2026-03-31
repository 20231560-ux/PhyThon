# Bài 1: Nhập vào số nguyên n từ bàn phím.
# In ra tích của 2 nhân với các giá trị nhỏ hơn n.
# Ví dụ: n = 4 => 2 = 2*1, 4 = 2*2, 6 = 2*3.

try:
    n = int(input("Nhập số nguyên n: "))
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")
    raise SystemExit(1)

if n <= 0:
    print("n cần là số nguyên dương.")
    raise SystemExit(1)

for i in range(1, n):
    tich = 2 * i
    print(f"{tich} = 2*{i}")
