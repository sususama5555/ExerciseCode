# -*- coding: utf-8 -*-
"""
@File  :JZ12_new.py
@Author:Sapphire
@Date  :2020/9/14 23:03
@Desc  :数值的整数次方：
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
保证base和exponent不同时为0
一步到位：使用pow(x, n)
"""


class Solution:
    """
    快速幂算法，将底数x转化为二进制，使得x最后一位与tmp*tmp...tmp相乘，然后向左移位，最终结果相乘
    """
    def Power(self, base, exponent):
        if base == 0:
            return 0
        if exponent == 0:
            return 1
        e = abs(exponent)
        tmp = base
        res = 1
        while e > 0:
            # 如果最后一位为1，那么给res乘上这一位的结果
            if e & 1 == 1:
                res = res * tmp
            e = e >> 1
            tmp = tmp * tmp
        return res if exponent > 0 else 1 / res


solution = Solution()
print(solution.Power(2, -3))
