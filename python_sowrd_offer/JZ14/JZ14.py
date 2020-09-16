# -*- coding: utf-8 -*-
"""
@File  :JZ14.py
@Author:Sapphire
@Date  :2020/9/15 20:15
@Desc  :
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head or k <= 0:
            return None
        # 设置两个指针，p2指针先走（k-1）步，然后再一起走，当p2为最后一个时，p1就为倒数第k个 数
        p1 = p2 = head
        # p2先走，走k-1步，如果k大于链表长度则返回 空，否则的话继续走
        while k > 1:
            if p2.next:
                p2 = p2.next
                k -= 1
            else:
                return None
        # 两个指针一起 走，一直到p2为最后一个,p1即为所求
        while p2.next:
            p1 = p1.next
            p2 = p2.next
        return p1


list_node_1 = ListNode([1, 2, 4, 6])
list_node_2 = ListNode([4, 8, 9, 5])
list_node_3 = ListNode([7, 11, 19, 22])
list_node_1.next = list_node_2
list_node_2.next = list_node_3

solution = Solution()
print(solution.FindKthToTail(list_node_1, 1))
