def div(min, max, divisor):
    sum = 0

    for i in range(min, max, 1):
        if i % divisor == 0:
            sum += i

    return sum


print(div(0, 10, 2))
print(div(3, 16, 3))
