class Tournament:

    def __init__(self, name='Default'):

        self.__name = name

    def set_name(self, name):

        self.__name = name

    def get_name(self):

        return self.__name


class Cricket_Tournament(Tournament):

    def __init__(self, tournament='Default', number_of_teams=0, type_='No type'):

        super().__init__(tournament)
        self.__number_of_teams = number_of_teams
        self.__type = type_

    def detail(self):

        summary = ''

        summary += f'Cricket Tournament Name: {self.get_name()} \n'
        summary += f'Number of teams: {self.__number_of_teams}\n'
        summary += f'Type: {self.__type}'

        return summary


class Tennis_Tournament(Tournament):

    def __init__(self, tournament, number_of_players):

        super().__init__(tournament)
        self.__number_of_players = number_of_players

    def detail(self):

        summary = ''

        summary += f'Tennis Tournament Name: {self.get_name()}\n'
        summary += f'Number of Players: {self.__number_of_players}'

        return summary

ct1 = Cricket_Tournament()
print(ct1.detail())
print("-----------------------")
ct2 = Cricket_Tournament("IPL", 10, "t20")
print(ct2.detail())
print("-----------------------")
tt = Tennis_Tournament("Roland Garros", 128)
print(tt.detail())
