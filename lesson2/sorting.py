#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright jitui 2018
#
# @author: chenyongjian@jituia.com
#
import bisect
import random

# def binary_search(the_array, item, start, end):
#     if start == end:
#         if the_array[start] > item:
#             return start
#         else:
#             return start + 1
#     if start > end:
#         return start
#
#     mid = round((start + end) / 2)
#
#     if the_array[mid] < item:
#         return binary_search(the_array, item, mid + 1, end)
#
#     elif the_array[mid] > item:
#         return binary_search(the_array, item, start, mid - 1)
#
#     else:
#         return mid
#
#
# """
# Insertion sort that timsort uses if the array size is small or if
# the size of the "run" is small
# """
#
#
# def insertion_sort(the_array):
#     l = len(the_array)
#     for index in range(1, l):
#         value = the_array[index]
#         pos = binary_search(the_array, value, 0, index - 1)
#         the_array = the_array[:pos] + [value] + the_array[pos:index] + the_array[index + 1:]
#     return the_array
#
#
# def merge(left, right):
#     """Takes two sorted lists and returns a single sorted list by comparing the
#     elements one at a time.
#     [1, 2, 3, 4, 5, 6]
#     """
#     if not left:
#         return right
#     if not right:
#         return left
#     if left[0] < right[0]:
#         return [left[0]] + merge(left[1:], right)
#     return [right[0]] + merge(left, right[1:])
#
#
# def timsort(the_array):
#     runs, sorted_runs = [], []
#     length = len(the_array)
#     new_run = [the_array[0]]
#
#     # for every i in the range of 1 to length of array
#     for i in range(1, length):
#         # if i is at the end of the list
#         if i == length - 1:
#             new_run.append(the_array[i])
#             runs.append(new_run)
#             break
#         # if the i'th element of the array is less than the one before it
#         if the_array[i] < the_array[i - 1]:
#             # if new_run is set to None (NULL)
#             if not new_run:
#                 runs.append([the_array[i]])
#                 new_run.append(the_array[i])
#             else:
#                 runs.append(new_run)
#                 new_run = [the_array[i]]
#         # else if its equal to or more than
#         else:
#             new_run.append(the_array[i])
#
#     # for every item in runs, append it using insertion sort
#     print(runs)
#     for item in runs:
#         sorted_runs.append(insertion_sort(item))
#
#     # for every run in sorted_runs, merge them
#     sorted_array = []
#     for run in sorted_runs:
#         sorted_array = merge(sorted_array, run)
#
#     print(sorted_array)
#
#
# timsort([5, 2, 1, 3, 8, 7, 15, 10])


#
# HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 26, 29, 30]
# NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
# ROW_FMT = '{0:2d} @ {1:2d}  {2}{0:<2d}'
#
#
# def demo(bisect_fn):
#     for needle in reversed(NEEDLES):
#         position = bisect_fn(HAYSTACK, needle)
#         offset = position * '    |'
#         print(ROW_FMT.format(needle, position, offset))
#
#
# if __name__ == '__main__':
#     if sys.argv[-1] == 'left':
#         bisect_fn = bisect.bisect_left
#     else:
#         bisect_fn = bisect.bisect
#
#     print('DEMO:', bisect_fn.__name__)
#     print('haystack ->', '   '.join('%2d' % n for n in HAYSTACK))
#     demo(bisect_fn)

# def grade(score, breakpoints=None, grades='FDCBA'):
#     if breakpoints is None:
#         breakpoints = [60, 70, 80, 90]
#     i = bisect.bisect(breakpoints, score)
#     return grades[i]
#
#
# print([grade(score) for score in [33, 99, 77, 89, 90, 100]])

SIZE = 7
random.seed(1729)
my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE * 2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)

