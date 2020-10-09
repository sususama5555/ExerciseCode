# -*- coding: utf-8 -*-
"""
@File  :JZ37_binarySearch.py
@Author:Sapphire
@Date  :2020/10/10 0:00
@Desc  :数字在升序数组中出现的次数：
使用二分查找方法
二分的前提：有序（一提到有序，必须立马想到二分！）
由于数组有序，所以使用二分查找方法定位 k 的第一次出现位置和最后一次出现位置
时间复杂度：O(logN)
空间复杂度：O(1)
tips：使用 python count()函数 不可取，没有利用到升序的条件，时间复杂度高
"""


class Solution:
    def GetNumberOfK(self, data, k):
        """
        二分查找寻找上下界
        """
        # write code here
        l = 0
        r = len(data)
        # 寻找下界
        while l < r:
            mid = l + (r - l) // 2
            if data[mid] < k:
                l = mid + 1
            else:
                r = mid
        lbound = l
        l = 0
        r = len(data)
        # 寻找上界
        while l < r:
            mid = l + (r - l) // 2
            if data[mid] <= k:
                l = mid + 1
            else:
                r = mid
        rbound = l
        return rbound - lbound

    def GetNumberOfK_double_pointer(self, data, k):
        """
        考虑数组为空的情况，直接返回0；双指针，收尾开始遍历，求得上下界
        """
        if len(data) == 0:
            return 0
        i = 0
        j = len(data) - 1
        while i < j and data[i] != data[j]:
            if data[i] < k:
                i += 1
            if data[j] > k:
                j -= 1
        if data[i] != k:
            return 0
        return j - i + 1

    def GetNumberOfK_count(self, data, k):
        return data.count(k)
