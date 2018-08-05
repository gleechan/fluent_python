#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright jitui 2018
#
# @author: chenyongjian@jituia.com
#
# a, b, *test = range(5)
# print(test)

# a, b, *test = range(3)
# print(a, b, test)

# a, b, *test = range(2)
# print(a, b, test)

a, *head, b = range(5)
print(a, b, head)


