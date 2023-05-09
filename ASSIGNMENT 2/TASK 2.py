def bmi_calc(height, weight):  # height first and then weight

    height_m = height / 100
    bmi = (weight / (height_m) ** 2)

    if bmi < 18.5:
        print(f'Score is {bmi:.1f}. You are Underweight')
    elif 18.5 <= bmi <= 24.9:
        print(f'Score is {bmi:.1f}. You are Normal')
    elif 25 <= bmi <= 30:
        print(f'Score is {bmi:.1f}. You are Overweight')
    elif bmi > 30:
        print(f'Score is {bmi:.1f}. You are Obese')


bmi_calc(int(input("Please enter your height in cm: ")),
         int(input("Hello,Sir! Please enter your weight in Kilogram(kg) please: ")))

# another way------------------


# def bmi_calc(height,weight):

#     height_m = height / 100
#     bmi = (weight/(height_m)**2)

#     if bmi < 18.5:
#         condition = 'Underweight'
#     elif 18.5 <= bmi <= 24.9:
#         condition = 'Normal'
#     elif 25 <= bmi <= 30:
#         condition = 'Overweight'
#     elif bmi > 30:
#         condition = 'Obese'

#     return f'Score is {bmi:.1f}. You are {condition}'

# print(bmi_calc(175,96))
