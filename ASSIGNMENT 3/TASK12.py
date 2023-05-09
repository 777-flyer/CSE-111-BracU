# Write your code here

class Calculator:
    
    def __init__(self):
        self.backend_history = []
        print("Calculator is ready!")
        
    def calculate(self, value_1, value_2, operator):
        
        if operator == "+":
            result = value_1 + value_2
        
        elif operator == "-":
            result = value_1 - value_2

        elif operator == "*":
            result = value_1 * value_2

        elif operator == "/":
            result = value_1 / value_2

        else:
            print("Please check your inputs!")
            return None
        
        self.backend_history.append((value_1,value_2,operator,result))
        return result
    
    def showCalculation(self):
      
      list_a = self.backend_history[-1]
      print(f'{list_a[0]} {list_a[2]} {list_a[1]} = {list_a[3]}')
      
c1 = Calculator()
print("==================")
val = c1.calculate(10, 20, '+')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 10, '-')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 5, '*')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 16, '/')
print("Returned value:", val)
c1.showCalculation()
