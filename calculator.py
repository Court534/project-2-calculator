# Welcome messages 
print("Welcome to my Python calculator!")
print("You can Add, Subtract, Multiply and Divide")
print("Type what would you like to do? \nAdd (+) \nSubtract (-) \nMultiply (*) \nDivide (/)")

# Get user input
user_input = input("Type the name or symbol of the mathematical function you would like to use: ")

# Math functions
def add(a, b):
    return a + b
    
def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
    
def divide(a, b):
    return a / b


# Swith to that math function
while True:
    
    if user_input == "Add" or user_input == "+":
        print("You've chosen addition!")
            
    elif user_input == "Add" or user_input == "+":
         print("You've chosen addition!")
            
    elif user_input == "Add" or user_input == "+":
        print("You've chosen addition!")
            
    elif user_input == "Add" or user_input == "+":
        print("You've chosen addition!")
        
    else:
        input("Sorry, try again: ")
        continue        
        
    
