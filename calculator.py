""""Task 9: Compulsory Task 1:"""
# Here we are using a function called calculator, inside are everything we need
# We have 3 different while true loops - this is because if an error is made, only repeat where error is made
# Using different while loops increases code but makes user experience better
# Inside the last loop, we use the variable zero to return error if num = 0

def calculator():
    while True:
        try:
            num1 = float(input("Please enter your first number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a numer: ")

    while True:
        operator = input("Enter an operator (+, -, *, /): ")
        if operator in ["+", "-", "*", "/"]:
            break
        else:
            print("Invalid operator! Please enter one of the following: +, -, *, /: ")

    while True:
        try:
            num2 = float(input("Please enter your second number: "))
            try:
                if operator == "/" and num2 == 0:
                    raise ValueError("You can not divide by zero (0)")
            except ValueError as zero:
                print(zero)
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a number: ")

    # The code below if, elif, else statement are for the calculator to know what to do for each symbol
    # Then we store the answer in the equation variable
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "/":
        result = num1 / num2
    elif operator == "*":
        result = num1 * num2

    equation = str(num1) + " " + operator + " " + str(num2) + " = " + str(result)
    return equation

# Below we have the main function to give user a decision to make, saving file, reading the file and repeat
# We made sure that the inputs are not case-sensitive
# I used first principles to make sure I am expecting all errors and working logically
# "def" is how you define a function

def main():
    while True:
        user = input("Please enter 'new' to perform a new calculation or 'read' to read equations from a file: ")
        if user.lower() == "new":
            equation = calculator()
            print("Your equation:", equation)
            file_name = input("Please enter a file name to save the equation to: ")
            try:
                with open(file_name, "a") as file:
                    file.write(equation)
            except IOError:
                print("Error: file not found")
                continue
        elif user.lower() == "read":
            file_name = input("Please enter the file name to read the equations from: ")
            try:
                with open(file_name, "r") as file:
                    print(file.read())
            except IOError:
                print("Error: file not found")
                continue
        else:
            print("Invalid choice, please enter 'new' or 'read'")
            continue

        again = input("Do you want to perform another calculation (y/n): ")
        if again.lower() == "n":
            print("Thank you for using the calculator with ALI@Hyperion-Dev Bootcamp!")
            break

# call the main function
main()
