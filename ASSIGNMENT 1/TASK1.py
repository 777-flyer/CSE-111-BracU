given_string = "ApplE"

upper_ctr = 0
lower_ctr = 0
new_string = ""

for char in given_string:

    if ord("A") <= ord(char) <= ord("Z"):
        upper_ctr += 1
    elif ord("a") <= ord(char) <= ord("z"):
        lower_ctr += 1
        
for characters in given_string:

    # if upper_ctr > lower_ctr:
    #     new_string += characters.upper()
    # elif lower_ctr >= upper_ctr:
    #     new_string += characters.lower()

    # if you don't want to use built-in function-----

    if upper_ctr > lower_ctr:
        if ord("A") <= ord(characters) <= ord("Z"):
            new_string += characters
        elif ord("a") <= ord(characters) <= ord("z"):
            new_string += chr(ord(characters) - 32)
    elif lower_ctr >= upper_ctr:
        if ord("A") <= ord(characters) <= ord("Z"):
            new_string += chr(ord(characters) + 32)
        elif ord("a") <= ord(characters) <= ord("z"):
            new_string += characters


print(new_string)



'''
----------------another way to solve----------------

input --> (A-Z, a-z)

symbol --> decimal
0-9    --> 48-57
A-Z    --> 65-90
a-z    --> 97-122

HOusE  --> HOUSE
ApplE  --> apple
BaNaNa --> banana

s = string_input = "ApplE"
t1 = flag_upper = 0
t2 = flag_lower = 0

for i in s:
    if 65 <= ord(i) <= 90:
        t1 += 1
    if 97 <= ord(i) <= 122:
        t2 += 1

if t1 > t2:
    print(s.upper())
    
if t1 <= t2:
    print(s.lower())

'''
