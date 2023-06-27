def findNextEmpty(puzzle):
    # Find the next row, col that is not filled yet --> rep with -1
    # Return row, col tuple ( of (None, None) if there is none)

    #We are using 0-8 indices
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c

    return None, None # If no spaces are empty

def isValid(puzzle, guess, row, col):
    # Figures out wether the guess at the row/col of the puzzle is a valid guess
    # Returns True if valid, otherwise False

    # For Rows
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # For Columns
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # For each sqaure
    # Iterate over 3 values in the row/column
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    # If all of these checks pass then guess is valid
    return True


def solveSudoku(puzzle):
    # Solve sudoku using backtracking
    # Return wether a solution exists
    # Mutates o be the solution (If solution exists)

    # Step 1: Choose somewhere on the puzzle to make a guess
    row, col = findNextEmpty(puzzle)

    # Step 1.1: If there's nowhere left, then we are done because we only allowes valid inputs
    if row is None:
        return True


    # Step 2: If there is a place to put a number then make a geuss between 1 and 9
    for guess in range(1, 10):
        # Step 3: Check if it is valid
        if isValid(puzzle, guess, row, col):
            # Step 3.1: If this is valid, then place the guess at the location
            puzzle[row][col] = guess

            # Step 4: Recursively call our function
            if solveSudoku(puzzle):
                return True

        # Step 5: If not valid OR if our guess does not solve the puzzle we need to backtrack and try new guess
        puzzle[row][col] = -1 # Reset the guess

    # Step 6: If none of the members that we try work, then this puzzle is unsolvable
    return False


if True:
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solveSudoku(example_board))
    print(example_board)