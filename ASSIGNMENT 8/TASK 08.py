class Team:

    def __init__(self, name):

        self.name = "default"
        self.total_player = 5

    def info(self):

        print("We love sports")


class FootBallTeam(Team):

    def __init__(self, name):

        super().__init__(name)
        self.name = name
        self.total_player = 11

    def info(self):

        print(f"Our name is {self.name}")
        print("We play Football")
        super().info()


class CricketTeam(Team):

    def __init__(self, name):

        super().__init__(name)
        self.name = name
        self.total_player = 11

    def info(self):

        print(f"Our name is {self.name}")
        print("We play Cricket")
        super().info()


class Team_test:

    def check(self, team):

        print("=========================")
        print("Total Player:", team.total_player)
        team.info()


f = FootBallTeam("Brazil")
c = CricketTeam("Bangladesh")
test = Team_test()
test.check(f)
test.check(c)
