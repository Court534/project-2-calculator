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
    
    # Give the user a choice 
    if user_input in ("1", "2", "3", "4"):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input, please enter either 1, 2, 3, 4")
    
    # Add is 1                   
    if user_input == "1":
        print(num1, "+", num2, "=", add(num1, num2)) 
    
    # Subtract is 2   
    elif user_input == "2":
        print(num1, "-", num2, "=", subtract(num1, num2))
    
    # Subtract is 3    
    elif user_input == "3":
        print(num1, "*", num2, "=", multiply(num1, num2))
    
    # Divide is 4    
    elif user_input == "4":
        print(num1, "/", num2, "=", divide(num1, num2))
    
    # Ask if they would like to go again    
    new_calulation = input("Would you like do another calculation? (yes/no)")
    # If no then break out of the loop
    if new_calulation == "no":
        print("Thank you!")
        break
    # If yes then run the loop again 
    elif new_calulation == "yes":
        continue
    else:
        print("Invalid input")
