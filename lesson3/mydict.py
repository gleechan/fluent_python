#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright jitui 2018
#
# @author: chenyongjian@jituia.com
#

# a = dict(one=1, two=2, three=3)
# b = {'one': 1, 'two': 2, 'three': 3}
# c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
# d = dict([('one', 1), ('two', 2), ('three', 3)])
# print(z for z in zip(['one', 'two', 'three'], [1, 2, 3]))
# print(a == b == c == d)

a = {}
b = zip(['one', 'two', 'three'], [1, 2, 3])
a.update(b)
