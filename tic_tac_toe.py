# Tic tac toe game for two players.
from __future__ import print_function
import random
# Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds
# with a number on a number pad, so you get a 3 by 3 board representation.


def display_board(board):
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

    print('-----------')

    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])

    print('-----------')

    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

# Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using
# while loops to continually ask until you get a correct answer.


def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = raw_input('Player 1: Do you want to be X or O?').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


# Step 3: Write a function that takes, in the board list object, a marker ('X' or 'O'), and a desired position
# (number 1-9) and assigns it to the board.

def place_marker(board, marker, position):
    board[position] = marker

# Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won.
def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or  #  across the bottom
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[1] == mark and board[4] == mark and board[7] == mark) or  # down the left side
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal
# Step 5: function uses the random module to randomly decide which player goes first.


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
# Step 6: function returns a boolean indicating whether a space on the board is available.
# if board[position] == ' ' return TRUE else FALSE


def space_check(board, position):
    return board[position] == ' '

# Step 7: function checks if the board is full and returns a boolean value.
# True if full.


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

# Step 8: Player choose a position of a marker


def player_choice(board):
    # Using strings because of raw_input
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = raw_input('Choose your next position: (1-9) ')
    return int(position)

# Step 9: Replay game


def replay():
    answer = raw_input('Do you want to play again? Enter Yes or No: ').lower()
    if answer.startswith('y'):
        return True
    else:
        return False

# Step 10: Running game

def make_player_actions(player, player_marker):
    display_board(theBoard)
    # choose position of a marker
    position = player_choice(theBoard)
    # board[position] = marker
    place_marker(theBoard, player_marker, position)

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board, game will ignore 0's index
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    # which player starts
    turn = choose_first()
    print(turn + ' will go first.')
    game_on = True

    while game_on:
        if turn == 'Player 1':

            player = 'Player 1'

            make_player_actions(player, player1_marker)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! %s won the game!' % player)
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            player = 'Player 2'

            make_player_actions(player, player2_marker)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Congratulations! %s won the game!' % player)
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        print ("Thanks for playing")
        break
