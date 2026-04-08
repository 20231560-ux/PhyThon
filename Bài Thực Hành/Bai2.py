from math import gcd

class Fraction:
    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ValueError("Mẫu số không được bằng 0")
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def simplify(self):
        g = gcd(self.numerator, self.denominator)
        self.numerator //= g
        self.denominator //= g
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator
        return self

    def __str__(self):
        return str(self.numerator) if self.denominator == 1 else f"{self.numerator}/{self.denominator}"

    def _binop(self, other, op):
        if not isinstance(other, Fraction):
            return NotImplemented
        a = self.numerator * other.denominator
        b = other.numerator * self.denominator
        d = self.denominator * other.denominator
        return Fraction(op(a, b), d)

    def __add__(self, other):
        return self._binop(other, lambda a, b: a + b)

    def __sub__(self, other):
        return self._binop(other, lambda a, b: a - b)

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        if other.numerator == 0:
            raise ZeroDivisionError("Không thể chia cho phân số bằng 0")
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)


if __name__ == "__main__":
    a, b = Fraction(2, 3), Fraction(4, 5)
    print(a, b, a + b, a - b, a * b, a / b, sep="\n")
