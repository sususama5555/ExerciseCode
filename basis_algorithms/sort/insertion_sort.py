# -*- coding: utf-8 -*-
"""
@File  :insertion_sort.py
@Author:Sapphire
@Date  :2020/12/13 21:55
@Desc  :插入排序：
"""


def insertion_sort(array):
    for i in range(1, len(array)):  # 将 i 看做摸到的牌的下标
        tmp = array[i]              # 将摸到的牌储存到 tmp
        j = i - 1                   # 将 j 看做手里的牌的下标
        while j >= 0 and array[j] > tmp:    # 如果手里的牌大于摸到的牌
            array[j + 1] = array[j]     # 将手里的牌往右移一个位置（将手里的牌赋值给下一个位置）
            j -= 1                  # 将手里的牌的下标减 1，再次准备与摸到的牌进行比较
        array[j + 1] = tmp          # 将摸到的牌插入到 j+1 位置
    return array


array = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
print(insertion_sort(array))
