# -*- coding: utf-8 -*-
"""
@File  :JZ7.py
@Author:Sapphire
@Date  :2020/9/14 15:12
@Desc  :斐波那契数列，求第n项
"""


class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        n_0 = 0
        n_1 = 1
        result = 0
        for i in range(1, n):
            result = n_0 + n_1
            n_0 = n_1
            n_1 = result
        return result


solution = Solution()
print(solution.Fibonacci(10))
