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
from typing import List


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
        # 二分查找，时间复杂度Ologn
        if not rotateArray:
            return 0
        l = 0
        r = len(rotateArray) - 1
        while l < r:
            mid = (l + r) // 2
            if rotateArray[mid] > rotateArray[r]:
                l = mid + 1
            elif rotateArray[mid] < rotateArray[r]:
                r = mid
            else:
                r -= 1
                # 如果是升序数组，就可以这么干
                # return rotateArray[mid]
        return rotateArray[l]

    def minNumberInRotateArray(self, rotateArray: List[int]) -> int:
        # 笨办法
        # write code here
        cur_num = rotateArray[0]
        for num in rotateArray:
            if num < cur_num:
                return num
            else:
                cur_num = num
        return rotateArray.index(cur_num)
