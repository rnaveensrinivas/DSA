from typing import Union

class Fraction:
    def __init__(self, numerator: int, denominator: int):
        """Initialize a Fraction object."""
        assert isinstance(numerator, int), "'numerator' must be an integer"
        assert isinstance(denominator, int), "'denominator' must be an integer"
        assert denominator != 0, "'denominator' cannot be zero"

        # Normalize signs
        if denominator < 0:
            numerator, denominator = -numerator, -denominator

        gcd = self._gcd(abs(numerator), abs(denominator))
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

    def __str__(self) -> str:
        return f"{self.numerator}/{self.denominator}" if self.numerator != 0 else "0"
    
    def __repr__(self) -> str: 
        return f"{self.__class__.__name__}(numerator={self.numerator}, \
            denominator={self.denominator})"

    def __add__(self, other: 'Fraction') -> 'Fraction':
        self._validate_operand(other)
        new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
    
    def __radd__(self, other: 'Fraction') -> 'Fraction':
        return self + other
    
    def __iadd__(self, other: 'Fraction') -> 'Fraction': 
        # Fraction(1,2) += Fraction(1,4)
        added_fraction = self + other
        self.numerator = added_fraction.numerator
        self.denominator = added_fraction.denominator

    def __sub__(self, other: 'Fraction') -> 'Fraction':
        self._validate_operand(other)
        new_numerator = self.numerator * other.denominator - self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        self._validate_operand(other)
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other: 'Fraction') -> 'Fraction':
        self._validate_operand(other)
        assert other.numerator != 0, "Cannot divide by zero"
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other: 'Fraction') -> bool:
        self._validate_operand(other)
        return self.numerator * other.denominator == self.denominator * other.numerator

    def __lt__(self, other: 'Fraction') -> bool:
        self._validate_operand(other)
        return self.numerator * other.denominator < self.denominator * other.numerator

    def __le__(self, other: 'Fraction') -> bool:
        self._validate_operand(other)
        return self.numerator * other.denominator <= self.denominator * other.numerator

    def __gt__(self, other: 'Fraction') -> bool:
        self._validate_operand(other)
        return self.numerator * other.denominator > self.denominator * other.numerator

    def __ge__(self, other: 'Fraction') -> bool:
        self._validate_operand(other)
        return self.numerator * other.denominator >= self.denominator * other.numerator

    def __ne__(self, other: 'Fraction') -> bool:
        self._validate_operand(other)
        return self.numerator * other.denominator != self.denominator * other.numerator

    def get_numerator(self): 
        return self.numerator
    
    def get_denominator(self): 
        return self.denominator
    
    @staticmethod
    def _gcd(a: int, b: int) -> int:
        """Calculate the greatest common divisor (GCD) using Euclid's algorithm."""
        while b:
            a, b = b, a % b
        return a

    @staticmethod
    def _validate_operand(other: Union['Fraction', int]):
        if not isinstance(other, Fraction):
            raise TypeError("Operand must be an instance of Fraction")
    
assert(Fraction(1,2) / Fraction(1,2)) == Fraction(1,1), "Logical error in __truediv__()"
assert(Fraction(1,-2) / Fraction(1,2)) == Fraction(-1,1), "Logical error in __truediv__()"
assert(Fraction(1,-2) - Fraction(1,2)) == Fraction(-1,1), "Logical error in __sub__()"
assert(Fraction(1,-2) + Fraction(1,2)) == Fraction(0,1), "Logical error in __add__()"
assert(Fraction(1,-2) < Fraction(1,2)) == True, "Logical error in __lt__()"
assert(Fraction(1,-2) <= Fraction(1,2)) == True, "Logical error in __le__()"
assert(Fraction(1,-2) > Fraction(1,2)) == False, "Logical error in __gt__()"
assert(Fraction(1,-2) >= Fraction(1,2)) == False, "Logical error in __ge__"
assert(Fraction(1,-4) < Fraction(1,-2)) == False, "Logical error in __lt__()"
assert(Fraction(1,-4) <= Fraction(1,-2)) == False, "Logical error in __le__()"
assert(Fraction(1,-4) > Fraction(1,-2)) == True, "Logical error in __gt__()"
assert(Fraction(1,-4) >= Fraction(1,-2)) == True, "Logical error in __ge__()"

        
        
        
        
        
    