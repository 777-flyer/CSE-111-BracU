class RealNumber:

    def __init__(self, r=0):

        self.__realValue = r

    def getRealValue(self):

        return self.__realValue

    def setRealValue(self, r):

        self.__realValue = r

    def __str__(self):

        return 'RealPart: ' + str(self.getRealValue())


class ComplexNumber(RealNumber):

    def __init__(self, RealPart=1, ImaginaryPart=1):

        super().__init__(1.0 * RealPart)
        self.__imaginary_part = float(ImaginaryPart)

    def __str__(self):

        summary = ''
        summary += f'{super().__str__()}'
        summary += f'\nImaginary Part: {self.__imaginary_part}'

        return summary


cn1 = ComplexNumber()
print(cn1)
print('---------')
cn2 = ComplexNumber(5, 7)
print(cn2)
