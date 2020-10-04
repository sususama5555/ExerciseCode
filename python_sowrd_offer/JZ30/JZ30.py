# -*- coding: utf-8 -*-
"""
@File  :JZ30.py
@Author:Sapphire
@Date  :2020/10/4 22:16
@Desc  :最小的K个数：
将每一种 连续子序列的和 都计算出来，然后比较大小（时间、空间复杂度较高）
"""


class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if max(array) < 0:
            return max(array)
        local_max, global_max = 0, 0
        for i in array:
            local_max = max(0, local_max + i)
            global_max = max(global_max, local_max)
        return global_max


array = [1, -2, 3, 10, -4, 7, 2, -5]
solution = Solution()
print(solution.FindGreatestSumOfSubArray(array))
