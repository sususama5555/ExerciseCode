# -*- coding: utf-8 -*-
"""
@File  :JZ35_MergeSort.py
@Author:Sapphire
@Date  :2020/10/9 0:31
@Desc  :数组中的逆序对：
题干：
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组，求出这个数组中的逆序对的总数P，并将P对1000000007取模的结果输出，即输出P%1000000007
思路：
todo 归并排序的算法解析
"""


class Solution:
    """
    使用归并排序的思路求解
    """

    def InversePairs(self, data):
        if len(data) > 1:
            # tips:python2中，n / m为整数，python3中为小数
            mid = len(data) // 2
            left_half = data[:mid]
            right_half = data[mid:]
            left_count = self.InversePairs(left_half) % 1000000007
            right_count = self.InversePairs(right_half) % 1000000007
            i, j, k, count = len(left_half) - 1, len(right_half) - 1, len(data) - 1, 0
            while i >= 0 and j >= 0:
                if left_half[i] < right_half[j]:
                    data[k] = right_half[j]
                    j = j - 1
                    k = k - 1
                else:
                    data[k] = left_half[i]
                    count += (j + 1)
                    i = i - 1
                    k = k - 1
            while i >= 0:
                data[k] = left_half[i]
                k = k - 1
                i = i - 1
            while j >= 0:
                data[k] = right_half[j]
                k = k - 1
                j = j - 1
            return (count + left_count + right_count) % 1000000007
        else:
            return 0


array = [364, 637, 341, 406, 747, 995, 234, 971, 571, 219, 993, 407, 416, 366, 315, 301, 601, 650, 418, 355, 460, 505,
         360, 965, 516, 648, 727, 667, 465, 849, 455, 181, 486, 149, 588, 233, 144, 174, 557, 67, 746, 550, 474, 162,
         268, 142, 463, 221, 882, 576, 604, 739, 288, 569, 256, 936, 275, 401, 497, 82, 935, 983, 583, 523, 697, 478,
         147, 795, 380, 973, 958, 115, 773, 870, 259, 655, 446, 863, 735, 784, 3, 671, 433, 630, 425, 930, 64, 266, 235,
         187, 284, 665, 874, 80, 45, 848, 38, 811, 267, 575]
solution = Solution()
print(solution.InversePairs(array))
