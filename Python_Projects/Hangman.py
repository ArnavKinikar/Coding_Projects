import random
import string

from Hangman_Words import words


def Valid_Word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def Hangman():
    word = Valid_Word(words)
    word_letters = set(word)  # Letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # What the user has guessed
    lives = 6

    # Getting the input
    while len(word_letters) > 0 and lives > 0:

        # letters already used
        print("\nYou have used these letters: ", " ".join(used_letters))
        print(f"You have {lives} Lives left.")

        # What current word is (ie W _ R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current Word: ", "".join(word_list))

        user_letter = input("Guess a Letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1  # Takes a life if wrong
                print("\n\nLetter not in word.")

        elif user_letter in used_letters:
            print("You have already used that character. Please try again")
        else:
            print("Invalid Character. Please try again")

    if lives == 0:
        print("Sorry, You died. Better luck next time")
    else:
        print(f"You Guessed the word {word} correctly")


Hangman()
