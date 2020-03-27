#Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad,
#  so you get a 3 by 3 board representation.

# from Ipython.display import clear_output

def display_board(board):
    print('   |   |   ')
    print(f' {board[0]} | {board[1]} | {board[2]}')
    print('   |   |   ')
    print('-----------')








test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)
