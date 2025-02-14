#Functions for the main program

def addition(num1, num2):
    print("The sum is: ", format(num1 + num2, '.0f'))

def substraction(num1, num2):
    print("The result is: ", format(num1 - num2, '.0f'))

def multiplication(num1, num2):
    print("The result is: ", format(num1 * num2, '.0f'))

def division(num1, num2):
    if num2 == 0.0:
        print("Cannot divide by zero")
    else:
        print("The result is: ", format(num1 / num2, '.3f'))