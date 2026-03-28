import math


def solve_quadratic(a, b, c):
    if a == 0:
        if b == 0:
            return 'infinite' if c == 0 else None
        return (-c / b,)

    delta = b * b - 4 * a * c
    if delta < 0:
        return ()
    elif delta == 0:
        x = -b / (2 * a)
        return (x,)
    else:
        sqrt_delta = math.sqrt(delta)
        x1 = (-b + sqrt_delta) / (2 * a)
        x2 = (-b - sqrt_delta) / (2 * a)
        return (x1, x2)


def main():
    try:
        a = float(input('Nhập a: ').strip())
        b = float(input('Nhập b: ').strip())
        c = float(input('Nhập c: ').strip())
    except ValueError:
        print('Giá trị không hợp lệ. Vui lòng nhập a, b, c là số.')
        return

    result = solve_quadratic(a, b, c)

    if result == 'infinite':
        print('Phương trình có vô số nghiệm.')
    elif result is None or len(result) == 0:
        print('Phương trình vô nghiệm.')
    elif len(result) == 1:
        print(f'Phương trình có nghiệm duy nhất: x = {result[0]:.6f}')
    else:
        x1, x2 = result
        print(f'Phương trình có hai nghiệm phân biệt: x1 = {x1:.6f}, x2 = {x2:.6f}')


if __name__ == '__main__':
    main()
