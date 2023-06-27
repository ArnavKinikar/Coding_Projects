import random


def guess(x):
    randomNum = random.randint(1, x)

    guess = 0

    while guess != randomNum:

        guess = int(input(f'Guess a number between 1 and {x}: '))

        if guess > randomNum:
            print('\nTry again, Too high\n')
        elif guess < randomNum:
            print('\nTry again, Too low\n')

    print(f'\nCongratulations!! You have guessed the number {randomNum} correctly')

guess(100)
