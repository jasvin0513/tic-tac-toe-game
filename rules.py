def is_win(board, player):
    """
    Checks if the player has met any of the win conditions
    """
    # Check rows
    for row in range(3):
        if (board[row][0] == player) and (board[row][0] == board[row][1] == board[row][2]):
            print(f"Win found in row {row+1}!")
            return True
        
    # Check columns
    for col in range(3):
        if (board[0][col] == player) and (board[0][col] == board[1][col] == board[2][col]):
            print(f"Win found in column {col+1}!")
            return True
    
    # Check diagonals
    if (((board[0][0] == player) and (board[0][0] == board[1][1] == board[2][2])) or 
        ((board[0][2] == player) and (board[0][2] == board[1][1] == board[2][0]))):
        print("Diagonal win!")
        return True
    
    return False

def is_full(board):
    """
    Checks if the board is full
    """
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                return False
    
    return True