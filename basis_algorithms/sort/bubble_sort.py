# -*- coding: utf-8 -*-
"""
@File  :bubble_sort.py
@Author:Sapphire
@Date  :2020/12/12 0:01
@Desc  :
"""


def bubble_sort(array):
    loop = len(array) - 1
    for i in range(loop):
        for j in range(loop - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


array = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
print(bubble_sort(array))
