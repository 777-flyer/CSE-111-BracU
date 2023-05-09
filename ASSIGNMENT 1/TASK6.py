# we need to solve this using list only as it comes from list's problem set.
# you can solve it using dictionary as well, I've provided the solution below.
# so, here's the solution.


num_list = []

while True:
    user = input("Sir,Please enter a number or STOP to break: ")

    if user == "STOP":
        break
    else:
        num_list.append(int(user))

processed_numbers = []

for i in range(len(num_list)):
    if num_list[i] in processed_numbers:
        continue
    else:
        counter = 1
        for j in range(i + 1, len(num_list)):
            if num_list[i] == num_list[j]:
                counter += 1

        processed_numbers.append(num_list[i])
        print(f'{num_list[i]} appeared {counter} time(s)')

# we can solve it using dictionary as well. You will find two more ways to solve below.

# dict_of_numbers = dcn = {}
# list_of_numbers = lon = []

# while True:

#     user = input("Enter your numbers or STOP to end giving inputs: ")

#     if user == "STOP":
#         break
#     else:
#         lon.append(int(user))

# for key in lon:

#     if key in dcn:

#         dcn[key] += 1
#     else:

#         dcn[key] = 1

# for i in dcn:

#     print(f"{i} : {dcn[i]} TIMES")


# #another way to solve this--------------------------


# num_frequency = freq = {}

# while True:

#     inputs = input("Enter your numbers or STOP to end giving inputs: ")

#     if inputs == "STOP":
#         break
#     elif inputs.isnumeric():
#         if inputs in freq:  #dictionary
#             freq[inputs] += 1
#         else:
#             freq[inputs] = 1


# for number, frequency in freq.items():

#     print(f"{number} : {frequency} Times")



# ---------------------------------------

# a = list_num = []

# while True:
#     n = input("enter a number (input 'STOP' to break): ")

#     if n == 'STOP':
#         break
#     else:
#         a.append(int(n))

# b = final_list = []

# for i in range(len(a)):
#     if a[i] in b:
#         continue
#     else:
#         c = 1 #counter
#         for j in range(i+1,len(a)):
#             if a[i] == a[j]:
#                 c += 1
#         b.append(a[i])
#         print(f'{a[i]} - {c} times')