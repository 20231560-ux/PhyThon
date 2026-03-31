# Bai2.py
# Nhập vào số nguyên dương n từ bàn phím.
# Tính và in ra n! (giải thừa của n) bằng vòng while.

n = int(input("Nhập số nguyên dương n: "))
if n < 0:
    print("Yêu cầu nhập số nguyên dương hoặc 0.")
else:
    i = 1
    giaithua = 1
    while i <= n:
        giaithua *= i
        i += 1
    print(f"{n}! = {giaithua}")
