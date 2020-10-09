# -*- coding: utf-8 -*-
"""
@File  :JZ36_stack.py
@Author:Sapphire
@Date  :2020/10/9 10:39
@Desc  :两个链表的第一个公共结点：
题干：
输入两个链表，找出它们的第一个公共结点。（注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）
思路二（最优）：双指针法
设置两个指针，一个从pHead1开始遍历，遍历完pHead1再遍历pHead2，
另一个从pHead2开始遍历，遍历完pHead2再遍历pHead1，
如果有交点，两个指针会同时遍历到交点处，既两个指针走过相同的长度的链表，最终两个指针到达 null 或者到达公共结点。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
#
# @param pHead1 ListNode类
# @param pHead2 ListNode类
# @return ListNode类
#
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        p1 = pHead1
        p2 = pHead2
        while p1 != p2:
            if p1 is None:
                p1 = pHead2
            else:
                p1 = p1.next
            if p2 is None:
                p2 = pHead1
            else:
                p2 = p2.next
        return p2
