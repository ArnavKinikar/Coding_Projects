import random
import re


# Create a board to represent the minesweeper game
# This is so that we can just say "Create a new board" or "Dig Here" of "Render this game for this object"
class Board:
    def __init__(self, dim_size, num_bombs):
        # let's keep track of these parameters. they'll be helpful later
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # let's create the board
        # helper function!
        self.board = self.make_new_board()  # plant the bombs
        self.assign_values_to_board()

        # initialize a set to keep track of which locations we've uncovered
        # we'll save (row,col) tuples into this set
        self.dug = set()  # if we dig at 0, 0, then self.dug = {(0,0)}

    def make_new_board(self):
        # construct a new board based on the dim size and num bombs

        # generate a new board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        # plant the bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size ** 2 - 1)  # return a random integer N such that a <= N <= b
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == '*':
                # Bomb already there
                continue

            board[row][col] = '*'  # plant the bomb
            bombs_planted += 1

        return board

    def assign_values_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    # if this is already a bomb, don't calculate anything
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):
        # let's iterate through each of the neighboring positions and sum number of bombs
        # make sure to not go out of bounds!

        num_neighboring_bombs = 0
        for r in range(max(0, row - 1), min(self.dim_size - 1, row + 1) + 1):
            for c in range(max(0, col - 1), min(self.dim_size - 1, col + 1) + 1):
                if r == row and c == col:
                    # our original location, don't check
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1

        return num_neighboring_bombs

    def dig(self, row, col):
        # dig at that location!
        # return True if successful dig, False if bomb dug

        # Scenarios:
        # hit a bomb -> game over
        # dig at location with neighboring bombs -> finish dig
        # dig at location with no neighboring bombs -> recursively dig neighbors

        self.dug.add((row, col))  # keep track that we dug here

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True

        # self.board[row][col] == 0
        for r in range(max(0, row - 1), min(self.dim_size - 1, row + 1) + 1):
            for c in range(max(0, col - 1), min(self.dim_size - 1, col + 1) + 1):
                if (r, c) in self.dug:
                    continue  # don't dig where you've already dug
                self.dig(r, c)

        # if our initial dig didn't hit a bomb, we *shouldn't* hit a bomb here
        return True

    def __str__(self):
        # It prints out whatever  this function returns

        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '

        # Put this in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key=len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % col)
        indices_row += '  '.join(cells)
        indices_row += '  \n'

        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % col)
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-' * str_len + '\n' + string_rep + '-' * str_len

        return string_rep


# Play the Game

def play(dim_size=10, num_bombs=10):
    # Step 1: Create the board and plant the bombs
    board = Board(dim_size, num_bombs)

    # Step 2: Show the borad to the user and ask for the dig location
    # Step 3A: If location is a bomb, Show game over message
    # Step 3B: If location is not a bomb, dig recursively until each swaure is atleast next to a bomb
    # Step 4: Repeat steps 2 and 3A/B until there are no movre places to dig -> Victory!

    safe = True

    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col: "))  # '0, 3'
        row, col = int(user_input[0]), int(user_input[-1])

        # If user inputs invalid location
        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
            print("Invalid location. Try again.")
            continue

        # If user inputes valid location
        safe = board.dig(row, col)

        if not safe:
            # Dug a bomb
            break

    # 2 ways to end the loop
    if safe:
        print("Congratulations!! You win!!")
    else:
        print("Game Over")
        # Revealing the whole board!!
        board.dug = [(r, c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)


play()
