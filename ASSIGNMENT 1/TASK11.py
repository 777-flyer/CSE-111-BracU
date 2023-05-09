dict_of_numbers = dcn = {}
list_of_numbers = lon = []

while True:

    user = input("Enter your numbers or STOP to end giving inputs: ")

    if user == "STOP":
        break
    else:
        lon.append(int(user))

for key in lon:

    if key in dcn:

        dcn[key] += 1
    else:

        dcn[key] = 1

for i in dcn:
    print(f"{i} : {dcn[i]} TIMES")

# another way to solve this--------------------------


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
