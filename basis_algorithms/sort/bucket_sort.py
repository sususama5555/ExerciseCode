# -*- coding: utf-8 -*-
"""
@File  :bucket_sort.py
@Author:Sapphire
@Date  :2020/12/14 0:38
@Desc  :桶排序：
桶排序又叫箱排序，工作的原理是将数组分到有限数量的桶子里。
每个桶子再个别排序（有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排序）。
桶排序是鸽巢排序的一种归纳结果。
步骤：
- 1.创建一个定量的数组当作空桶子；
- 2.遍历序列，把元素一个一个放到对应的桶子去；
- 3.对每个不是空的桶子进行排序；
- 4.从不是空的桶子里把元素再放回原来的序列中。
"""


def bucket_sort(arr):
    max_num = max(arr)
    n = len(arr)
    buckets = [[] for _ in range(n)]  # 创建桶
    for var in arr:
        i = min(var // (max_num // n), n - 1)  # i 表示 var 放到几号桶里
        buckets[i].append(var)  # 把 var 加到桶里边
        # 保持桶内的顺序
        for j in range(len(buckets[i]) - 1, 0, -1):
            if buckets[i][j] < buckets[i][j - 1]:
                buckets[i][j], buckets[i][j - 1] = buckets[i][j - 1], buckets[i][j]
            else:
                break
    sorted_arr = []
    for buc in buckets:
        sorted_arr.extend(buc)
    return sorted_arr


arr = [12, 11, 13, 5, 6, 7]
print(bucket_sort(arr))
