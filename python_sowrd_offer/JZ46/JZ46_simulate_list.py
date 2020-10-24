# -*- coding: utf-8 -*-
"""
@File  :JZ46_simulate_list.py
@Author:Sapphire
@Date  :2020/10/21 23:49
@Desc  :孩子们的游戏（圆圈中最后剩下的数）:
题干：
游戏是这样的：首先，让小朋友们围成一个大圈。
然后，他随机指定一个数m，让编号为0的小朋友开始报数。
每次喊到m-1的那个小朋友要出列，不再回到圈中，从他的下一个小朋友开始，
继续0...m-1报数....这样下去....直到剩下最后一个小朋友获胜，
获胜的小朋友编号多少？(注：小朋友的编号是从0到n-1)
思路：模拟（数组）
使用堆栈模拟一个圈，每次将将抽出的数pop掉，直到最后一个数
TODO 1.递归
TODO 2.模拟（链表）
TODO 3.迭代
"""


class Solution:
    def LastRemaining_Solution(self, n, m):
        if not n and not m:
            return -1
        res = range(n)
        i = 0
        while len(res) > 1:
            i = (m + i - 1) % len(res)
            res.pop(i)
        return res[0]
