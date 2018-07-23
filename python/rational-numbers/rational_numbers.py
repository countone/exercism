from __future__ import division
import math

class Rational(object):
    def __init__(self, numer, denom):
        
        if denom!=0:
            if denom<0:
                self.numer = -numer/math.gcd(abs(numer),abs(denom))
                self.denom = -denom/math.gcd(abs(numer),abs(denom))
            else:
                self.numer = numer/math.gcd(abs(numer),abs(denom))
                self.denom = denom/math.gcd(abs(numer),abs(denom))
        else:
            raise ValueError('ValueError')

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return Rational(int(self.numer*other.denom + self.denom*other.numer),int(self.denom *other.denom))

    def __sub__(self, other):
        return Rational(int(self.numer*other.denom - self.denom*other.numer),int(self.denom *other.denom))

    def __mul__(self, other):
        return Rational(int(self.numer*other.numer),int(self.denom *other.denom))

    def __truediv__(self, other):
        return Rational(int(self.numer*other.denom),int(other.numer*self.denom) )
        
    def __abs__(self):
        return Rational( int(abs(self.numer)),int(abs(self.denom)))

    def __pow__(self, power):
        if type(power) is int:
            if power>=0:
                return Rational (int(self.numer**power),int(self.denom**power))
            else:
                return Rational(int(self.denom**abs(power)),int(self.numer**abs(power)))
        else:
             return Rational(int(self.numer**power),int(self.denom**power))

    def __rpow__(self, base):
        return (base**self.numer)**(1/self.denom)

