given_input = {'key1': 'value1', 'key2': 'value2', 'key3': 'value1'}
final_dict = {}

for k, v in given_input.items():
    if v not in final_dict:
        final_dict[v] = [k]
    else:
        final_dict[v].append(k)
print(final_dict)

# if we want to take user inputs

# user = input("Sir,Please enter the dictionary here: ").split(",")
# main_dict = {}

# for i in user:
#     temp = i.split(":")
#     main_dict[(temp[0])] = temp[1]

# final_dict = {}

# for key, value in main_dict.items():
#     if value not in final_dict:
#         final_dict[value] = [key]
#     else:
#         final_dict[value].append(key)

# print(final_dict)
