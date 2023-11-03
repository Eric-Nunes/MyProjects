import random

# Initialize an empty board
board = [" " for _ in range(9)]

# Function to display the Tic-Tac-Toe board
def display_board():
    print(" " + board[0] + " | " + board[1] + " | " + board[2] + " ")
    print("-----------")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
    print("-----------")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")

# Function to check for a win
def check_win(player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Function for the computer's move (random)
def computer_move():
    while True:
        move = random.randint(0, 8)
        if board[move] == " ":
            return move

# Main game loop
player = "X"
computer = "O"
while True:
    display_board()
    print(f"Player {player}'s turn.")
    
    # Get the player's move
    while True:
        move = int(input("Enter your move (0-8): "))
        if 0 <= move <= 8 and board[move] == " ":
            board[move] = player
            break
        else:
            print("Invalid move. Try again.")
    
    # Check for a win
    if check_win(player):
        display_board()
        print(f"Player {player} wins!")
        break
    
    # Check for a draw
    if " " not in board:
        display_board()
        print("It's a draw!")
        break
    
    # Computer's move
    computer_move_position = computer_move()
    board[computer_move_position] = computer
    
    # Check for a win
    if check_win(computer):
        display_board()
        print("Computer wins!")
        break
