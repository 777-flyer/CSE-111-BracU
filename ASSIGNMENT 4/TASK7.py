class Match:

    def __init__(self, team_names):
        team_names = team_names.split("-")
        self.batting_team = team_names[0]
        self.bowling_team = team_names[1]
        self.runs = 0
        self.overs = 0
        self.wickets = 0

        welcoming_message = ""

        for i in range(5, 0, -1):
            welcoming_message += str(i) + ".."
        welcoming_message += "Play!!!"

        print(welcoming_message)

    def add_run(self, runs):

        self.runs += runs

    def add_over(self, overs):

        if self.overs + overs > 5:
            print(f'Warning! Cannot add {overs} over/s (5 over match)')
        else:
            self.overs += overs

    def add_wicket(self, wickets):

        if self.wickets + wickets > 5:
            print(f'Warning! Cannot add {wickets} wicket/s (10 wickets can be taken)')
        else:
            self.wickets += wickets

    def print_scoreboard(self):

        scoreboard = ""
        scoreboard += "Batting Team: {}\n".format(self.batting_team)
        scoreboard += "Bowling Team: {}\n".format(self.bowling_team)
        scoreboard += "Total Runs: {} Wickets: {} Overs: {}".format(self.runs, self.wickets, self.overs)

        return scoreboard


match1 = Match("Rangpur Riders-Cumilla Victorians")
print("=========================")
match1.add_run(4)
match1.add_run(6)
match1.add_over(1)
print(match1.print_scoreboard())
print("=========================")
match1.add_over(5)
print("=========================")
match1.add_wicket(1)
print(match1.print_scoreboard())
