# -*- coding: utf-8 -*-
"""
@File  :JZ8_1.py
@Author:Sapphire
@Date  :2020/9/14 11:48
@Desc  :跳台阶：
一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
"""
import time
from functools import wraps


def time_counter(function):
    """
    迭代法、变形斐波那契数列，耗时短
    """
    @wraps(function)
    def function_timer(*args, **kwargs):
        t_0 = time.time()
        result = function(*args, **kwargs)
        t_1 = time.time()
        print("Total time running {}: {} seconds".format(function, str(t_1 - t_0)))
        return result

    return function_timer


# 跳台阶：迭代法
# 斐波那契数列，时间短
class Solution:
    @time_counter
    def jumpFloor(self, number):
        if number < 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        result = [1, 2]
        for i in range(2, number):
            result.append(result[i - 1] + result[i - 2])
        return result[-1]


solution = Solution()
print(solution.jumpFloor(10))
