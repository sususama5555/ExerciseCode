# -*- coding: utf-8 -*-
"""
@File  :JZ40_bitwise_XOR.py
@Author:Sapphire
@Date  :2020/10/12 23:58
@Desc  :组中只出现一次的数字：
题干：一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
思路：位运算（异或运算）
异或运算：如果a、b两个值不相同，则异或结果为1，如果a、b两个值相同，异或结果为0。
所以，我们可以让数组中的每一个数异或一下，最后会得到一个结果ret，就是两个出现一次的数字的异或结果。
这个结果肯定是由两个不同数字异或而来，因此我们找ret二进制中为1的位置i，因为1一定是由0,1异或而来，因此要求得两个数中，一定有一个数的二进制中的第i个位置为1， 一个为0。
时间复杂度：O(n)
空间复杂度：O(1)
"""


class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        res = 0
        for i in array:
            res ^= i
        splitBit = 1
        while splitBit & res == 0:
            splitBit = splitBit << 1
        res1 = 0
        res2 = 0
        for i in array:
            if i & splitBit == 0:
                res1 ^= i
            else:
                res2 ^= i
        return [res1, res2]


array = [4, 2, 5, 7, 8, 9, 4, 7]
solution = Solution()
print(solution.FindNumsAppearOnce(array))
