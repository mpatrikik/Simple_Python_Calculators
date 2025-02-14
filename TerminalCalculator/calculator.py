#Simple calculator using terminal

from functions import *

while True:
    print("What do u want to do?")
    print("1 Addition")
    print("2 Subtraction")
    print("3 Multiplication")
    print("4 Division")
    print("Enter Q to exit")

    choice = input("Enter your choice: ")
    if choice == 'q' or choice == 'Q':
        break

    num1 = float(input("Enter the Number 1: "))
    num2 = float(input("Enter the Number 2: "))

    if choice == '1':
        addition(num1, num2)
    elif choice == '2':
        substraction(num1, num2)
    elif choice == '3':
        multiplication(num1, num2)
    elif choice == '4':
        division(num1, num2)
    else:
        print("Invalid choice")

    print("\n")
