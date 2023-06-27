import random


def computer_guess(x):
    guess = 0
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # Can also be set to high because low = high
        feedback = input(f'Is {guess} too High (H), Too Low (L), Or Correct (C): ').lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'\nYay Computer guessed the number {guess} correctly!!!')


computer_guess(100)
