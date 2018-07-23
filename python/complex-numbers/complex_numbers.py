from math import sqrt,sin,cos,exp

class ComplexNumber(object):
    def __init__(self, real, imaginary):
        
        self.real=real
        self.imaginary=imaginary

    def __add__(self, other):
        return ComplexNumber((self.real+other.real),(self.imaginary+other.imaginary))

    def __mul__(self, other):
        return ComplexNumber((self.real*other.real-self.imaginary*other.imaginary),(self.imaginary*other.real+self.real*other.imaginary))

    def __eq__(self, other):
        return self.real== other.real and other.imaginary==self.imaginary

    def __sub__(self, other):
        r=self.real-other.real
        i=self.imaginary-other.imaginary
        return ComplexNumber(r,i)     

    def __truediv__(self, other):
        r=(self.real*other.real+other.imaginary*self.imaginary)/(other.real**2+other.imaginary**2)
        i=(self.imaginary*other.real - self.real*other.imaginary)/(other.real**2 + other.imaginary**2)
        return ComplexNumber(r,i)

    def __abs__(self):
        return sqrt(self.real**2 + self.imaginary**2)

    def conjugate(self):
        return ComplexNumber(self.real,-self.imaginary)

    def exp(self):
        return ComplexNumber(exp(self.real),0)* ComplexNumber(round(cos(self.imaginary),8),round(sin(self.imaginary),8))

