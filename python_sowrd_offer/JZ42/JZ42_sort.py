# -*- coding: utf-8 -*-
"""
@File  :JZ42_sort.py
@Author:Sapphire
@Date  :2020/10/14 0:30
@Desc  :和为S的两个数字：
题干：输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
思路：hash | 遍历数组
"""


class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        res_list = []
        for i in array:
            j = tsum - i
            if j in array:
                res_list.append([i, j])
        return sorted(res_list, key=lambda x: x[0] * x[1])[0] if res_list else []


    def FindNumbersWithSum_simple(self, array, tsum):
        # write code here
        for i in array:
            j = tsum - i
            if j in array:
                return [i, j]
        return []


solution = Solution()
print(solution.FindNumbersWithSum([1, 2, 4, 7, 11, 15], 15))
