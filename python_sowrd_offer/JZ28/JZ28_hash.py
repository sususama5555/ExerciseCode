# -*- coding: utf-8 -*-
"""
@File  :JZ28_hash.py
@Author:Sapphire
@Date  :2020/9/30 17:10
@Desc  :数组中出现次数超过一半的数字：
使用python的dict当做hashmap，key:value，表示数字和出现次数的关系
第一次出现的数字设为num:1，表示次数为1，
每重复出现一次value+1，
如果存在数字的value超过数字长度的一半，则返回该数字
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
        return 0


solution = Solution()
print(solution.MoreThanHalfNum_Solution([1, 2, 3, 4, 4, 5, 2, 2, 25, 2, 2, 2, 2]))
