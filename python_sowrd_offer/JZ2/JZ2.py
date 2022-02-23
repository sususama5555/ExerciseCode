# -*- coding: utf-8 -*-
"""
@File  :JZ2.py
@Author:Sapphire
@Date  :2021/1/7 23:26
@Desc  :替换空格
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""


class Solution:
    # s 源字符串
    def replaceSpace(self, pre_s):
        return pre_s.replace(" ", "%20")

    def replaceSpace_s(self, pre_s):
        res_s = ""
        for char in pre_s:
            if char == " ":
                res_s += "%20"
            else:
                res_s += char
        return res_s
