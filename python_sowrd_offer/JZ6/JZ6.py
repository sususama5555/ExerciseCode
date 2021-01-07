# -*- coding: utf-8 -*-
"""
@File  :JZ6.py
@Author:Sapphire
@Date  :2021/1/8 0:39
@Desc  :旋转数组中的最小数字
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
"""


class Solution:
    def minNumberInRotateArray_O_N(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0
        for i in range(len(rotateArray) - 1):
            if rotateArray[i] > rotateArray[i + 1]:
                return rotateArray[i + 1]
        return rotateArray[0]

    def minNumberInRotateArray_O_logn(self, rotateArray):
        if not rotateArray:
            return 0
        l = 0
        r = len(rotateArray) - 1
        while l < r:
            mid = (l + r) / 2
            if rotateArray[mid] > rotateArray[r]:
                l = mid + 1
            else:
                r = mid
        return rotateArray[l]
