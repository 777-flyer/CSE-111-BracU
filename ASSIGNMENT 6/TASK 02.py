class Assassin:

    number_of_assassin = 0

    def __init__(self, name, success_rate):

        self.name = name
        self.success_rate = success_rate
        Assassin.number_of_assassin += 1

    def printDetails(self):

        print(f'Name: {self.name}')
        print(f'Success Rate: {self.success_rate}%')
        print(f'Total number of Assassin: {Assassin.number_of_assassin}')

    @classmethod
    def failureRate(cls, name, failure_rate):

        success_rate = 100 - failure_rate
        return cls(name, success_rate)

    @classmethod
    def failurePercentage(cls, name, failure_percentage):

        success_rate = 100 - int(failure_percentage.strip('%'))
        return cls(name, success_rate)


john_wick = Assassin('John Wick', 100)
john_wick.printDetails()
print('================================')
nagisa = Assassin.failureRate("Nagisa", 20)
nagisa.printDetails()
print('================================')
akabane = Assassin.failurePercentage("Akabane", "10%")
akabane.printDetails()
