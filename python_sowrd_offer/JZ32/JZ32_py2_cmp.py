# -*- coding: utf-8 -*-
"""
@File  :JZ32_py2_cmp.py
@Author:Sapphire
@Date  :2020/10/5 20:16
@Version: Python2.7.5
@Desc  :把数组排成最小的数：
题干：输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
思路：两个数字m和n能拼接成数字mn和nm，
如果mn<nm，也就是m应该拍在n的前面，我们定义此时m小于n；反之，如果nm<mn，我们定义n小于m；如果mn=nm，m等于n。
技巧：使用python2的 sort 或者 sorted 方法 中的 cmp 参数
优点：使用简单，功能契合
缺点：key 和 reverse 比一个等价的 cmp 函数处理速度要快。
这是因为对于每个列表元素，cmp 都会被调用多次，而 key 和 reverse 只被调用一次
todo python3中去除了 cmp 参数，使用python3解决
"""


class Solution:
    """
    使用python2中 list.sort(cmp=None, key=None, reverse=False)
    或者 sorted(iterable, cmp=None, key=None, reverse=False)
    方法中的 `cmp` 参数：
    cmp -- 比较的函数：这个具有两个参数，参数的值都是从可迭代对象中取出，
    此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0。
    """
    def PrintMinNumber(self, numbers):
        # write code here
        if not len(numbers):
            return ""
        arr = [str(x) for x in numbers]
        arr.sort(cmp=lambda x, y: cmp(x + y, y + x))
        return int("".join(arr))


array = [3, 5, 1, 4, 2]
solition = Solution()
print(solition.PrintMinNumber(array))
