class buttons:
    
    def __init__(self, button_name, no_of_spaces, border_sign):
        
        self.button_name = button_name
        self.spaces = no_of_spaces
        self.border = border_sign
        print(f'{self.button_name} Button Specifications:')
        print(f'Button Name: {self.button_name}')
        space_count = (1 + self.spaces + len(self.button_name) + self.spaces + 1)
        print(f'Number of the border characters for the top and the bottom: {space_count}')
        print(f'Number of spaces between the left side border and the first character of the button name: {self.spaces}')
        print(f'Number of spaces between the right side border and the last character of the button name: {self.spaces}')
        print(f'Characters representing the borders: {self.border}')
        print(f'{self.border * space_count}')
        print(f'{self.border + (" " * self.spaces) + self.button_name + (" " * self.spaces) + self.border}')
        print(f'{self.border * space_count}')
        
word = "CANCEL"  
spaces = 10
border = 'x'
b1 = buttons(word, spaces, border)
print("=======================================================")
b2 = buttons("Notify",3, '!')
print("=======================================================")
b3 = buttons('SAVE PROGRESS', 5, '$')
