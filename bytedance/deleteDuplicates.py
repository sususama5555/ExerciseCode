# -*- coding: utf-8 -*-
"""
@File  :deleteDuplicates.py
@Author:Sapphire
@Date  :2021/1/10 2:04
@Desc  :删除有序链表中重复的元素
删除给出链表中的重复元素（链表中元素从小到大有序），使链表中的所有元素都只出现一次
例如：
给出的链表为1\to1\to21→1→2,返回1 \to 21→2.
给出的链表为1\to1\to 2 \to 3 \to 31→1→2→3→3,返回1\to 2 \to 31→2→3.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
#
# @param head ListNode类
# @return ListNode类
#
class Solution:
    def deleteDuplicates(self, head):
        # write code here
        if not head:
            return None
        node = head
        while node.next:
            if node.val != node.next.val:
                node = node.next
            else:
                node.next = node.next.next
        return head
