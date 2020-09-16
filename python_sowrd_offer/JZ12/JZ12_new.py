# -*- coding: utf-8 -*-
"""
@File  :JZ12_new.py
@Author:Sapphire
@Date  :2020/9/14 23:03
@Desc  :数值的整数次方：新方法：判断正负再循环
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
保证base和exponent不同时为0
一步到位：使用pow(x, n)
"""


class Solution:
    """
    x*x*x...x 迭代相乘求幂，
    需要考虑指数为负数的情况，python中善用range
    """
    def Power(self, base, exponent):
        # write code here
        result = 1
        for i in range(exponent):
            result = result * base
        for i in range(exponent, 0):
            result = result * (1 / base)
        return result


solution = Solution()
print(solution.Power(2, -3))


