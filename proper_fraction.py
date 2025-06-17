import math

class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Value can not be zero")
        self.a = a
        self.b = b
        self._reduce()

    def _reduce(self):
        gcd = math.gcd(self.a, self.b)
        self.a //= gcd
        self.b //= gcd
        if self.b < 0:
            self.a = -self.a
            self.b = -self.b

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return Fraction(self.a * other.a, self.b * other.b)

    def __add__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        new_a = self.a * other.b + other.a * self.b
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        new_a = self.a * other.b - other.a * self.b
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.a == other.a and self.b == other.b

    def __lt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.a * other.b < other.a * self.b

    def __gt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.a * other.b > other.a * self.b

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"

if __name__ == "__main__":
    f_a = Fraction(2, 3)
    f_b = Fraction(3, 6)
    f_c = f_b + f_a
    print(f_c)
    f_d = f_b * f_a
    print(f_d)
    f_e = f_a - f_b
    print(f_e)

    assert str(f_c) == 'Fraction: 7, 6'
    assert str(f_d) == 'Fraction: 1, 3'
    assert str(f_e) == 'Fraction: 1, 6'

    assert f_d < f_c
    assert f_d > f_e
    assert f_a != f_b

    f_1 = Fraction(2, 4)
    f_2 = Fraction(3, 6)
    assert f_1 == f_2

    print('OK')
