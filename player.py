board = [[" " for _ in range(3)] for _ in range(3)]

def player_choice(board, player):
    """
    Accepts the player's choice of row and column before adding their choice to the board
    """

    while True:
        row = validate_choice("row", player)
        col = validate_choice("column", player)
                
        if validate_board(board, row-1, col-1):
            board[row-1][col-1] = player
            return board

def validate_choice(dim, player):
    """
    Checks to see if the input value is valid
    """
    while True:
        try:
            choice = int(input(f"Player {player}: Choose {dim} 1, 2 or 3: "))
            if 1 <= choice <= 3:
                return choice
            else:
                print(f"Please enter a valid {dim}")
        except ValueError:
            print("Please enter a valid number")
            
def validate_board(board, row, col):
    """
    Checks to see if the row and column position on the board is available
    """
    if board[row][col] != " ":
        print("This space is taken. Please choose another")
        return False
    else:
        return True