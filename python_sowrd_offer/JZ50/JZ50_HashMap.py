# -*- coding: utf-8 -*-
"""
@File  :JZ50_HashMap.py
@Author:Sapphire
@Date  :2020/10/27 1:02
@Desc  :数组中重复的数字：
题干：
给定一个长度为n的数组，数据范围在0-n-1，找到第一个重复的数字。
思路：哈希（或set） + 遍历
时间复杂度：O(N)
空间复杂度：O(N)
"""


class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        hash_map = {}
        for num in numbers:
            if hash_map.get(num):
                duplication[0] = num
                return True
            else:
                hash_map[num] = 1
        return False
