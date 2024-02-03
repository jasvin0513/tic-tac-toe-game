import board as b
import rules as r
import player as p

def play_game():
    """
    Plays a game of tic-tac-toe
    """
    print("A new game has been started. Player X will start")
    
    # Initialize player and board
    player = "X"
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    # Run loop until win condition is found
    while True:
        board = p.player_choice(board, player)
        
        b.print_board(board)
        
        if r.is_win(board, player):
            b.print_board(board)
            print(f"Player {player} is the winner!")
            break
        elif r.is_full(board):
            b.print_board(board)
            print("The board is full")
            break
        
        # Swap between players
        player = "O" if player == "X" else "X"
        
play_game()