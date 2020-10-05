# -*- coding: utf-8 -*-
"""
@File  :JZ33_enumerate.py
@Author:Sapphire
@Date  :2020/10/5 23:13
@Desc  :丑数：
题干：把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
方法：通过排列组合2、3、5组合的次数，求出组合出来的数，然后排序取第 index 个
todo 时间复杂度非常高，需要减少循环的index次数
"""


class Solution:
    """
    列出所有丑数的列表（2、3、5的n次组合），然后进行排列
    """
    def GetUglyNumber_Solution(self, index):
        # write code here
        num_list = []
        for i in range(index):
            num_2 = i
            for j in range(index - num_2):
                num_3 = j
                for k in range(index - num_2 - num_3):
                    num_5 = k
                    num_list.append(",".join(map(str, [num_2, num_3, num_5])))
        cmp_sort = lambda x: (2 ** int(x.split(",")[0])) * (3 ** int(x.split(",")[1])) * (5 ** int(x.split(",")[2]))
        cmp_list = sorted(set([cmp_sort(i) for i in num_list]))
        return cmp_list[index - 1]


solution = Solution()
print(solution.GetUglyNumber_Solution(200))