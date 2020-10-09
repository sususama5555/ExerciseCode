# -*- coding: utf-8 -*-
"""
@File  :JZ36_stack.py
@Author:Sapphire
@Date  :2020/10/9 10:39
@Desc  :两个链表的第一个公共结点：
题干：
输入两个链表，找出它们的第一个公共结点。（注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）
思路一：使用堆栈解决
两条相交的链表呈Y型。可以从两条链表尾部同时出发，最后一个相同的结点就是链表的第一个相同的结点。
可以利用栈来实现。时间复杂度有O(m + n), 空间复杂度为O(m + n)
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
        pList1 = []
        pList2 = []
        first = None
        while pHead1:
            pList1.append(pHead1)
            pHead1 = pHead1.next
        while pHead2:
            pList2.append(pHead2)
            pHead2 = pHead2.next
        while pList1 and pList2:
            p1 = pList1.pop()
            p2 = pList2.pop()
            if p1 is p2:
                first = p1
            else:
                break
        return first
