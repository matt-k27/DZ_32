class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Denominator cannot be zero")
        self.a = a
        self.b = b

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Unsupported operand type")
        return Fraction(self.a * other.a, self.b * other.b)

    def __add__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Unsupported operand type")
        return Fraction(self.a * other.b + other.a * self.b, self.b * other.b)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Unsupported operand type")
        return Fraction(self.a * other.b - other.a * self.b, self.b * other.b)

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return False
        return (self.a * other.b) / (self.b * other.b) == other.a * self.b / (self.b * other.b)

    def __gt__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Unsupported operand type")
        return (self.a * other.b) / (self.b * other.b) > other.a * self.b / (self.b * other.b)

    def __lt__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Unsupported operand type")
        return (self.a * other.b) / (self.b * other.b) < other.a * self.b / (self.b * other.b)

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"
