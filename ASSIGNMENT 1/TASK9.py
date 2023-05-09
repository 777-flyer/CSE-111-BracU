# I'm describing my code as so many of you requested it to do


# I'm taking the number of students and the time BracU head wants each team to participate in finals

n, k = int(input("Sir,Please enter the number of students: ")), int(
    input("Sir,Please enter the number of times you want each team to participate: "))

st_participations = []

for i in range(n):
    st_participations.append(int(input("Please enter the number of times each student has already participated: ")))

# Now I am done taking inputs from the BracU head, we will check how many times a student has left in his store
# to participate more.

available_participations = []

for j in st_participations:
    available_participations.append(5 - j)

print(
    f"This list represents how many times each student has left in his hand to participate: {available_participations}")

'''
now we will check how many student can meet the requirement given by BracU head.
For example, the value of k is 4, so each team and all the same members from that team has to 
participate 4 times in the finals next. We will now take those students only whose available
time of participation meets this requirement.
'''

valid_members = 0

for approved in range(len(available_participations)):

    if available_participations[approved] >= k:  # this is the most important part
        valid_members += 1  # try to understand

print(f"The number of approved students is: {valid_members}")

'''
as each team contains minimum and maximum 3 members,
'''

max_teams = valid_members // 3

print(f"Maximum Team/s Available: {max_teams}")
