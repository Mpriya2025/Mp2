import random

# Game board
board = [' ' for _ in range(9)]

# Function to draw the game board
def draw_board():
    row1 = '| {} | {} | {} |'.format(board[0], board[1], board[2])
    row2 = '| {} | {} | {} |'.format(board[3], board[4], board[5])
    row3 = '| {} | {} | {} |'.format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

# Function to handle player move
def player_move(player):
    run = True
    while run:
        move = input("Please select a position to place an '{}' (1-9): ".format(player))
        try:
            move = int(move)
            if move > 0 and move < 10:
                if space_is_free(move):
                    run = False
                    insert_letter(player, move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')

# Function to handle computer move
def computer_move():
    run = True
    while run:
        move = random.randint(1, 9)
        if space_is_free(move):
            run = False
            insert_letter('O', move)
            return

# Function to check if space is free
def space_is_free(pos):
    return board[pos - 1] == ' '

# Function to insert letter at position
def insert_letter(letter, pos):
    board[pos - 1] = letter

# Function to check if board is full
def is_board_full():
    return board.count(' ') == 0

# Function to check for a win
def is_winner(player):
    winning_combos = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combo in winning_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Main game loop
def play_game():
    print('Welcome to Tic Tac Toe!')
    draw_board()

    while True:
        player_move('X')
        draw_board()
        if is_winner('X'):
            print('X\'s win!')
            break
        elif is_board_full():
            print('Tie game!')
            break

        computer_move()
        draw_board()
        if is_winner('O'):
            print('O\'s win!')
            break
        elif is_board_full():
            print('Tie game!')
            break

play_game()
