# -*- coding: utf-8 -*-
"""
@File  :JZ41_SlideWindow.py
@Author:Sapphire
@Date  :2020/10/14 0:07
@Desc  :和为S的连续正数序列：
题干：
小明很喜欢数学,有一天他在做数学作业时，要求计算出9~16的和，他马上就写出了正确答案是100。
但是他并不满足于此，他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
题目抽象：给定一个1到sum的序列，求所有和为sum的连续序列。
思路：滑动窗口（双指针）
补充：什么是滑动窗口：
使用一个窗口，用窗口的左边界i和右边界j来唯一表示一个窗口，滑动代表，窗口始终从左往右移动，这也表明左边界i和右边界j始终会往后移动，而不会往左移动。
扩大窗口，j += 1，缩小窗口，i += 1。
获取一次满足结果的序列的步骤：
1、初始化，i=1,j=1, 表示窗口大小为0
2、如果窗口中值的和小于目标值sum， 表示需要扩大窗口，j += 1
3、否则，如果狂口值和大于目标值sum，表示需要缩小窗口，i += 1
4、否则，等于目标值，存结果，缩小窗口，继续进行步骤2,3,4
"""

class Solution:
    def FindContinuousSequence(self, tsum):
        res = []
        plow = 1
        phigh = 2
        while plow < phigh:
            curSum = (plow + phigh) * (phigh - plow + 1) / 2
            # 当前的和满足条件时，将满足的序列加入结果中
            if curSum == tsum:
                res.append(range(plow, phigh + 1))
                phigh += 1
            # 当前的和小于条件时，窗口右边界向右滑动
            elif curSum < tsum:
                phigh += 1
            # 当前的和大于条件时，窗口左边界向左滑动
            else:
                plow += 1
        return res


solution = Solution()
print(solution.FindContinuousSequence(4))
