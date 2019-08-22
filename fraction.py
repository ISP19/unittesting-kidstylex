import math
class Fraction:
    """A fraction with a numerator and denominator and arithmetic operations.

    Fractions are always stored in proper form, without common factors in 
    numerator and denominator, and denominator >= 0.
    Since Fractions are stored in proper form, each value has a
    unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
    internal representation.
    """
    
    def __init__(self, numerator, denominator=1):
        """Initialize a new fraction with the given numerator
           and denominator (default 1).
        """

        self.gcd = math.gcd(numerator, denominator)
        self.numerator = int(numerator / self.gcd)
        self.denominator = int(denominator / self.gcd)

        if not isinstance(numerator, int):
            raise TypeError("Numerator must be int.")

        if not isinstance(denominator, int):
            raise TypeError("Denominator must be int.")

        if denominator == 0:
            if self.numerator > 0:
                self.numerator = 1
                self.denominator = 0
            self.numerator = -1
            self.denominator = 0
        elif denominator < 0:
            self.numerator *= -1
            self.denominator *= -1


    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        new_num = (self.numerator*frac.denominator) + (self.denominator*frac.numerator)
        new_deno = self.denominator*frac.denominator
        return Fraction(new_num, new_deno)

    def __mul__(self, frac):
        return Fraction(self.numerator*frac.numerator, self.denominator*frac.denominator)

    def __str__(self):
        if self.denominator == 1:
            return "{}".format(self.numerator)
        return "{}/{}".format(self.numerator, self.denominator)

    def __sub__(self, frac):
        """From formula a/b - c/d = (ad-bc)/(b*d)
        """
        new_num = (self.numerator * frac.denominator) - (self.denominator * frac.numerator)
        new_deno = self.denominator * frac.denominator
        return Fraction(new_num, new_deno)

    # def __gt__(self, frac):
    #
    # def __neg__(self):

    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """
        return self.numerator == frac.numerator and self.denominator == frac.denominator
