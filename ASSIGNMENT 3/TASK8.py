class Calculator:
    
    def __init__(self, first_value, operator, second_value):
        
        self.first_value = first_value
        self.operator = operator
        self.second_value = second_value
    
    print("Let's Calculate!")

    def add(self):
        print(f'Value 1: {self.first_value}')
        print(f'Operator: {self.operator}')
        print(f'Value 2: {self.second_value}')
        print("Result: ", first_value + second_value)
    
    def subtract(self):
        print(f'Value 1: {self.first_value}')
        print(f'Operator: {self.operator}')
        print(f'Value 2: {self.second_value}')
        print("Result: ", first_value - second_value)
    
    def multiply(self):
        print(f'Value 1: {self.first_value}')
        print(f'Operator: {self.operator}')
        print(f'Value 2: {self.second_value}')
        print("Result: ", first_value * second_value)
    
    def divide(self):
        print(f'Value 1: {self.first_value}')
        print(f'Operator: {self.operator}')
        print(f'Value 2: {self.second_value}')
        print("Result: ", first_value / second_value)
        
first_value = int(input("Sir,Please enter the first number: "))
operator = input("Sir,Please enter the operator: ")
second_value = int(input("Sir,Please enter the second number: "))

calc = Calculator(first_value,operator,second_value)

if operator == "+":
    calc.add()
elif operator == "-":
    calc.subtract()
elif operator == "*":
    calc.multiply()
elif operator == "/":
    calc.divide()
else:
    print("Please enter a valid operator!")