import math
import random


class Player:
    def __init__(self, letter):
        # the letter is X or O
        self.letter = letter

    # The next move
    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            # We are going to check this is a correct value y trying to cast
            # it to an integer, and if it is not, then we say it is invalid
            # if that spot is not available on the board, we also say its invalid

            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True  # if these are successful, the yay!
            except ValueError:
                print("Invalid square, Try again")
        return val
