# task07

class PokemonBasic:

    def __init__(self, name='Default', hp=0, weakness='None', type_='Unknown'):
        self.name = name
        self.hit_point = hp
        self.weakness = weakness
        self.type = type_

    def get_type(self):
        return 'Main type: ' + self.type

    def get_move(self):
        return 'Basic move: ' + 'Quick Attack'

    def __str__(self):
        return "Name: " + self.name + ", HP: " + str(self.hit_point) + ", Weakness: " + self.weakness


class PokemonExtra(PokemonBasic):

    def __init__(self, *info):

        self.secondary = ""
        self.other_moves = []

        if len(info) == 4:

            super().__init__(info[0], info[1], info[2], info[3])

        else:

            super().__init__(info[0], info[1], info[2], info[3])
            self.secondary = info[4]
            self.other_moves = self.other_moves + list(info[5])

    def get_type(self):

        if self.secondary == "":

            return f"{super().get_type()}"

        else:

            return f"{super().get_type()}, Secondary type: {self.secondary}"

    def get_move(self):

        if len(self.other_moves) == 0:

            return f"{super().get_move()}"

        else:

            return f"{super().get_move()}\nOther move: {', '.join(self.other_moves)}"


print('\n------------Basic Info:--------------')
pk = PokemonBasic()
print(pk)
print(pk.get_type())
print(pk.get_move())
print('\n------------Pokemon 1 Info:-------------')
charmander = PokemonExtra('Charmander', 39, 'Water', 'Fire')
print(charmander)
print(charmander.get_type())
print(charmander.get_move())
print('\n------------Pokemon 2 Info:-------------')
charizard = PokemonExtra('Charizard', 78, 'Water', 'Fire', 'Flying', ('Fire Spin', 'Fire Blaze'))
print(charizard)
print(charizard.get_type())
print(charizard.get_move())