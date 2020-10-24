# -*- coding: utf-8 -*-
"""
@File  :JZ47_recursive.py
@Author:Sapphire
@Date  :2020/10/22 0:02
@Desc  :题干：
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
思路：递归（实现循环） + 逻辑运算符（实现 if 终止条件）
tips：
终止条件为 if (n==0) return 0
需要当n==0，终止递归，所以可以使用逻辑与&&连接符。
A&&B，表示如果A成立则执行B，否则如果A不成立，不用执行B
因此我们可以这样。在 n>0 的时候，执行递归函数。
python example：
bool(True) and n = n
bool(False) and n = bool
"""


class Solution:
    def Sum_Solution(self, n):
        # write code here
        return n and self.Sum_Solution(n - 1) + n
