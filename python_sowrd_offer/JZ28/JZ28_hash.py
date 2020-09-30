# -*- coding: utf-8 -*-
"""
@File  :JZ28_hash.py
@Author:Sapphire
@Date  :2020/9/30 17:10
@Desc  :数组中出现次数超过一半的数字：时间复杂度：O(nlongn)、空间复杂度：O(n)
使用python的dict当做hashmap，key:value，表示数字和出现次数的关系
第一次出现的数字设为num:1，表示次数为1，
每重复出现一次value+1，
如果存在数字的value超过数字长度的一半，则返回该数字
todo：排序法、候选法
排序法：时间复杂度：O(nlongn)、空间复杂度：O(1)，排序后，判断中位数是否为众数。
候选法：时间复杂度：O(n)、空间复杂度：O(1)，
加入数组中存在众数，那么众数一定大于数组的长度的一半，
如果两个数不相等，就消去这两个数，最坏情况下，每次消去一个众数和一个非众数，那么如果存在众数，最后留下的数肯定是众数
"""


class Solution:
    """
    哈希法
    """
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        hash_dict = dict()
        for num in numbers:
            if hash_dict.get(num):
                hash_dict[num] += 1
            else:
                hash_dict[num] = 1
            if hash_dict[num] > len(numbers) / 2:
                return num
        # 以下排序可以得到出现次数的排序
        # sorted(hash_dict, key=lambda x: hash_dict[x], reverse=True)
        return 0


solution = Solution()
print(solution.MoreThanHalfNum_Solution([1, 2, 3, 4, 4, 5, 2, 2, 25, 2, 2, 2, 2]))
