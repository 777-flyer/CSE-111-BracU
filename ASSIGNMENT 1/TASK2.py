given_string = "213213"

is_word = True
is_number = True

for i in given_string:
    
    if (ord(i) < 97 or ord(i) > 122) and (ord(i) < 65 or ord(i) > 90):
        
        is_word = False
        
    if ord(i) < 48 or ord(i) > 62:
        
        is_number = False
        
if is_word:
    print("WORD")

elif is_number:
    print("NUMBER")

else:
    print("MIXED")


'''
-----------------another way-------------------

# symbol --> decimal
# 0-9    --> 48-57
# A-Z    --> 65-90
# a-z    --> 97-122

# Sample Input ---> Sample Output
# 213213       ---> NUMBER
# jhg231j213   ---> MIXED
# Hello        ---> WORD

s = string_input = "213213"
t1 = flag_number = 0
t2 = flag_word = 0
# t3 = flag_mixed = 0

for i in s:
    if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
        t2 += 1
    if 48 <= ord(i) <= 57:
        t1 += 1

# if t2>1 and t1>1:
#     t3 = 1

if t1 > 0 and t2 > 0:
    print("MIXED")
elif t1 > 0 and t2 == 0:
    print("NUMBER")
elif t2 > 0 and t1 == 0:
    print("WORD")

'''