class Batsman:

    def __init__(self, *data):

        length = len(data)

        if length == 2:
            self.name = "New Batsman"
            self.runs_scored = data[0]
            self.balls_faced = data[1]

        elif length == 3:
            self.name = data[0]
            self.runs_scored = data[1]
            self.balls_faced = data[2]

    def setName(self, new_name):

        self.name = new_name

    def printCareerStatistics(self):

        summary = ""
        summary += "Name: {}\n".format(self.name)
        summary += "Runs Scored: {} , Balls Faced: {}".format(self.runs_scored, self.balls_faced)
        print(summary)

    def battingStrikeRate(self):

        strike_rate = (self.runs_scored / self.balls_faced) * 100
        return strike_rate


b1 = Batsman(6101, 7380)
b1.printCareerStatistics()
print("============================")
b2 = Batsman("Liton Das", 678, 773)
b2.printCareerStatistics()
print("----------------------------")
print(b2.battingStrikeRate())
print("============================")
b1.setName("Shakib Al Hasan")
b1.printCareerStatistics()
print("----------------------------")
print(b1.battingStrikeRate())
