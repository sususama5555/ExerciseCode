# -*- coding: utf-8 -*-
"""
@File  :bubble_sort.py
@Author:Sapphire
@Date  :2020/12/12 0:01
@Desc  :冒泡排序：
时间复杂度：O(n2)
空间复杂度：O(1)
"""


def bubble_sort(array):
    """传统冒泡排序"""
    loop = len(array) - 1
    for i in range(loop):
        for j in range(loop - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def bubble_sort_opt(array):
    """
    冒泡排序优化：
    立一个 flag，当某一趟序列遍历中元素没有发生交换，则证明该序列已经有序，就不再进行后续的排序
    """
    loop = len(array) - 1
    for i in range(loop):
        flag = False
        for j in range(loop - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = True
            if not flag:
                return array
    return array


array = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
print(bubble_sort(array))
print(bubble_sort_opt(array))
