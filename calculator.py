# Welcome messages 
print("Welcome to my Python calculator!\n")
print("You can Add, Subtract, Multiply and Divide\n")
print("Type what would you like to do? \n1.Add (+) \n2.Subtract (-) \n3.Multiply (*) \n4.Divide (/)\n")

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
    
    # Get user input
    user_input = input("Type the number (1, 2, 3, 4) of the mathematical operation you would like to use: ")
    
    if user_input in ("1", "2", "3", "4"):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input, please enter either 1, 2, 3, 4")
            
     
     
                       
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
        
    
