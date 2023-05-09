#Write your class code here

class Joker:
    
    def __init__(self,name,power,is_he_psycho):
        self.name = name
        self.power = power
        self.is_he_psycho = is_he_psycho
        
#driver code
j1 = Joker('Heath Ledger', 'Mind Game', False)
print(j1.name)
print(j1.power)
print(j1.is_he_psycho)
print("=====================")
j2 = Joker('Joaquin Phoenix', 'Laughing out Loud', True)
print(j2.name)
print(j2.power)
print(j2.is_he_psycho)
print("=====================")
if j1 == j2:
    print('same')
else: 
    print('different')
j2.name = 'Heath Ledger'
if j1.name == j2.name:
    print('same')
else:
    print('different')


#Write your code for 2,3 here
print("\n")
print("The first if/else block prints the output as ‘different’ \nBecause it is checking wif j1 == j2 or not,\nAnd when we compare two variables, we compare their memory locations actually,\nHere, their memory location isn't same.\nSo,it's showing different.")
print("\n")
print("The second if/else block prints the output as ‘same’ \nBecause it is checking if they share same names or not,\nBoth j1 and j2 shares the same name here.\nSo,it's showing same as output. ")