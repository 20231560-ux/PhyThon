# Bài 2: Nhập vào 1 số nguyên n từ bàn phím.
# Nếu số đó lớn hơn 10 thì in ra dòng text: Số nhập vào phải bé hơn 10.
# Nếu số đó nhỏ hơn hoặc bằng 10: In ra những số chẵn từ 1 đến n.

try:
    n = int(input("Nhập số nguyên n: "))
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")
    raise SystemExit(1)

if n > 10:
    print("Số nhập vào phải bé hơn 10.")
else:
    for i in range(2, n + 1, 2):
        print(i)
