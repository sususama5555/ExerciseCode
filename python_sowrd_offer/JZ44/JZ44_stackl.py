# -*- coding: utf-8 -*-
"""
@File  :JZ44_string_wheel.py
@Author:Sapphire
@Date  :2020/10/15 23:03
@Desc  :翻转单词顺序列：
题干：
例如，“student. a am I”翻转为“I am a student.”
思路：使用堆栈思想：
push and pop
"""


class Solution:
    def ReverseSentence(self, s):
        # write code here
        stack = s.split(" ")
        res = ""
        while stack:
            res += stack.pop() + " "
        return res[:-1]

    def ReverseSentence_else(self, s):
        # write code here
        s_list = s.split(" ")
        stack = []
        for i in range(len(s_list)):
            stack.append(s_list.pop())
        return " ".join(stack)


sample = "student. a am I"
solution = Solution()
print(solution.ReverseSentence(sample))
