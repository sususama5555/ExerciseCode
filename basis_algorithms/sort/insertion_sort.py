# -*- coding: utf-8 -*-
"""
@File  :insertion_sort.py
@Author:Sapphire
@Date  :2020/12/13 21:55
@Desc  :插入排序：
1.从第一个元素开始，该元素可以认为已经被排序；
2.取出下一个元素，在已经排序的元素序列中从后向前扫描；
3.如果该元素（已排序的）大于新元素，将该元素往右移到下一位置，重复该步骤，直到找到已排序的元素小于或者等于新元素的位置；
4.将新元素插入到步骤 3 找到的位置的后面；
5.重复步骤 2 ~ 4。
"""


def insertion_sort(array):
    for i in range(1, len(array)):  # 将 i 看做摸到的牌的下标
        tmp = array[i]  # 将摸到的牌储存到 tmp
        j = i - 1  # 将 j 看做手里的牌的下标
        while j >= 0 and array[j] > tmp:  # 如果手里的牌大于摸到的牌
            array[j + 1] = array[j]  # 将手里的牌往右移一个位置（将手里的牌赋值给下一个位置）
            j -= 1  # 将手里的牌的下标减 1，再次准备与摸到的牌进行比较
        array[j + 1] = tmp  # 将摸到的牌插入到 j+1 位置
    return array


test_case_1 = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
print(insertion_sort(test_case_1))
