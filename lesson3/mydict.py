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
#
# a = {}
# b = zip(['one', 'two', 'three'], [1, 2, 3])
# a.update(b)

import sys
import re
import collections


# WORD_RE = re.compile(r'\w+')
# index = collections.defaultdict(list)
# index['a'].append(('one', 1))
# print(index)
# with open(sys.argv[1], encoding='utf-8') as fp:
#     for line_no, line in enumerate(fp, 1):
#         for match in WORD_RE.finditer(line):
#             word = match.group()
#             column_no = match.start() + 1
#             location = (line_no, column_no)
#             # oc = index.get(word, [])
#             # oc.append(location)
#             # index[word] = oc
#             index.setdefault(word, []).append(location)
#     for word in sorted(index, key=str.upper):
#         print(word, index[word])

#
# class StrKeyDict0(dict):
#     def __missing__(self, key):
#         print(1)
#         print(isinstance(key, str))
#         if isinstance(key, str):
#             raise KeyError(key)
#         return self[str(key)]
#
#     def get(self, key, default=None):
#         print(2)
#         try:
#             return self[key]
#         except KeyError:
#             return default
#
#     def __contains__(self, key):
#         print(3)
#         return key in self.keys() or str(key) in self.keys()


# d = StrKeyDict0([('2', 'two'), ('4', 'four')])
# print(d.get(3))

# a = [1,2,3,4,5,5,5,5,5,6,6,7,7,7,8,8,8,9,9,9,9,9,9,9]
# from collections import Counter
# print(Counter(a).most_common(100))

# from collections import ChainMap
# import os, argparse
#
# defaults = {'color': 'red', 'user': 'guest'}
#
# parser = argparse.ArgumentParser()
# parser.add_argument('-u', '--user')
# parser.add_argument('-c', '--color')
# namespace = parser.parse_args()
# command_line_args = {k: v for k, v in vars(namespace).items() if v}
# combined = ChainMap(command_line_args, os.environ, defaults)
# print(combined['color'])
# print(combined['user'])

from collections import UserDict


class StrKeyDict(UserDict):
    def __missing__(self, key):
        print(1)
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        print(2)
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item


d = StrKeyDict([('2', 'two'), ('4', 'four'), ('5', 'five')])
