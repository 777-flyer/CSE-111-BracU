class RealNumber:

    def __init__(self, number=0):
        self.number = number

    def __add__(self, anotherRealNumber):
        return self.number + anotherRealNumber.number

    def __sub__(self, anotherRealNumber):
        return self.number - anotherRealNumber.number

    def __str__(self):
        return str(self.number)


class ComplexNumber(RealNumber):

    def __init__(self, real_part, imaginary_part=0):

        self.imaginary_part = imaginary_part

        if type(real_part) != int:

            super().__init__(real_part.number)

        else:

            super().__init__(real_part)

    def __add__(self, anotherComplexNumber):

        return str(super().__add__(anotherComplexNumber)) + ' + ' + str(
            self.imaginary_part + anotherComplexNumber.imaginary_part) + 'i'

    def __sub__(self, anotherComplexNumber):

        return str(super().__sub__(anotherComplexNumber)) + ' - ' + str(
            anotherComplexNumber.imaginary_part - self.imaginary_part) + 'i'

    def __str__(self):

        return str(self.number) + ' + ' + str(self.imaginary_part) + 'i'


r1 = RealNumber(3)
r2 = RealNumber(5)
print(r1 + r2)
cn1 = ComplexNumber(2, 1)
print(cn1)
cn2 = ComplexNumber(r1, 5)
print(cn2)
cn3 = cn1 + cn2
print(cn3)
cn4 = cn1 - cn2
print(cn4)
