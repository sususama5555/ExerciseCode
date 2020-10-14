# -*- coding: utf-8 -*-
"""
@File  :JZ43_slice.py
@Author:Sapphire
@Date  :2020/10/15 1:00
@Desc  :左旋转字符串：
题干：
汇编语言中有一种移位指令叫做循环左移（ROL），
现在有个简单的任务，就是用字符串模拟这个指令的运算结果。
对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。例
如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。
思路：python切片：
将需要移到尾部的部分表示为[:n]
不动的部分表示为[n:]
结果则为[n:] + [:n]
tips:python切片不会越界
时间复杂度：O(N)
空间复杂度：O(N)
"""


class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        s_left = s[:n]
        s_right = s[n:]
        return s_right + s_left


s_test = "abcXYZdef"
solution = Solution()
print(solution.LeftRotateString(s_test, n=3))

