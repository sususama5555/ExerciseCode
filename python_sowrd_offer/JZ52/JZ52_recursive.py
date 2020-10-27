# -*- coding: utf-8 -*-
"""
@File  :JZ52_recursive.py
@Author:Sapphire
@Date  :2020/10/28 1:11
@Desc  :正则表达式匹配：
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，
而'*'表示它前面的字符可以出现任意次（包含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配。
思路：TODO 如果 s和pattern都为空，匹配成功。
当模式中的第二个字符不是*时：（1）如果字符串第一个字符和模式中的第一个字符相匹配，那么字符串和模式都后移一个字符，然后匹配剩余的；（2）如果字符串第一个字符和模式中的第一个字符相不匹配，直接返回false。
而当模式中的第二个字符是*时：（1）模式后移2字符，相当于x*被忽略；（2）字符串后移1字符，模式后移2字符。
reference：https://zhuanlan.zhihu.com/p/74641093

"""


class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        if s == pattern:
            return True
        if len(pattern) > 1 and pattern[1] == '*':
            if s and (s[0] == pattern[0] or pattern[0] == '.'):
                return self.match(s, pattern[2:]) or self.match(s[1:], pattern)
            else:
                return self.match(s, pattern[2:])
        elif s and pattern and (s[0] == pattern[0] or pattern[0] == '.'):
            return self.match(s[1:], pattern[1:])
        return False
