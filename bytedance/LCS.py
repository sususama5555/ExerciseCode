# -*- coding: utf-8 -*-
"""
@File  :LCS.py
@Author:Sapphire
@Date  :2021/1/10 4:15
@Desc  :最长公共子串 - LCS(The Longest Common Substring)
给定两个字符串str1和str2,输出两个字符串的最长公共子串，如果最长公共子串为空，输出-1。
思路：
LCS问题就是求两个字符串最长公共子串的问题。
解法就是用一个矩阵来记录两个字符串中所有位置的两个字符之间的匹配情况，是匹配则为1,否则为0。
然后求出对角线最长的1的序列，其对应的位置就是最长匹配子串的位置。
"""


#
# longest common substring
# @param str1 string字符串 the string
# @param str2 string字符串 the string
# @return string字符串
#
class Solution:
    def LCS(self, str1, str2):
        # write code here
        m = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]  # 生成0矩阵，为方便后续计算，比字符串长度多了一列
        mmax = 0
        p = 0
        for i in range(len(str1)):
            for j in range(len(str2)):
                if str1[i] == str2[j]:
                    m[i + 1][j + 1] = m[i][j] + 1
                    if m[i + 1][j + 1] > mmax:
                        mmax = m[i + 1][j + 1]
                        p = i + 1
        return str1[p - mmax:p], mmax


solution = Solution()
print(solution.LCS("1AB2345CD", "12345EF"))
