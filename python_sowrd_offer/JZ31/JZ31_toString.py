# -*- coding: utf-8 -*-
"""
@File  :JZ31_toString.py
@Author:Sapphire
@Date  :2020/10/4 23:10
@Desc  :从1到n的整数中1出现的个数：
例如：1~13中包含1的数字有1、10、11、12、13，因此共出现6次
方法二：转化为字符串（或列表），判断 "1" 的个数（需要用到内置count方法）
"""


class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        count = 0
        for i in range(1, n + 1):
            count += str(i).count("1")
        return count
        # 一行解决：使用map得出所有数字的字符串列表，用join连接所有数字，并计算出1的个数
        # return ''.join(map(str, range(n + 1))).count('1')


solution = Solution()
print(solution.NumberOf1Between1AndN_Solution(13))
