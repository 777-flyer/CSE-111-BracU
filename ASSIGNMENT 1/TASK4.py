given_string = gs = "harry, hermione"

'''
this code will work for given inputs like this only
as we are getting one comma and a space
after the first word. 
'''

string_one = ""
string_two = ""
length = len(given_string)
detector = 0

for div in range(length):

    if gs[div] != ",":
        string_one += gs[div]
    else:
        detector = div
        break

for adder in range(detector + 2, length, 1):
    string_two += gs[adder]

new_string = ""

for i in gs:

    if i in string_one and i in string_two:
        new_string += i

if new_string == "":

    print("Nothing in common")

else:

    print(f"Common characters are '{new_string}'")


'''
-------------------------------------------

# Sample Input       -->  Sample Output
# harry, hermione    -->  hrrhr
# dean, tom          -->  Nothing in common.

s1 = "harry"
s2 = "hermione" 

# s1 = "dean"
# s2 = "tom" 

fs = final_string = ""

for i in s1:
    if i in s2:
        fs += i

for i in s2:
    if i in s1:
        fs += i

if len(fs) == 0:
    print("Nothing in common.")
else:
    print(fs)
'''