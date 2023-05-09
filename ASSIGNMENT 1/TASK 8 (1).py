given_list_1 = [2, 3, 6]
given_list_2 = [3, 4, 5]
final_list = []

for i in given_list_1:
  for j in given_list_2:
    final_list.append(i * j)    

print(final_list)