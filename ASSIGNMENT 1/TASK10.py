'''task11  main_solution'''

user = {'a': 100, 'b': 100, 'c': 200, 'd': 300},{'a': 300, 'b': 200, 'd': 400, 'e': 200}

dict1 = user[0]

dict2 = user[1]

new_dict = {}

for i in dict1:  
    
    if i in dict2:  
        new_value = dict1[i] + dict2[i]  
        new_dict[i] = new_value 
    else:
        new_dict[i] = dict1[i]

for i in dict2:

    if i not in new_dict:
        new_dict[i] = dict2[i]


list_containing_values = l = []

for i in new_dict.values():

    if i not in l:
        l.append(i)

for i in range(len(l)):
  
  for j in range(i+1, len(l)):
    
    if l[i] > l[j]:

      temp = l[i]
      l[i] = l[j]
      l[j] = temp


print(new_dict)
print("values:",tuple(l))


'''
It has some user_input_problem, doesn't match with the question but it works like
I have mentioned before taking user inputs

'''

'''---------------another solution--------------'''


print(f'The way you have to give the input is : (a: 100,b: 200,c: 300) ')

user_1 = input("Sir,Please enter your first dictionary like the example given above: ").split(",")
first_dict = {}

for key in user_1:
    temp = key.split(":")
    first_dict[(temp[0])] = int(temp[1])

user_2 = input("Sir,Please enter your first dictionary like the example given above: ").split(",")
second_dict = {}

for key_2 in user_2:
    temp_1 = key_2.split(":")
    second_dict[(temp_1[0])] = int(temp_1[1])

final_dict = {}

for i in first_dict:
    final_dict[i] = first_dict[i]

for j in second_dict:
    if j in final_dict:
        final_dict[j] = final_dict[j] + second_dict[j]
    if j not in final_dict:
        final_dict[j] = second_dict[j]

final_list = []

for keys in final_dict:
    if final_dict[keys] not in final_list:
        final_list.append(final_dict[keys])

# final_list.sort() 
# we can sort the values like this but the better way is to do it by manual checking.
# let's do that now ''

for k in range(len(final_list)):
    for v in range(len(final_list)):
        if final_list[v] > final_list[k]:
            up = final_list[k]
            final_list[k] = final_list[v]
            final_list[v] = up

print("Your desired dictionary is: ", final_dict)
print("Values: ", tuple(final_list))


'''
---------------------another_solution--------------------
'''


'''

n1 = input("enter 1st dict: ").split(",")
d1 = {}
for i in n1:
    temp = i.split(":")
    d1[(temp[0])] = int(temp[1])

n2 = input("enter 2nd dict: ").split(",")
d2 = {}
for i in n2:
    temp = i.split(":")
    d2[(temp[0])] = int(temp[1])

d3 = final_dic = {}

for i in d1:
    d3[i] = d1[i]

for i in d2:
    if i in d3:
        d3[i] = d3[i] + d2[i]
    if i not in d3:
        d3[i] = d2[i]

a = values = []

for i in d3:
    if d3[i] not in a:
        a.append(d3[i])

for i in range(len(a)):
    for j in range(len(a)):
        if a[j] > a[i]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

print(d3)
print("Values:",tuple(a))

'''