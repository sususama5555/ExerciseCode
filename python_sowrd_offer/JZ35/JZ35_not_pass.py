# -*- coding: utf-8 -*-
"""
@File  :JZ35_not_pass.py
@Author:Sapphire
@Date  :2020/10/8 23:49
@Desc  :数组中的逆序对：
题干：
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组，求出这个数组中的逆序对的总数P，并将P对1000000007取模的结果输出，即输出P%1000000007
思路：
一、暴力方法：
遍历数组，使用每个元素与后面的元素比较
时间复杂度：O(N^2) --未通过
空间复杂度：O(1)
二、排序法：
copy出一个相同的数组，从小到大进行排序，遍历排序后的数组，
使用data.index(i)求出当前数在原数组中的位置，则排在前面的所有数都构成逆序对，然后在原数组中删除这个最小数，继续遍历下一个最小数。
example：
原数组：data=[3,2,1,5,4,6,0,7]
排序好数组：dataSorted=[0,1,2,3,4,5,6,7]
顺序遍历dataSorted数组，第一个元素0是最小的元素，因此在data数组中，0前面有多少个数，就有多少个逆序对。
在0检测完之后，将0从data数组中删除，data=[3,2,1,5,4,6,7]，dataSorted数组遍历到1，而1其实就是[1,2,3,4,5,6,7]中的最小元素
result：时间复杂度较高 --未通过
"""


class Solution:
    def InversePairs(self, data):
        # write code here
        count = 0
        for i in range(len(data)):
            for j in range(i, len(data)):
                if data[i] > data[j]:
                    count += 1
        return count % 1000000007

    def InversePairs_sort(self, data):
        # write code here
        count = 0
        copy = []
        for i in data:
            copy.append(i)
        copy.sort()

        for i in range(len(copy)):
            count += data.index(copy[i])
            data.remove(copy[i])

        return count % 1000000007


array = [364, 637, 341, 406, 747, 995, 234, 971, 571, 219, 993, 407, 416, 366, 315, 301, 601, 650, 418, 355, 460, 505,
         360, 965, 516, 648, 727, 667, 465, 849, 455, 181, 486, 149, 588, 233, 144, 174, 557, 67, 746, 550, 474, 162,
         268, 142, 463, 221, 882, 576, 604, 739, 288, 569, 256, 936, 275, 401, 497, 82, 935, 983, 583, 523, 697, 478,
         147, 795, 380, 973, 958, 115, 773, 870, 259, 655, 446, 863, 735, 784, 3, 671, 433, 630, 425, 930, 64, 266, 235,
         187, 284, 665, 874, 80, 45, 848, 38, 811, 267, 575]
solution = Solution()
print(solution.InversePairs(array))
