# -*- coding: utf-8 -*-
"""
@File  :JZ7.py
@Author:Sapphire
@Date  :2020/9/14 15:12
@Desc  :斐波那契数列，求第n项
"""


class Solution:
    def Fibonacci(self, n):
        # 使用两个数字，只保留斐波那契最近两个数
        # write code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        n_0 = 0
        n_1 = 1
        result = 0
        for i in range(1, n):
            result = n_0 + n_1
            n_0, n_1 = n_1, result
        return result

    def Fibonacci_total(self, n: int) -> int:
        # 保留全部斐波那契数列
        # write code here
        fib_nums = [1, 1]
        for i in range(2, n):
            fib_nums.append(fib_nums[i - 1] + fib_nums[i - 2])
        return fib_nums[-1]

    def Fibonacci_recursion(self, n):
        # 递归比较慢
        # write code here
        if n <= 2:
            return 1
        return self.Fibonacci(n - 1) + self.Fibonacci(n - 2)


solution = Solution()
print(solution.Fibonacci(10))
