# -*- coding: utf-8 -*-
"""
@File  :JZ29_Heapsort.py
@Author:Sapphire
@Date  :2020/10/3 23:02
@Desc  :最小的K个数：
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。
方法二：
Heapsort：堆排序：
建立一个容量为k的大根堆的优先队列。
遍历一遍元素，如果队列大小 < k，就直接入队，否则，让当前元素与队顶元素相比，如果队顶元素大，则出队，将当前元素入队
"""


class Solution:
    def __init__(self):
        self.heap = []

    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if len(tinput) < k or k == 0:
            return []
        self.buildHeap(tinput[:k], k)
        for i in range(k, len(tinput)):
            if tinput[i] > self.heap[0]:
                continue
            else:
                self.heap[0] = tinput[i]
                self.perceDown(0, k)
        return sorted(self.heap)

    def buildHeap(self, tinput, k):
        self.heap = tinput
        for i in range(k // 2, -1, -1):
            self.perceDown(i, k)

    def perceDown(self, i, k):
        temp = self.heap[i]
        while (2 * i + 1) < k:
            child = 2 * i + 1
            if (child < k - 1) and self.heap[child] < self.heap[child + 1]:
                child = child + 1
            if temp < self.heap[child]:
                self.heap[i] = self.heap[child]
                i = child
            else:
                break
        self.heap[i] = temp


arr = [12, 11, 13, 5, 6, 7]
solution = Solution()
print(solution.GetLeastNumbers_Solution(arr, 2))
