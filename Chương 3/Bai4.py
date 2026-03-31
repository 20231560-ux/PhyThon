# Bài 4: Nhập vào 1 số nguyên n < 20 từ bàn phím.
# In ra các số thỏa mãn điều kiện chia hết cho 5 hoặc chia hết cho 7.

try:
    n = int(input("Nhập số nguyên n (<20): "))
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")
    raise SystemExit(1)

if n >= 20:
    print("n cần nhỏ hơn 20.")
    raise SystemExit(1)

for i in range(1, n + 1):
    if i % 5 == 0 or i % 7 == 0:
        print(i)
