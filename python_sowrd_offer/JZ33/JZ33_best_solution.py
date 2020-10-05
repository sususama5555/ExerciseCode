# -*- coding: utf-8 -*-
"""
@File  :JZ33_best_solution.py
@Author:Sapphire
@Date  :2020/10/5 22:14
@Desc  :丑数：
题干：把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
最优解：动态规划的解法，首先确保数组里的已有的丑数是排好序的，同时要维护三个索引。
"""


class Solution:
    def GetUglyNumber_Solution(self, index):
        if index <= 0:
            return 0
        res = [1]
        a = b = c = 0
        while len(res) < index:
            nextMin = min(res[a] * 2, res[b] * 3, res[c] * 5)
            res.append(nextMin)
            while res[a] * 2 == nextMin:
                a += 1
            while res[b] * 3 == nextMin:
                b += 1
            while res[c] * 5 == nextMin:
                c += 1
        return res[-1]


solution = Solution()
print(solution.GetUglyNumber_Solution(1500))
