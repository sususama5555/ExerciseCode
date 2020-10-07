# -*- coding: utf-8 -*-
"""
@File  :JZ34_hash.py
@Author:Sapphire
@Date  :2020/10/7 23:30
@Desc  :第一个只出现一次的字符：
题干：
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符，
并返回它的位置，如果没有则返回 -1（需要区分大小写）.（从0开始计数）
思路：
创建哈希表，下标为ASCII值，值为出现次数：
利用每个字母的ASCII码作hash来作为数组的index。首先用一个58长度的数组来存储每个字母出现的次数，
长度58主要是由于A-Z对应的ASCII码为65-90，a-z对应的ASCII码值为97-122，而每个字母的index=int(word)-65，
而数组中具体记录的内容是该字母出现的次数，最终遍历一遍字符串，找出第一个数组内容为1的字母就可以了，
时间复杂度为 O(n)。
tips：

"""


class Solution:
    def FirstNotRepeatingChar_list(self, s):
        """
        使用list进行hash，使用字符串的ASCII做list的索引
        :param s:
        :return:
        """
        # write code here
        ls = [0] * 58
        # 遍历字符串,下标为ASCII值,值为次数
        for i in s:
            ls[ord(i) - 65] += 1  # ord()函数以一个字符作为参数，返回对应的ASCII数值
        for j in s:
            if ls[ord(j) - 65] == 1:
                return s.find(j)
        return -1

    def FirstNotRepeatingChar_dict(self, s):
        """
        使用python的字典hash => {"a": 3, "b":1, ......}
        :param s:
        :return:
        """
        # write code here
        d = dict()
        # 第一次遍历字符串，将每个字符的次数存入字典
        for i in s:
            d[i] = d.get(i, 0) + 1
        # 第二次遍历字符串，检查每个字符出现的次数
        for i in s:
            if d[i] == 1:  # O(1)
                return s.index(i)
        return -1


solution = Solution()
print(solution.FirstNotRepeatingChar_list("google"))
