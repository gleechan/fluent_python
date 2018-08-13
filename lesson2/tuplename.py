#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright jitui 2018
#
# @author: chenyongjian@jituia.com
#
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
# print(tokyo)

# print(City._fields)

LatLong = namedtuple('Latlong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
# print(delhi)
# delhi = City(*delhi_data)
# print(delhi._asdict())
# print(delhi._asdict().items())
# for key, value in reversed(delhi._asdict().items()):
for key, value in delhi._asdict().items():
    print(key + ':', value)
