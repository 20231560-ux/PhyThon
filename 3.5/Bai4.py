import math

def main():
    try:
        n = int(input('Nhập số nguyên dương: ').strip())
    except ValueError:
        print('Giá trị không hợp lệ. Hãy nhập một số nguyên dương.')
        return

    if n <= 0:
        print('Giá trị không hợp lệ. Hãy nhập số nguyên dương lớn hơn 0.')
        return

    chia2 = (n % 2 == 0)
    chia3 = (n % 3 == 0)

    if chia2 and chia3:
        print(f'{n} chia hết cho cả 2 và 3.')
    elif chia2:
        print(f'{n} chia hết cho 2 nhưng không chia hết cho 3.')
    elif chia3:
        print(f'{n} chia hết cho 3 nhưng không chia hết cho 2.')
    else:
        print(f'{n} không chia hết cho cả 2 và 3.')


if __name__ == '__main__':
    main()
