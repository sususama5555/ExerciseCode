# -*- coding: utf-8 -*-
"""
@File  :JZ34_str.find.py
@Author:Sapphire
@Date  :2020/10/7 23:08
@Desc  :第一个只出现一次的字符：
题干：
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符，
并返回它的位置，如果没有则返回 -1（需要区分大小写）.（从0开始计数）
思路：
str.find(str, beg=0, end=len(string))
find() 方法检测字符串中是否包含子字符串 str ，
如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，
如果指定范围内如果包含指定索引值，返回的是索引值在字符串中的起始位置。
如果不包含索引值，返回-1。
str.index(str, beg=0, end=len(string))，该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常。
python内置方法find与index会极大减少难度，不建议使用。
"""


class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        """
        使用了内置方法str.count()和str.index()
        :param s:
        :return:
        """
        for i in s:
            if s.count(i) == 1:
                return s.index(i)
        return -1

    def FirstNotRepeatingChar_1(self, s):
        """
        缺点：如果不存在只出现一次的数，越界
        :param s:
        :return:
        """
        return [i for i in range(len(s)) if s.count(s[i]) == 1][0] if s else -1

    def FirstNotRepeatingChar_2(self, s):
        """
        同上
        :param s:
        :return:
        """
        return s.index(list(filter(lambda c:s.count(c)==1,s))[0]) if s else -1


solution = Solution()
print(solution.FirstNotRepeatingChar("google"))
