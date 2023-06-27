import random


def play():

    while True:
        user = input("Input Rock (R), Paper (P), Scissors (S): ").lower()
        computer = random.choice(['r', 'p', 's'])

        if computer == user:
            print("\nIt is a Tie.\n")
        elif computer == 'r' and user == 'p':
            print("\nThe Computer Chose Rock.")
            print("You Won!!\n")
        elif computer == 'r' and user == 's':
            print("\nThe Computer Chose Rock.")
            print("Computer Won! Better luck next time.\n")
        elif computer == 'p' and user == 'r':
            print("\nThe Computer Chose Paper.")
            print("Computer Won! Better luck next time.\n")
        elif computer == 'p' and user == 's':
            print("\nThe Computer Chose Paper.")
            print("You Won!!\n")
        elif computer == 's' and user == 'r':
            print("\nThe Computer Chose Scissors.")
            print("You Won!!\n")
        elif computer == 's' and user == 'p':
            print("\nThe Computer Chose Scissors.")
            print("Computer Won! Better luck next time.\n")

        con = input("Play Again (Y/N): ").lower()

        if con == 'n':
            print("\nThanks For Playing!!")
            break


play()
