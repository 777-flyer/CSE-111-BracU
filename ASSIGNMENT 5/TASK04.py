class Team:

    def __init__(self, name=''):

        self.__team = name
        self.__player_list = []

    def setName(self, new_name):

        self.__team = new_name

    def addPlayer(self, location):

        player = location.player_name
        self.__player_list.append(player)

    def printDetail(self):

        print(f"Team: {self.__team}")
        print("List of Players:")
        print(f"{self.__player_list}")


class Player:

    def __init__(self, name):

        self.player_name = name


b = Team()
b.setName('Bangladesh')
mashrafi = Player("Mashrafi")
b.addPlayer(mashrafi)
tamim = Player("Tamim")
b.addPlayer(tamim)
b.printDetail()
a = Team("Australia")
ponting = Player("Ponting")
a.addPlayer(ponting)
lee = Player("Lee")
a.addPlayer(lee)
a.printDetail()
