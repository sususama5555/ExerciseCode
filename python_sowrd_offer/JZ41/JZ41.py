# -*- coding: utf-8 -*-
"""
@File  :JZ41.py
@Author:Sapphire
@Date  :2020/10/13 0:34
@Desc  :和为S的连续正数序列：
题目抽象：给定一个1到sum的序列，求所有和为sum的连续序列。
"""


class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        ret_list = []
        for i in range(2, tsum):
            quotient = tsum // i
            tmp = i % 2
            if tsum % 2 and not quotient % 2:
                continue
            if tmp:
                tmp_list = [quotient-(i/2)+j for j in range(i)]
            else:
                tmp_list = [quotient-(i/2)+j for j in range(1, i+1)]
            ret_list.append(tmp_list)
        return ret_list


solution = Solution()
print(solution.FindContinuousSequence(4))


