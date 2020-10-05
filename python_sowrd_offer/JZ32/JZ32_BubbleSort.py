# -*- coding: utf-8 -*-
"""
@File  :JZ32_BubbleSort.py
@Author:Sapphire
@Date  :2020/10/5 21:18
@Version: Python3.6.7
@Desc  :把数组排成最小的数：
题干：输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
思路：
使用冒泡排序，将符合 x + y > y + x 条件的（x，y为转化为字符串的数组元素），交换在数组中的位置
todo 冒泡排序的时间复杂度为 O(n**2)，使用复杂度低的排序（快速排序、堆排序等）
"""


class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not len(numbers):
            return ""
        numbers = list(map(str, numbers))
        cmp = lambda x, y: x + y > y + x
        for i in range(len(numbers)):
            for j in range(len(numbers) - 1):
                if cmp(numbers[j], numbers[j + 1]):
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        return "".join(numbers)

    def PrintMinNumber_fake(self, numbers):
        # write code here
        if not len(numbers):
            return ""
        numbers = list(map(str, numbers))
        cmp = lambda x, y: x + y > y + x
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if cmp(numbers[i], numbers[j]):
                    numbers[i], numbers[j] = numbers[j], numbers[i]
        return "".join(numbers)


array = [3, 5, 1, 4, 2, 7, 12, 32, 10]
solition = Solution()
print(solition.PrintMinNumber(array))
print(solition.PrintMinNumber_fake(array))
