# -*- coding: utf-8 -*-
"""
@File  :JZ45.py
@Author:Sapphire
@Date  :2020/10/15 23:42
@Desc  :扑克牌顺子：
题干：
一副扑克牌,里面有2个大王，2个小王，从中随机抽出5张牌，如果牌能组成顺子就输出true，否则就输出false。
为了方便起见，大小王是0，大小王可以当作任何数字。
思路：满足以下条件则为 True
1、五张牌中，除0外没有重复的牌。可用 set 实现，或者排序后 numbers[i] != numbers[i+1]
2、max(numbers) - min(numbers) < 5，最大值、最小值相差需要小于 5。
"""


class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return numbers
        list = [i for i in numbers if i != 0]
        if len(list) == len(set(list)):
            nlow = list[0]
            nhigh = list[-1]
            for i in list:
                if i < nlow:
                    nlow = i
                elif i > nhigh:
                    nhigh = i
            if nhigh - nlow < len(numbers):
                return True
            else:
                return False
        else:
            return False


array = [1, 3, 2, 5, 4]
solution = Solution()
print(solution.IsContinuous(array))
