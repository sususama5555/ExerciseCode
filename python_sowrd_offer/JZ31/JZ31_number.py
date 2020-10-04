# -*- coding: utf-8 -*-
"""
@File  :JZ31_number.py
@Author:Sapphire
@Date  :2020/10/4 23:11
@Desc  :从1到n的整数中1出现的个数：
例如：1~13中包含1的数字有1、10、11、12、13，因此共出现6次
方法一：使用数字的处理
"""


class Solution:
    """
    判断 1 的个数时，使用 %10 取余数判断，然后取 /10 进行下一次哦按段
    """
    def NumberOf1Between1AndN_Solution(self, n):
        count = 0
        for i in range(1, n + 1):
            j = i
            while j > 0:
                if j % 10 == 1:
                    count += 1
                j = j / 10
        return count

solution = Solution()
print(solution.NumberOf1Between1AndN_Solution(13))
