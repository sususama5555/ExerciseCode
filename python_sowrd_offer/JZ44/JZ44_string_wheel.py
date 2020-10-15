# -*- coding: utf-8 -*-
"""
@File  :JZ44_string_wheel.py
@Author:Sapphire
@Date  :2020/10/15 23:03
@Desc  :翻转单词顺序列：
题干：
例如，“student. a am I”翻转为“I am a student.”
思路：python字符串、列表处理
利用python的字符串、列表的内置函数，实现功能。
str.split("s")
list or string 切片slice [n:m:p]  p =-1 时反转
"s".join(list) 数组元素按照 s 依次连接
"""


class Solution:
    def ReverseSentence(self, s):
        # write code here
        return " ".join(s.split(" ")[::-1])


sample = "student. a am I"
solution = Solution()
print(solution.ReverseSentence(sample))
