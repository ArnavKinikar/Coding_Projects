# This program is to make a Simple Calculator

# Functions

def add(x, y):
    return int(x) + int(y)


def sub(x, y):
    return int(x) - int(y)


def div(x, y):
    return int(x) / int(y)


def mul(x, y):
    return int(x) * int(y)


print("1. Addition \t 2. Subtraction \t 3. Division \t 4. Multiply")

while True:
    # To Repeat the entire program

    # To get intput
    choice = input("Select Option by selecting the number: ")

    # Verifying that choice is one of 4
    if choice in ("1", "2", "3", "4"):
        num1 = input("Enter 1st Number: ")
        num2 = input("Enter 2nd Number: ")

        if choice == "1":
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == "2":
            print(num1, "-", num2, "=", sub(num1, num2))

        elif choice == "3":
            print(num1, "/", num2, "=", div(num1, num2))

        elif choice == "4":
            print(num1, "*", num2, "=", mul(num1, num2))

        nextCalculation = input("Another Calculation(Y/N): ")
        if nextCalculation == "N" or nextCalculation == "n":
            break

    else:
        print("Invalid Input")
