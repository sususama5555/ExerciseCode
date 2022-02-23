# -*- coding: utf-8 -*-
"""
@File  :JZ1.py
@Author:Sapphire
@Date  :2021/1/7 23:06
@Desc  :二维数组中的查找
在一个二维数组中（每个一维数组的长度相同），
每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""


class Solution:
    def find(self, target, array):
        row = len(array) - 1
        col = len(array[0]) - 1
        i = row
        j = 0
        while i >= 0 and j <= col:
            if array[i][j] > target:
                i -= 1
            elif array[i][j] < target:
                j += 1
            else:
                return True
        return False

    def find_opt(self, target, array):
        row = len(array) - 1
        col = len(array[0]) - 1
        i = 0
        j = col
        while i <= row and j >= 0:
            if array[i][j] > target:
                j -= 1
            elif array[i][j] < target:
                i += 1
            else:
                return True
        return False


test_case = [
    [1, 2, 3, 34, 55, 100],
    [3, 6, 7, 55, 100, 101],
    [5, 9, 10, 66, 102, 104],
    [15, 20, 30, 86, 222, 344],
]

test_target = 102

solution = Solution()
print(solution.find(test_target, test_case))
print(solution.find_opt(test_target, test_case))
