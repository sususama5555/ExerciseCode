# -*- coding: utf-8 -*-
"""
@File  :JZ30_simple.py
@Author:Sapphire
@Date  :2020/10/4 22:38
@Desc  :连续子数组的最大和：最优解
如果数组里所有的整数都是负数，那么选择最大的数即可，因为越累加越小。
正负数都有的情况，需要两个变量，
一个是global_max，从全局来看，每次最大的是什么组合，
另一个是local_max，和global_max相比，更新global_max。
"""


class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if max(array) < 0:
            return max(array)
        local_max, global_max = 0, 0
        for i in array:
            # 如果之前的和为正，则保持结果；为负，则置0并重新累计
            local_max = max(0, local_max + i)
            global_max = max(global_max, local_max)
        return global_max

        # 另一种：动态规划
        # n = len(array)
        # dp = [i for i in array]
        # for i in range(1, n):
        #     dp[i] = max(dp[i - 1] + array[i], array[i])
        #
        # return max(dp)


array = [1, -2, 3, 10, -4, 7, 2, -5]
solution = Solution()
print(solution.FindGreatestSumOfSubArray(array))
