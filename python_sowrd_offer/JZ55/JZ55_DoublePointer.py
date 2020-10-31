# -*- coding: utf-8 -*-
"""
@File  :JZ55_DoublePointer.py
@Author:Sapphire
@Date  :2020/11/1 0:35
@Desc  :链表中环的入口结点
题干：
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
思路：双指针法
快慢指针，快指针一次走两步，慢指针一次走一步。
如果链表中存在环，且环中假设有n个节点，那么当两个指针相遇时，快的指针刚好比慢的指针多走了环中节点的个数，即n步。
从另一个角度想，快的指针比慢的指针多走了慢的指针走过的步数，也是n步。
相遇后，快指针再从头开始走，快慢指针再次相遇时，所指位置就是入口。
时间复杂度：O(n)
空间复杂度：O(1)
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    以下两种方法都是双指针法，循环过程有差别
    """
    def EntryNodeOfLoop(self, pHead):
        # write code here
        slow = fast = pHead
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow2 = pHead
                while slow != slow2:
                    slow = slow.next
                    slow2 = slow2.next
                return slow

    def EntryNodeOfLoop_2(self, pHead):
        if not pHead or not pHead.next or not pHead.next.next:
            return None
        low = pHead.next
        fast = pHead.next.next
        while low != fast:
            if not fast.next or not fast.next.next:
                return None
            low = low.next
            fast = fast.next.next
        fast = pHead
        while low != fast:
            low = low.next
            fast = fast.next
        return fast
