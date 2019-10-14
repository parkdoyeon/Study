#!/bin/python3

import os
import sys

#
# Complete the jumpingRooks function below.
#
def jumpingRooks(k, board):
    board = makeBoard(k, board)
    beat = 0

    for n in range(len(board)):
        row = []
        for m in range(len(board)):
            if(board[n][m] == '#'):
                rocks = row.count('o')
                beat += (rocks*(rocks-1))/2
                row = []
                continue
            row.append(board[n][m])
        rocks = row.count('o')
        beat += (rocks*(rocks-1))/2

    for n in range(len(board)):
        row = []
        for m in range(len(board)):
            if(board[m][n] == '#'):
                rocks = row.count('o')
                beat += (rocks*(rocks-1))/2
                row = []
                continue
            row.append(board[n][m])
        rocks = row.count('o')
        beat += (rocks*(rocks-1))/2

    return int(beat)

def makeBoard(k, board):

    for n in range(len(board)):
        if k < 1: break
        if board[n][n] == '.':
            board[n][n] = 'o'
            k -= 1
    
    for n in range(len(board)):
        if k < 1: break
        if board[n][len(board)-1-n] == '.':
            if n == len(board)-1-n: continue
            board[n][len(board)-1-n] = 'o'
            k -= 1

    for n in range(len(board)):
        for m in range(len(board)):
            if k == 0: break
            if board[n][m] == '.':
                board[n][m] = 'o'
                k -= 1
    
    for b in board:
        print(b)
    return board

if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])

    board = []

    for _ in range(n):
        board_item = input()
        board.append(list(board_item))

    result = jumpingRooks(k, board)

    print(str(result) + '\n')
