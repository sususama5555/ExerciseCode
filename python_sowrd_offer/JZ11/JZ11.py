# -*- coding: utf-8 -*-
"""
@File  :JZ11.py
@Author:Sapphire
@Date  :2020/9/14 22:29
@Desc  :二进制中 1 的个数：位运算
或者直接用轮子：bin(n).count('1')，直接返回二进制表示（限制于正数）
"""


class Solution:
    """
    一个整数减去1，都是把最右边的1变成0，如果它后面还有0，那么0变成1。
    那么我们把一个整数减去1，与该整数做位(与)运算，相当于把最右边的1变成了0，比如1100与1011做位与运算，得到1000。
    那么一个整数中有多少个1就可以做多少次这样的运算。
    python的负数需要特殊处理
    """
    def NumberOf1(self, n):
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            n = (n - 1) & n
            count += 1
        return count


solution = Solution()
print(solution.NumberOf1(-2147483648))
