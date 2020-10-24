# -*- coding: utf-8 -*-
"""
@File  :JZ49.py
@Author:Sapphire
@Date  :2020/10/25 1:10
@Desc  :把字符串转换成整数：
题干：
将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0
思路：
判断第一位的正负，然后 sum * 10 + numlist.index(string) 或者 sum * 10 + int(string) 循环求和
"""


class Solution:
    def StrToInt(self, s):
        # write code here
        if s == '':
            return 0
        numlist = [str(num) for num in range(10)]
        sum = 0
        label = 1
        if s[0] == '+':
            s = s[1:]
        elif s[0] == '-':
            label = -1
            s = s[1:]
        for string in s:
            if string not in numlist:  # 非合法字符
                return 0
            if string in numlist:  # 如果是合法字符
                sum = sum * 10 + numlist.index(string)
        return sum * label


s = '+2147483647'
solution = Solution()
print(solution.StrToInt(s))
