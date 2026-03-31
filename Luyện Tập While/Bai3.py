# Bai3.py
# Nhập vào số nguyên dương n từ bàn phím.
# Kiểm tra xem n có phải số nguyên tố không.
# Nếu là số nguyên tố thì in: Đây là số nguyên tố.
# Ngược lại in: Không phải số nguyên tố.

n = int(input("Nhập số nguyên dương n: "))
if n <= 1:
    print("Không phải số nguyên tố")
else:
    i = 2
    is_prime = True
    while i * i <= n:
        if n % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print("Đây là số nguyên tố")
    else:
        print("Không phải số nguyên tố")
