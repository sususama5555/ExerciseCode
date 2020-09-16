# -*- coding: utf-8 -*-
"""
@File  :JZ15.py
@Author:Sapphire
@Date  :2020/9/16 19:56
@Desc  :反转链表：
输入一个链表，反转链表后，输出新链表的表头。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    列表实现：作为中间变量
    """
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not (pHead and pHead.next):
            return pHead
        tmp_node = pHead.next
        pHead.next = None
        node_list = [pHead]
        while tmp_node:
            node_list.append(tmp_node)
            tmp_node = tmp_node.next
        node_list.reverse()
        for i in range(len(node_list) - 1):
            node_list[i].next = node_list[i + 1]
        return node_list[0]


list_node_1 = ListNode([1, 2, 4, 6])
list_node_2 = ListNode([4, 8, 9, 5])
list_node_3 = ListNode([7, 11, 19, 22])
list_node_1.next = list_node_2
list_node_2.next = list_node_3
solution = Solution()
print(solution.ReverseList(list_node_1))
