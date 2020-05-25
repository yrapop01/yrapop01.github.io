"""
    Simple Tic-Tac-Toe implementation.
"""

import sys

def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('---------')
    print()

def guess_o(board):
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == ' ':
                board[i] = board[i][:j] + 'O' + board[i][j+1:]
                return

def read_coord(board):
    i = int(input('Next row: '))
    if not (0 <= i <= 2):
        print('Bad coordinate format')
        return None

    j = int(input('Next column: '))
    if not (0 <= j <= 2):
        print('Bad coordinate format')
        return None

    if board[i][j] != ' ':
        print('The coordinate is taken.')
        return None
    return (i, j)

def read_x(board):
    coord = read_coord(board)
    while coord is None:
        coord = read_coord(board)

    i, j = coord
    board[i] = board[i][:j] + 'X' + board[i][j+1:]
    print_board(board)

def is_a_win(board, symbol):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == symbol:
            return True
        if board[0][i] == board[1][i] == board[2][i] == symbol:
            return True
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return True

    return False

def main():
    board = ['   ' for i in range(3)]
    while ' ' in ''.join(board):
        print_board(board)
        read_x(board)
        if is_a_win(board, 'X'):
            print('X wins')
            break

        guess_o(board)
        if is_a_win(board, 'O'):
            print('O wins')
            break

    print_board(board)
 
if __name__ == "__main__":
    main()
