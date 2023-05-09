class SportsPerson:

    def __init__(self, team_name, name, role):

        self.__team = team_name
        self.__name = name
        self.role = role
        self.earning_per_match = 0

    def get_name_team(self):

        return 'Name: ' + self.__name+', Team Name: ' + self.__team


class Player(SportsPerson):

    def __init__(self, team_name, name, role, total_goal, total_match):

        super().__init__(team_name, name, role)
        self.total_goal = total_goal
        self.total_match = total_match
        self.goal_ratio = 0
        self.match_earning = 0

    def calculate_ratio(self):

        self.goal_ratio = self.total_goal / self.total_match

    def calculate_earning(self):

        self.match_earning = (self.total_goal * 1000) + (self.total_match * 10)

    def print_details(self):

        self.calculate_earning()
        print(self.get_name_team())
        print('Team Role:', self.role)
        print('Total Goal:', self.total_goal,', Total Played:', self.total_match)
        print('Goal Ratio:', self.goal_ratio)
        print('Match Earning:', str(self.match_earning)+'K')


class Manager(SportsPerson):

    def __init__(self, team_name, name, role, match_win):

        super().__init__(team_name, name, role)
        self.match_win = match_win
        self.match_earning = 0

    def calculate_earning(self):

        self.match_earning = self.match_win * 1000

    def print_details(self):

        self.calculate_earning()
        print(self.get_name_team())
        print('Team Role:', self.role)
        print('Total Win:', self.match_win)
        print('Match Earning:', str(self.match_earning)+'K')


player_one = Player('Juventus', 'Ronaldo', 'Striker', 25, 32)
player_one.calculate_ratio()
player_one.print_details()
print('------------------------------------------')
manager_one = Manager('Real Madrid', 'Zidane', 'Manager', 25)
manager_one.print_details()
