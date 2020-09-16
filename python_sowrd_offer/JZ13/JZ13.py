# -*- coding: utf-8 -*-
"""
@File  :JZ13.py
@Author:Sapphire
@Date  :2020/9/15 15:30
@Desc  :调整数组顺序使奇数位于偶数前面：
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
python快捷轮子：善用lambda:x, x和sorted(iterable, key=None, reverse=False)
（区别于list.sort，后者只能用于list，改变当前的list）
return sorted(array, key=lambda c:c%2, reverse=True)
"""


class Solution:
    """
    考察列表
    """

    def reOrderArray(self, array):
        # write code here
        odd_list = []
        even_list = []
        for i in array:
            if not i % 2:
                odd_list.append(i)
            else:
                even_list.append(i)
        return even_list + odd_list


solution = Solution()
print(solution.reOrderArray([2, 1, 4, 6, 8, 9, 7]))
