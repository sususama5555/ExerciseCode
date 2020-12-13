# -*- coding: utf-8 -*-
"""
@File  :merge_sort.py
@Author:Sapphire
@Date  :2020/12/13 22:57
@Desc  :归并排序：

**归并的基本步骤：**
- 1.申请空间，使其大小为**两个已经排序序列之和**，该空间用来存放合并后的序列；
- 2.设定两个指针，最初位置分别为两个已经排序序列的起始位置；
- 3.比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置；
- 4.重复步骤 3 直到某一指针达到序列尾；
- 5.将另一序列剩下的所有元素直接到合并序列尾。

**归并排序的步骤：**
- 1.分解：将列表越分越小，直至分成一个元素，终止条件：一个元素是有序的。
- 2.合并：不断将两个有序列表进行归并，列表越来越大，直到所有序列归并完毕。
"""


def merge(arr, low, mid, high):
    # low 和 high 为整个数组的第一个和最后一个位置索引，mid 为中间位置索引
    # i 和 j 为指针，最初位置分别为两个有序序列的起始位置
    # ltmp 用来存放合并后的序列
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <= high:  # 只要左右两边都有数
        if arr[i] < arr[j]:  # 当左边的数小于右边的数
            ltmp.append(arr[i])  # 将左边的数存入 ltmp
            i += 1  # 左边的指针往右移一位
        else:  # 当右边的数小于左边的数
            ltmp.append(arr[j])  # 将右边的数存入 ltmp
            j += 1  # 右边的指针往右移一位
    # 上面的 while 语句执行完后，左边或者右边没有数了
    while i <= mid:  # 当左边还有数的时候
        ltmp.append(arr[i])  # 将左边剩下的数全部存入 ltmp
        i += 1
    while j <= high:  # 当右边还有数的时候
        ltmp.append(arr[j])  # 将右边剩下的数全部存入 ltmp
        j += 1
    arr[low:high + 1] = ltmp  # 将排序后的数组写回原数组


def merge_sort(arr, low, high):  # low 和 high 为整个数组的第一个和最后一个位置索引
    if low < high:  # 至少有两个元素
        mid = (low + high) // 2
        merge_sort(arr, low, mid)  # 把左边递归分解
        merge_sort(arr, mid + 1, high)  # 把右边递归分解
        merge(arr, low, mid, high)  # 做归并
        return arr


def merge_sort_opt(data):
    """
    归并排序：
    根据 JZ35_MergeSort.py 思路
    """
    if len(data) > 1:
        # tips:python2中，n / m为整数，python3中为小数
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]
        merge_sort_opt(left_half)
        merge_sort_opt(right_half)
        i, j, k = len(left_half) - 1, len(right_half) - 1, len(data) - 1
        while i >= 0 and j >= 0:
            if left_half[i] < right_half[j]:
                data[k] = right_half[j]
                j = j - 1
                k = k - 1
            else:
                data[k] = left_half[i]
                i = i - 1
                k = k - 1
        while i >= 0:
            data[k] = left_half[i]
            k = k - 1
            i = i - 1
        while j >= 0:
            data[k] = right_half[j]
            k = k - 1
            j = j - 1
    return data


array = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
print(merge_sort(array, 0, 14))
print(merge_sort_opt(array))
