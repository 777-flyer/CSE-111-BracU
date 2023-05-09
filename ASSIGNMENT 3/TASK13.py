# Write your code here.

class Programmer:
    
    def __init__(self, name, language, experience):
        print("Horray! A new programmer is born")
        self.name = name
        self.language = language
        self.experience = experience
        
    def addExp(self, new_xp):
        self.experience += new_xp
        print(f'Updating experience of {self.name}')
        
    def printDetails(self):
        print(f'Name: {self.name}')
        print(f'Language: {self.language}')
        print(f'Experience: {self.experience}')

p1 = Programmer("Ethen Hunt", "Java", 10)
p1.printDetails()
print('--------------------------')
p2 = Programmer("James Bond", "C++", 7)
p2.printDetails()
print('--------------------------')
p3 = Programmer("Jon Snow", "Python", 4)
p3.printDetails()
p3.addExp(5)
p3.printDetails()    

