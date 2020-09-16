# -*- coding: utf-8 -*-
"""
@File  :JZ9.py
@Author:Sapphire
@Date  :2020/9/14 15:18
@Desc  :变态跳台阶：
一只青蛙一次可以跳上1级台阶，
也可以跳上2级……它也可以跳上n级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""


class Solution:
    """
    思路：假设到了n级台阶，我们可以从n-1级一步跳上来，也可以不经过n-1级跳上来，所以f(n)=2*f(n-1)。
    推公式也能得出：
    n = n时：f(n) = f(n-1)+f(n-2)+...+f(n-(n-1)) + f(n-n) = f(0) + f(1) + f(2) + ... + f(n-1)
    由于f(n-1) = f(0)+f(1)+f(2)+ ... + f((n-1)-1) = f(0) + f(1) + f(2) + f(3) + ... + f(n-2)
    所以f(n) = f(n-1)+f(n-1)=2*f(n-1)
    """
    def jumpFloorII(self, number):
        # write code here
        result = [1]
        for i in range(1, number):
            result.append(2*result[i-1])
        return result[-1]


solution = Solution()
print(solution.jumpFloorII(10))
