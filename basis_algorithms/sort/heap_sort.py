# -*- coding: utf-8 -*-
"""
@File  :HeapSort.py
@Author:Sapphire
@Date  :2020/10/3 23:20
@Desc  :堆排序：
堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。
堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。
堆排序可以说是一种利用堆的概念来排序的选择排序。
步骤：
- 1.构建堆：将待排序序列构建成一个堆 H[0……n-1]，从最后一个非叶子结点开始，从左至右，从下至上进行调整。根据升序或降序需求选择大顶堆或小顶堆；
- 2.此时的堆顶元素，为最大或者最小元素；
- 3.把堆顶元素和堆尾元素互换，调整堆，重新使堆有序；
- 4.此时堆顶元素为第二大元素；
- 5.重复以上步骤，直到堆变空。
"""


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换

        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # 一个个交换元素
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换
        heapify(arr, i, 0)

    return arr


arr = [12, 11, 13, 5, 6, 7]
print(heap_sort(arr))
