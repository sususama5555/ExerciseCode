# -*- coding: utf-8 -*-
"""
@File  :JZ11_test.py
@Author:Sapphire
@Date  :2020/9/14 18:45
@Desc  :二进制中 1 的个数：自己写的新方法
"""


class Solution:
    def NumberOf1(self, n):
        # write code here
        if n < 0:
            n = n & 0xffffffff
        if n == 0:
            return 0
        tmp = 1
        for i in range(32):
            if n == 1:
                break
            if n % 2:
                tmp += 1
            n = int(n / 2)
        return tmp


solution = Solution()
print(solution.NumberOf1(-2147483648))
