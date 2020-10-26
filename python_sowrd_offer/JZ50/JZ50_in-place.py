# -*- coding: utf-8 -*-
"""
@File  :JZ50_in-place.py
@Author:Sapphire
@Date  :2020/10/27 0:57
@Desc  :数组中重复的数字：
题干：in-place算法（利用 '数字都在0到n-1的范围内' 条件）
给定一个长度为n的数组，数据范围在0-n-1，找到第一个重复的数字。
思路：
数据的范围是0-n-1。所以我们可以这么做：
1、设置一个指针i指向开头0，
2、对于arr[i]进行判断，如果arr[i] == i，说明下标为i的数据正确的放在了该位置上，让i++
3、如果arr[i] != i， 说明没有正确放在位置上，那么我们就把arr[i]放在正确的位置上，也就是交换 arr[i] 和arr[arr[i]]。交换之后，如果arr[i] ！= i，继续交换。
如果交换的过程中，arr[i] == arr[arr[i]]，说明遇到了重复值，返回即可。

时间复杂度：O(N)
空间复杂度：O(1)
"""

class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        for i in range(len(numbers)):
            while numbers[i] != i:
                m = numbers[i]
                if numbers[m] == numbers[i]:
                    duplication[0] = m
                    return True
                else:
                    numbers[i] = numbers[m]
                    numbers[m] = m
        return False