# -*- coding: utf-8 -*-
"""
@File  :JZ16_non-recursive.py
@Author:Sapphire
@Date  :2020/9/18 0:08
@Desc  :合并两个排序的链表：
输入两个单调递增的链表，输出两个链表合成后的链表，
当然我们需要合成后的链表满足单调不减规则。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    递归版本
    """
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1
        if pHead1.val < pHead2.val:
            pHead1.next = self.Merge(pHead1.next, pHead2)
            return pHead1
        else:
            pHead2.next = self.Merge(pHead1, pHead2.next)
            return pHead2


# {1,3,5}
list_node_1 = ListNode(1)
list_node_2 = ListNode(3)
list_node_3 = ListNode(5)
list_node_1.next = list_node_2
list_node_2.next = list_node_3
# {2,4,6}
list_node_4 = ListNode(2)
list_node_5 = ListNode(4)
list_node_6 = ListNode(6)
list_node_4.next = list_node_5
list_node_5.next = list_node_6

solution = Solution()
print(solution.Merge(list_node_1, list_node_4))
