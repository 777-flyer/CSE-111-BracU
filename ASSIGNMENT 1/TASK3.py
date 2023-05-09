# user = up = input("Sir, Please enter a string: ")
given_string = gs = "baNgladEsh"

first_upper = -1
last_upper = -1
length_of_gs = len(gs)

for i in range(length_of_gs):

    if ord("A") <= ord(gs[i]) <= ord("Z"):

        if first_upper == -1:
            first_upper = i

        last_upper = i

if first_upper != -1 and last_upper != -1 and last_upper > first_upper + 1:

    substring = gs[first_upper + 1:last_upper]
    print(substring)  # or you can use a for loop here to add the characters in that substring.

else:
    print("BLANK")


'''
------------------------------------

task3 - no slicing

Sample Input --> Sample Output
baNgladEsh   --> glad
coDIng       --> BLANK

s = given_string = "baNgladEsh"

start = 0   starting index of final string 
end = 0     ending  index of final string 

for i in range(len(s)):
    if 65 <= ord(s[i]) <= 90:
        start = i
        break
for i in range(len(s)):
    if 65 <= ord(s[i]) <= 90 and i != start:
        end = i
        break
fs = final_string = ""
for i in range(start+1,end):
    fs += s[i]

if len(fs) == 0:
    print("BLANK")
else:
    print(fs)
'''