# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import numpy as np

def check_row(row, board):
    temp_row = np.arange(1, 9, int)
    for col in range(1, 9):
        value  = board[row, col]
        if temp_row[value]:
            return False
        else:
            temp_row[value] = True

    return True

def check_col(col, board):
    temp_col = np.arange(1, 9, int)
    for row in range(1, 9):
        value  = board[row, col]
        if temp_col[value]:
            return False
        else:
            temp_col[value] = True
    return True

def check_square(s_row, s_col, board):
    temp_square = [False] * 9
    for row in range(1, 3):
        for col in range(1, 3):
            value  = board[s_row * 3 + row , s_col * 3 + col]
            if temp_square[value]:
                return False
            else:
                temp_square[value] = True
    return True

def check_move(move, board):
    board[move.row][move.col] = move.value
    for row in range(1, 9):
        if not check_row(row, board):
            return False
    for col in range(1, 9):
        if not check_col(col, board):
            return False
    for s_row in range(0, 2):
        for s_col in range(0, 2):
            if not check_square(s_row, s_col, board):
                return False
    return True

board =