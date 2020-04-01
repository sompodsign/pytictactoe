#Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad,
#  so you get a 3 by 3 board representation.

# from Ipython.display import clear_output

def display_board(board):
    print('   |   |   ')
    print(f' {board[0]} | {board[1]} | {board[2]}')
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(f' {board[0]} | {board[1]} | {board[2]}')
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(f' {board[0]} | {board[1]} | {board[2]}')
    print('   |   |   ')

def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player1, choose X or O: ')
    player1 = marker
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
        
    print(player1, player2)

player_input()







