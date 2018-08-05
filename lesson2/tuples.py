#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright jitui 2018
#
# @author: chenyongjian@jituia.com
#
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
# for passport in sorted(traveler_ids):
#     print('%s/%s' % passport)

for country, _ in traveler_ids:
    print(country)

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889))
]

print('{:9} | {:7} | {:9}'.format('city.', 'lat.', 'long.'))
fmt = '{:9} | {:7.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude >= 0:
        print(fmt.format(name, latitude, longitude))

