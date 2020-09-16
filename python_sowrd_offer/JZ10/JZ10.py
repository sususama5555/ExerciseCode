# -*- coding: utf-8 -*-
"""
@File  :JZ10.py
@Author:Sapphire
@Date  :2020/9/14 18:34
@Desc  :矩形覆盖：
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
"""


class Solution:
    """
    假设到了n，那么上一步就有两种情况：
    在n-1的时候，竖放一个矩形，或者在n-2时，横放两个矩形，
    所以总数是f(n)=f(n-1)+f(n-2)。
    时间复杂度O(n)。和跳台阶题一样。
    """
    def rectCover(self, number):
        if number in range(3):
            return number
        result = [1, 2]
        for i in range(2, number):
            result.append(result[-1] + result[-2])
        return result[-1]


solution = Solution()
print(solution.rectCover(5))
