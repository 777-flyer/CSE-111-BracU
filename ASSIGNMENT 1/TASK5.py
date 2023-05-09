user = input("Dear Student, Please provide your new password: ")

upper_detector = False
lower_detector = False
digit_detector = False
special_detector = False
list_of_special_characters = ['_', '$', '#', '@']

for checker in user:

    if checker.isupper():
        upper_detector = True
    elif checker.islower():
        lower_detector = True
    elif checker.isdigit():
        digit_detector = True
    elif checker in list_of_special_characters:
        special_detector = True

wrong_outs = []

if not upper_detector:
    wrong_outs.append("Uppercase Missing")
if not lower_detector:
    wrong_outs.append("Lowercase Missing")
if not digit_detector:
    wrong_outs.append("Digit Missing")
if not special_detector:
    wrong_outs.append("Special Character Missing")

if len(wrong_outs) == 0:

    print("OK")

else:

    for outs in wrong_outs:
        print(outs)

# ---------------------------------------------


# # symbol --> decimal
# # 0-9    --> 48-57
# # A-Z    --> 65-90
# # a-z    --> 97-122


# # ohMyBR@CU      -->  Digit missing
# # ohmybracu      -->  Uppercase character missing, Digit missing, Special character missing
# # OhMyBR@CU20    -->  OK

# p = input("enter password: ")

# f1 = flag_lower = 0
# f2 = flag_upper = 0
# f3 = flag_digit = 0 
# f4 = flag_special = 0

# for i in p:
#     if 97 <= ord(i) <= 122:
#         f1 += 1
#     elif 65 <= ord(i) <= 90:
#         f2 += 1
#     elif 48 <= ord(i) <= 57:
#         f3 += 1
#     else:
#         f4 += 1

# problem=[]
# if(f1==0):
#   problem.append("Lower missing")
# if(f2==0):
#   problem.append("Upper missing")
# if(f3==0):
#   problem.append("Digit missing")
# if(f4==0):
#   problem.append("Special missing")

# # print(problem)
# for i in range(len(problem)):
#   if(i==len(problem)-1):
#      print(problem[i])
#   else:
#      print(problem[i],end=", ")

# if len(problem) == 0:
#   print("OK")