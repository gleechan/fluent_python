#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright jitui 2018
#
# @author: chenyongjian@jituia.com
#
# board = [['_'] * 3 for i in range(3)]
# print(board)
# board[1][2] = 'X'
# print(board)
#
# # 错误演示
# weird_board = [['_'] * 3] * 3
# print(weird_board)
# weird_board[1][2] = 'O'
# print(weird_board)

# 错误演示
# row = ['_'] * 3
# board = []
# for i in range(3):
#     board.append(row)
# print(board)
# board[1][2] = 'X'
# print(board)

# 正确演示
board = []
for i in range(3):
    row = ['_'] * 3
    board.append(row)

print(board)
board[1][2] = 'O'
print(board)
