# -*- coding: utf-8 -*-
"""
@File  :JZ29.py
@Author:Sapphire
@Date  :2020/10/1 23:59
@Desc  :最小的K个数：
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。
方法一：
Timsort：蒂姆排序：
使用python内置的tim排序（底层是快排等）
不推荐使用
todo 堆排序：循环列表，把最小的K个数放在堆里面
"""


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput or k > len(tinput):
            return []
        tinput.sort()
        return tinput[:k]
