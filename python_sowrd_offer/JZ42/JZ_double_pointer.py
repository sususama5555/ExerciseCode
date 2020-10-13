# -*- coding: utf-8 -*-
"""
@File  :JZ_double_pointer.py
@Author:Sapphire
@Date  :2020/10/14 0:37
@Desc  :和为S的两个数字：
题干：输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
思路：双指针（首尾夹逼）
由于是排好序的数组，因此对于和相等的两个数来说，相互之间的差别越大，那么乘积越小，
因此我们使用两个指针，一个从前往后遍历，另一个从后往前遍历数组即可。
具体解法：
设定指针i指向数组首， 指针j指向数组尾部
如果arr[i] + arr[j] == sum , 说明是可能解
如果arr[i] + arr[j] > sum, 说明和太大，所以--j
如果arr[i] + arr[j] < sum, 说明和太小，所以++i
时间复杂度：O(n)
空间复杂度：O(1)
最优解
"""


class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        res = []
        plow = 0
        phigh = len(array) - 1
        while plow < phigh:
            if array[plow] + array[phigh] > tsum:
                phigh -= 1
            elif array[plow] + array[phigh] < tsum:
                plow += 1
            else:
                res = [array[plow], array[phigh]]
                break
        return res