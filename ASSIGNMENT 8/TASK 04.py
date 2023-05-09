class Fruit:

    def __init__(self, formalin=False, name=''):
        self.__formalin = formalin
        self.name = name

    def getName(self):
        return self.name

    def hasFormalin(self):
        return self.__formalin


class testFruit:

    def test(self, fruit):

        print('----Printing Detail----')

        if fruit.hasFormalin():

            print('Do not eat the', fruit.getName(), '.')
            print(fruit)

        else:

            print('Eat the', fruit.getName(), '.')
            print(fruit)


class Mango(Fruit):

    def __init__(self, formalin=True, name="Mango"):

        super().__init__(formalin, name)

    def __str__(self):

        if self.hasFormalin():

            return f"{self.getName()}es are bad for you"

        else:

            return f"{self.getName()}es are good for you"


class Jackfruit(Fruit):

    def __init__(self, formalin=False, name="Jackfruit"):

        super().__init__(formalin, name)

    def __str__(self):

        if self.hasFormalin():

            return f"{self.getName()}s are bad for you"

        else:

            return f"{self.getName()}s are good for you"


m = Mango()
j = Jackfruit()
t1 = testFruit()
t1.test(m)
t1.test(j)
