# UB Jumper problem

while True:
    sequence = input("Enter a number sequence (or STOP to exit): ")
    if sequence == "STOP":
        break
    sequence = sequence.split()
    n = len(sequence)
    int_sequence = []
    for i in range(n):
        int_sequence.append(int(sequence[i]))
    absolute_diffs = []
    for i in range(1, n):
        absolute_diffs.append(abs(int_sequence[i] - int_sequence[i-1]))
    absolute_diffs.sort()
    flag = True
    # for i in range(n-1):
    #     if absolute_diffs[i] != i+1:
    #         flag = False
    #         break
    flag = True
    for i in range(1, n):
        if i not in absolute_diffs:
            flag = False
            break

    if flag:
        print("UB Jumper")
    else:
        print("Not UB Jumper")
