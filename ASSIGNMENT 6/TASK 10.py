class SultansDine:

    total_branches = 0
    total_sell = 0
    branches = []

    @classmethod
    def details(cls):

        print(f'Total Number of branch(s): {cls.total_branches}')
        print(f'Total Sell: {cls.total_sell} Taka')

    def __init__(self, name):

        self.name = name
        self.sell = 0
        SultansDine.total_branches += 1
        SultansDine.branches.append(self)

    def sellQuantity(self, quantity):

        if quantity < 10:

            self.sell = quantity * 300

        elif quantity < 20:

            self.sell = quantity * 350

        else:

            self.sell = quantity * 400

        SultansDine.total_sell += self.sell

    def branchInformation(self):

        print(f'Branch Name: {self.name}')
        print(f'Branch Sell: {self.sell} Taka')
        print('-----------------------------------------')
        print(f'Total Number of branch(s): {SultansDine.total_branches}')
        print(f'Total Sell: {SultansDine.total_sell} Taka')

        branch_info = ''

        for branch in SultansDine.branches:
            branch_sell_percentage = round((branch.sell / SultansDine.total_sell) * 100, 2)
            branch_info += f'Branch Name: {branch.name}, Branch Sell: {branch.sell} Taka \n'
            branch_info += f'Branch consists of total sell\'s: {branch_sell_percentage}% \n'

        print(branch_info)


SultansDine.details()
print('########################')
dhanmodi = SultansDine('Dhanmondi')
dhanmodi.sellQuantity(25)
dhanmodi.branchInformation()
print('-----------------------------------------')
SultansDine.details()

print('========================')

baily_road = SultansDine('Baily Road')
baily_road.sellQuantity(15)
baily_road.branchInformation()
print('-----------------------------------------')
SultansDine.details()

print('========================')

gulshan = SultansDine('Gulshan')
gulshan.sellQuantity(9)
gulshan.branchInformation()
print('-----------------------------------------')
SultansDine.details()
