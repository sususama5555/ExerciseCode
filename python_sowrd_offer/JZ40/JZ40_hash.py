# -*- coding: utf-8 -*-
"""
@File  :JZ40_hash.py
@Author:Sapphire
@Date  :2020/10/12 23:32
@Desc  :数组中只出现一次的数字：
题干：一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
思路一：hashmap
使用dict保存数字出现的次数 key:value => num:count，得到value为1的key
简化：由于其他数字只出现两次，第二次遇到时，删除该 key:value，减少空间复杂度
思路二：list
基于思路一hash的思路，他数字只出现两次，使用list实现hash
当数字第二次出现时，删掉该数字，剩下的为出现一次的数字
hash法：
时间复杂度：O(n)
空间复杂度：O(n)
"""


class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce_dict(self, array):
        """
        使用dict实现hash
        """
        # write code here
        hash_dict = {}
        for i in array:
            if hash_dict.get(i):
                del hash_dict[i]
            else:
                hash_dict[i] = 1
        return [i for i in hash_dict]

    def FindNumsAppearOnce_list(self, array):
        """
        使用数组，第二次出现则删除
        """
        # write code here
        if not array:
            return []
        res = []
        for i in array:
            if i in res:
                res.remove(i)
            else:
                res.append(i)
        return res


array = [4, 2, 5, 7, 8, 9, 4, 7]
solution = Solution()
print(solution.FindNumsAppearOnce_dict(array))
print(solution.FindNumsAppearOnce_list(array))
