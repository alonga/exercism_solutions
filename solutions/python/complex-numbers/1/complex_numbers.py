import math

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def _coerce(self, other):
        if isinstance(other, ComplexNumber):
            return other
        if isinstance(other, (int, float)):
            return ComplexNumber(other, 0)
        return NotImplemented

    def __eq__(self, other):
        if not isinstance(other, ComplexNumber):
            return False
        return (math.isclose(self.real, other.real) and
                math.isclose(self.imaginary, other.imaginary))

    def __add__(self, other):
        other = self._coerce(other)
        if other is NotImplemented:
            return NotImplemented
        return ComplexNumber(self.real + other.real,
                             self.imaginary + other.imaginary)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        other = self._coerce(other)
        if other is NotImplemented:
            return NotImplemented
        return ComplexNumber(self.real - other.real,
                             self.imaginary - other.imaginary)

    def __rsub__(self, other):
        other = self._coerce(other)
        return ComplexNumber(other.real - self.real,
                             other.imaginary - self.imaginary)

    def __mul__(self, other):
        other = self._coerce(other)
        if other is NotImplemented:
            return NotImplemented
        a, b = self.real, self.imaginary
        c, d = other.real, other.imaginary
        return ComplexNumber(a * c - b * d,
                             b * c + a * d)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        other = self._coerce(other)
        if other is NotImplemented:
            return NotImplemented
        a, b = self.real, self.imaginary
        c, d = other.real, other.imaginary
        denominator = c * c + d * d
        return ComplexNumber((a * c + b * d) / denominator,
                             (b * c - a * d) / denominator)

    def __rtruediv__(self, other):
        other = self._coerce(other)
        return other.__truediv__(self)

    def __abs__(self):
        return math.sqrt(self.real * self.real + self.imaginary * self.imaginary)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        a, b = self.real, self.imaginary
        factor = math.exp(a)
        return ComplexNumber(factor * math.cos(b),
                             factor * math.sin(b))

    def __repr__(self):
        return f"ComplexNumber({self.real}, {self.imaginary})"
