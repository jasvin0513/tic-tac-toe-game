from board import *
from game_rules import *
from player import *

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
        board = player_choice(board, player)
        
        print_board(board)
        
        if is_win(board, player):
            print(f"Win found in row {row+1}")
            print(f"Player {player} is the winner")
            break
        elif is_full(board):
            print(f"Win found in row {row+1}")
            print("The board is full")
            break
        
        # Swap between players
        player = "O" if player == "X" else "X"
        
play_game()