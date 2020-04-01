import random

def display_board(board):
    print('   |   |   ')
    print(f' {board[7]} | {board[8]} | {board[9]}')
<<<<<<< HEAD
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(f' {board[4]} | {board[5]} | {board[6]}')
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(f' {board[1]} | {board[2]} | {board[3]}')
    print('   |   |   ')
=======
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(f' {board[4]} | {board[5]} | {board[6]}')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(f' {board[1]} | {board[2]} | {board[3]}')
    print('   |   |   ')
>>>>>>> 56e1aabe51cb78bb7c8a9b91c1acd5800397e7c8


def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player1, choose X or O: ').upper()
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1, player2)

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[7] == board[8] == board[9] == mark) or 
            (board[4] == board[5] == board[6] == mark) or 
            (board[1] == board[2] == board[3] == mark) or
            (board[1] == board[5] == board[9] == mark) or
            (board[3] == board[5] == board[7] == mark))

def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose a position: (1-9) '))
    return position

def replay():
    choice = input("Play again? Enter Yes or No")
    return choice == 'Yes'

print('Welcome to Tic Tac Toe!')
while True:
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play? y or n?')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)
            if win_check(the_board, player1_marker):
                print('Player 1 won!')
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie Game!')
                    break
                else:
                    turn = 'Player 2'
        else:
            
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)
            if win_check(the_board, player2_marker):
                print('Player 2 won!')
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie Game!')
                    break
                else:
                    turn = 'Player 1'
        if not replay():
            break