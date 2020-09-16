# -*- coding: utf-8 -*-
"""
@File  :JZ15_easy.py
@Author:Sapphire
@Date  :2020/9/16 22:24
@Desc  :反转链表：
输入一个链表，反转链表后，输出新链表的表头。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    单一中间变量实现
    """
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if (pHead and pHead.next) is None:
            return pHead
        pre = None
        cur = pHead
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre


list_node_1 = ListNode([1, 2, 4, 6])
list_node_2 = ListNode([4, 8, 9, 5])
list_node_3 = ListNode([7, 11, 19, 22])
list_node_1.next = list_node_2
list_node_2.next = list_node_3
solution = Solution()
print(solution.ReverseList(list_node_1))
