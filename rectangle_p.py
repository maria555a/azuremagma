import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.get_square() == other.get_square()
        return NotImplemented

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        r_area = self.get_square() + other.get_square()
        width = round(math.sqrt(r_area))
        height = r_area / width
        return Rectangle(width, height)

    def __mul__(self, n):
        if not isinstance(n, (int, float)):
            return NotImplemented
        new_area = self.get_square() * n
        width = round(math.sqrt(new_area))
        height = new_area / width
        return Rectangle(width, height)

    def __str__(self):
        return f'Rectangle({self.width}, {self.height})'

if __name__ == "__main__":
    r1 = Rectangle(2, 4)
    r2 = Rectangle(3, 6)
    print(f"r1: {r1}, area: {r1.get_square()}")
    print(f"r2: {r2}, area: {r2.get_square()}")

    assert r1.get_square() == 8, 'Test1'
    assert r2.get_square() == 18, 'Test2'

    r3 = r1 + r2
    print(f"r3 (r1 + r2): {r3}, area: {r3.get_square()}")
    assert r3.get_square() == 26, 'Test3'

    r4 = r1 * 4
    print(f"r4 (r1 * 4): {r4}, area: {r4.get_square()}")
    assert r4.get_square() == 32, 'Test4'

    assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'

