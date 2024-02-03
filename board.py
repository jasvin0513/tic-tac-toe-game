def print_board(board):
    """
    Prints the entire board matrix in a 3x3 grid
    """
    for row in range(3):
        print_row(board, row)

def print_row(board, row):
    """
    Prints a given row in the board matrix
    """
    # Top row in cell
    print((" " * 7) + "|" + (" " * 7) + "|" + (" " * 7))

    # Middle row in cell
    print((" " * 3) + str(board[row][0]) + (" " * 3) + "|", end = "")
    print((" " * 3) + str(board[row][1]) + (" " * 3) + "|", end = "")
    print((" " * 3) + str(board[row][2]) + (" " * 3))

    # Bottom row in cell
    if row == 2:
        print((" " * 7) + "|" + (" " * 7) + "|" + (" " * 7))
    else:
        print(("_" * 7) + "|" + ("_" * 7) + "|" + ("_" * 7))