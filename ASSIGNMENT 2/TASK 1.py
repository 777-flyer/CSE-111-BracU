def fraction(numerator,denominator):

  if denominator == 0:
    return 0
  else:
    return (numerator / denominator) - (numerator // denominator)

num = int(input('Please enter the numerator: '))
den = int(input("Please enter the denominator: "))

result = fraction(num,den)
print(result)