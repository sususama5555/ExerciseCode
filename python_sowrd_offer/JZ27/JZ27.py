# -*- coding: utf-8 -*-
"""
@File  :JZ27.py
@Author:Sapphire
@Date  :2020/9/30 0:55
@Desc  :字符串的排序
递归：
把字符串分为两个部分： 字符串的第一个字符，第一个字符后面的所有字符。
1.求所有可能出现在第一个位置的字符，用索引遍历。
2.求第一个字符以后的所有字符的全排列。将后面的字符又分成第一个字符以及剩余字符。
"""


class Solution:
    def __init__(self):
        self.sort_list = []

    def Permutation(self, ss):
        # write code here
        if not ss:
            return ss
        self.helper(ss, "")
        return self.sort_list

    def helper(self, ss, result):
        if not ss:
            self.sort_list.append(result)
        else:
            for i, j in enumerate(ss):
                self.helper(ss[:i] + ss[i + 1:], result + j)


solution = Solution()
print(solution.Permutation("abc"))
