# -*- coding: utf-8 -*-
"""
@File  :JZ8_2.py
@Author:Sapphire
@Date  :2020/9/14 11:48
@Desc  :跳台阶
"""


class Solution:
    """
    解法二：
    递归法、动态规划，耗时长
    """
    def jumpFloor(self, number):
        # write code here
        if number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            return self.jumpFloor(number - 1) + self.jumpFloor(number - 2)


solution = Solution()
print(solution.jumpFloor(30))
