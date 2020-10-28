# -*- coding: utf-8 -*-
"""
@File  :JZ54_HashMap.py
@Author:Sapphire
@Date  :2020/10/29 0:14
@Desc  :字符流中第一个不重复的字符
题干：
请实现一个函数用来找出字符流中第一个只出现一次的字符。
例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
如果当前字符流没有存在出现一次的字符，返回#字符。
思路：哈希法
用一个字典保存下出现过的字符，以及字符出现的次数。
除保存出现的字符之外，我们用一个字符数组保存出现过程字符顺序，如果不保存插入的char的话，我们可以遍历ascii码中的字符。
"""


class Solution:
    # 返回对应char
    def __init__(self):
        self.s = ""
        self.hash_map = {}
    def FirstAppearingOnce(self):
        for i in self.s:
            if self.hash_map[i]==1:
                return i
        return '#'
    # write code here
    def Insert(self, char):
        # write code here
        self.s += char
        if char in self.hash_map:
            self.hash_map[char] += 1
        else:
            self.hash_map[char] = 1
