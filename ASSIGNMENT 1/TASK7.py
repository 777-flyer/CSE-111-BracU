user = int(input("Enter the number of lists: "))
list_creator = []
highest_sum = -1
highest_list = []

for inp in range(user):
    
    user_list = input("Sir,Please enter the elements of the list separated by a space: ").split()
    list_creator.append(user_list)
    list_sum = 0
    
    for summer in range(len(user_list)):
        
        list_sum += int(user_list[summer])
        
    if list_sum > highest_sum:
        
        highest_sum = list_sum
        highest_list = user_list
        
        
print("The highest sum is : {}".format(highest_sum))
print("The highest sum's list is : {}".format(highest_list))
