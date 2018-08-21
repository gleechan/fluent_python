#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright jitui 2018
#
# @author: chenyongjian@jituia.com
#
from array import array

from random import random


floats = array('d', (random() for i in range(10**7)))
fp = open('files/floats.bin', 'wb')
floats.tofile(fp)
fp.close()
floats2 = array('d')
fp = open('files/floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
print(floats2 == floats)
print(floats2.typecode)

# numbers = array('h', [-2, -1, 0, 1, 2])
# menv = memoryview(numbers)
# menv.tolist()
# memv_oct = menv.cast('B')
# print(memv_oct.tolist())
