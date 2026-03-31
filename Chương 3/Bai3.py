# Bài 3: In ra các số trong khoảng từ 80 - 100 thoả mãn vừa chia hết cho 2, vừa chia hết cho 3.

for x in range(80, 101):
    if x % 2 == 0 and x % 3 == 0:
        print(x)
