#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright jitui 2018
#
# @author: chenyongjian@jituia.com
#

# import array

# symbols = '￥&×=-|'
# for symbol in symbols:
#     codes.append(ord(symbol))

# codes = [ord(s) for s in symbols]
# print(codes)

# codes = list(filter(lambda x: x > 300, map(ord, symbols)))
# print(codes)

colors = ['white', 'black']
sizes = ['S', 'M', 'L']
# tshirts = [(color, size) for color in colors for size in sizes]
# print(tshirts)
for tshirt in ((c, s) for c in colors for s in sizes):
    print(tshirt)

# print(tuple(ord(symbol) for symbol in symbols))
# print(array.array('I', (ord(symbol) for symbol in symbols)))