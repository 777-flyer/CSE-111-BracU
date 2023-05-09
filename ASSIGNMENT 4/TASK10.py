class EPL_Team:

    def __init__(self, club_name, theme_song="No Slogan"):

        self.club_name = club_name
        self.theme_song = theme_song
        self.titles = 0

    def showClubInfo(self):

        summary = ""
        summary += f"Name: {self.club_name}\n"
        summary += f"song: {self.theme_song}\n"
        summary += f"Total No of title: {self.titles}"
        return summary

    def increaseTitle(self):

        self.titles += 1

    def changeSong(self, new_song):

        self.theme_song = new_song


manu = EPL_Team('Manchester United', 'Glory Glory Man United')
chelsea = EPL_Team('Chelsea')
print('===================')
print(manu.showClubInfo())
print('##################')
manu.increaseTitle()
print(manu.showClubInfo())
print('===================')
print(chelsea.showClubInfo())
chelsea.changeSong('Keep the blue flag flying high')
print(chelsea.showClubInfo())
