# -*- coding: utf-8 -*-
"""
@File  :selection_sort.py
@Author:Sapphire
@Date  :2020/12/13 21:34
@Desc  :选择排序：
时间复杂度：O(n2)
空间复杂度：O(1)
"""


def selection_sort(array):
    """
    选择排序：
    第一次从待排序的数据元素中选出最小（或最大）的一个元素，存放在序列的起始位置，
    然后再从剩余的未排序元素中寻找到最小（大）元素，然后放到已排序的序列的末尾。
    以此类推，直到全部待排序的数据元素的个数为零。
    """
    # 最后一个元素不需要排序
    for i in range(len(array) - 1):
        min_index = i
        # 与i之后的元素对比
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


array = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
print(selection_sort(array))
