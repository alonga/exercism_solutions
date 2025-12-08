from math import gcd, pow


class Rational:
    def __init__(self, numer, denom):
        if denom == 0:
            raise ZeroDivisionError("Denominator cannot be zero")

        g = gcd(numer, denom)
        numer //= g
        denom //= g

        # Standard form: denom > 0
        if denom < 0:
            numer *= -1
            denom *= -1

        self.numer = numer
        self.denom = denom

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f"{self.numer}/{self.denom}"

    # ----------------------------
    # Arithmetic operations
    # ----------------------------

    def __add__(self, other):
        return Rational(
            self.numer * other.denom + other.numer * self.denom,
            self.denom * other.denom
        )

    def __sub__(self, other):
        return Rational(
            self.numer * other.denom - other.numer * self.denom,
            self.denom * other.denom
        )

    def __mul__(self, other):
        return Rational(
            self.numer * other.numer,
            self.denom * other.denom
        )

    def __truediv__(self, other):
        if other.numer == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return Rational(
            self.numer * other.denom,
            self.denom * other.numer
        )

    # ----------------------------
    # Special math operations
    # ----------------------------

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        if isinstance(power, int):
            if power >= 0:
                return Rational(self.numer ** power, self.denom ** power)
            else:
                p = abs(power)
                return Rational(self.denom ** p, self.numer ** p)
        else:
            # float exponent → produce real number
            return pow(self.numer / self.denom, power)

    def __rpow__(self, base):
        # base^(a/b)
        return pow(base, self.numer / self.denom)
