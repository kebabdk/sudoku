import copy
import numpy as np
import itertools as it
from sympy.utilities.iterables import multiset_permutations


def check_row(row, board):
    temp_row = np.zeros(10, int)
    for col in range(0, 9):
        value = board[row, col]
#        print(f'row: {row} {col} {value}')
        if value > 0:
            if temp_row[value] == 1:
                return False
            else:
                temp_row[value] = 1
    return True


def check_col(col, board):
    temp_col = np.zeros(10, int)
    for row in range(0, 9):
        value = board[row, col]
        #print(f'col: {row} {col} {value}')
        if value > 0:
            if temp_col[value] == 1:
                #print(f'fail col: {row} {col} {value}')
                return False
            else:
                temp_col[value] = 1
    return True


def check_square(s_row, s_col, board):
    temp_values = np.zeros(10, int)
    for row in range(0, 3):
        for col in range(0, 3):
            value = board[s_row * 3 + row, s_col * 3 + col]
#           print(f'square: {s_row * 3 + row} {s_col * 3 + col} {value} -- {s_row} {s_col}')
            if value > 0:
                if temp_values[value] == 1:
                    # print(f'square fail: {s_row * 3 + row} {s_col * 3 + col} {value} -- {s_row} {s_col}')
                    return False
                else:
                    temp_values[value] = 1
    return True


def contains_duplicates(X):
    counts = np.unique(X, return_counts=True)
    c0 = counts[0]
    c1 = counts[1]
    # print(f' contains_duplicates {X} {c0} {c1} {len(c1)+c1[0]}')
    if c0[0] == 0:
        # print('   is 0')
        return len(c1)+c1[0] != 10
    else:
        # print(f' contains_duplicates {X} {c0} {c1} {len(c1)+c1[0]} {len(c1) != 9}')
        return len(c1) != 9


def contains_duplicates_1(X):
    seen = set()
    seen_add = seen.add
    for x in X:
        if x != 0:
            if (x in seen or seen_add(x)):
                return True
    return False


def check_board(board):
    for col in range(0, 9):
        if not check_col(col, board):
            return False
    for s_row in range(0, 3):
        for s_col in range(0, 3):
            if not check_square(s_row, s_col, board):
                return False
    return True


def check_board_alt(board):
    for col in range(0, 9):
        col_arr0 = board[:, col]
        # print(col_arr0)
        if contains_duplicates_1(col_arr0):
            # print('  dub')
            return False
    for s_row in range(0, 3):
        for s_col in range(0, 3):
            if not check_square(s_row, s_col, board):
                return False
    return True


def find_free(row, board):
    temp = np.zeros(10, int)
    ro = []
    pos = []
    for col in range(0, 9):
        value = board[row, col]
        if value > 0:
            temp[value] = 1
        else:
            pos.append(col)

    for i in range(1, 10):
        if temp[i] == 0:
            ro.append(i)
            # print(f'value: {i} {ro}')
    return pos, ro


def all_rows(row_idx, fp, board):
    for row_num in multiset_permutations(fp[row_idx][1]):
        for col_idx, col in enumerate(fp[row_idx][0]):
            # print(f'{row_idx} {col_idx} {col}')
            board[row_idx, col] = row_num[col_idx]
        if check_board_alt(board):

            # print(f'Ok {row_idx}: {row_num}')
            # print(board)
            if row_idx == 7:
                print(f' {row_idx} {all_rows.counter}')
            if row_idx < 8:
                all_rows.counter += 1
                if all_rows.counter % 100 == 0:
                    print(f' {row_idx} {all_rows.counter}')
                m = copy.copy(board)
                all_rows(row_idx + 1, fp, m)
            else:
                print(f' SOLVED!!!! {all_rows.counter}')
                print(board)
                return


all_rows.counter = 0

def find_free_pos(board):
    free_pos_list = []
    for row in range(0, 9):
        free_pos_list.append(find_free(row, board))
    for row in range(0, 9):
        print(f'{row} {free_pos_list[row]}')
    return free_pos_list


mainboard_easy = np.array([
    [0, 2, 0, 8, 7, 1, 0, 0, 5],
    [0, 0, 0, 3, 4, 0, 7, 2, 0],
    [4, 7, 0, 2, 0, 0, 0, 9, 0],
    [6, 8, 0, 0, 0, 2, 4, 0, 0],
    [0, 3, 4, 0, 9, 0, 0, 6, 0],
    [2, 0, 9, 0, 0, 0, 5, 3, 0],
    [3, 0, 0, 9, 1, 0, 0, 8, 7],
    [0, 6, 0, 0, 0, 7, 0, 0, 0],
    [1, 9, 0, 6, 8, 0, 0, 5, 4]
    ]
)
mainboard_zero = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
)

#24000
mainboard_hard = np.array([
    [8, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 3, 0, 0, 7, 0, 0, 9, 1],
    [2, 0, 0, 0, 9, 0, 0, 0, 6],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 7, 0, 6, 0, 0, 0, 4],
    [3, 0, 0, 0, 0, 2, 0, 0, 9],
    [0, 0, 0, 0, 0, 0, 1, 8, 0],
    [0, 8, 0, 0, 0, 6, 4, 0, 0],
    [4, 0, 0, 0, 0, 5, 0, 0, 3]
    ]
)

# 493
mainboard_expert = np.array([
    [1, 3, 0, 0, 0, 5, 0, 4, 0],
    [0, 0, 0, 7, 3, 0, 0, 0, 0],
    [7, 0, 0, 0, 1, 9, 0, 0, 0],
    [0, 0, 6, 0, 0, 0, 1, 0, 9],
    [0, 0, 9, 8, 0, 0, 0, 0, 2],
    [8, 7, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 8, 0, 0, 0],
    [0, 0, 0, 3, 4, 0, 0, 6, 0],
    [6, 0, 0, 0, 0, 0, 0, 0, 5]
    ]
)

mainboard_evil = np.array([
    [0, 0, 2, 0, 0, 0, 0, 6, 0],
    [5, 6, 0, 3, 0, 0, 0, 0, 7],
    [0, 0, 8, 0, 0, 5, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 8],
    [6, 3, 0, 0, 0, 9, 0, 1, 0],
    [0, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 0, 0, 4, 0, 0],
    [9, 1, 0, 0, 0, 3, 0, 8, 0],
    [0, 0, 5, 0, 0, 0, 0, 0, 0]
    ]
)

print(mainboard_evil)
m = copy.copy(mainboard_evil)
free_pos = find_free_pos(m)
print('START!!')
all_rows(0, free_pos, m)
print('STOPPED!!')

