keyboard = {
    "1": [".", ",", "?", "!", ":"],
    "2": ["A", "B", "C"],
    "3": ["D", "E", "F"],
    "4": ["G", "H", "I"],
    "5": ["J", "K", "L"],
    "6": ["M", "N", "O"],
    "7": ["P", "Q", "R", "S"],
    "8": ["T", "U", "V"],
    "9": ["W", "X", "Y", "Z"],
    "0": [" "],
}

user = input("Sir,Please enter your desired input: ").upper()
key_count = []
final_output = ""

for i in user:
    for key,values in keyboard.items():
        if i in values:
            index = 0
            for x in range(len(values)):
                if i == values[x]:
                    index = x + 1
            for k in range(index):
                final_output += key

print(final_output)


'''

---another way to do the final part---


n = input("input: ").upper()
temp = []
p = output = ""

for i in n:
    for j,k in kp.items():
        if i in k:
            indx = k.index(i)
            p += j*(indx + 1)

print(p)

'''