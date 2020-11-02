# -*- coding: utf-8 -*-
"""
@File  :JZ56_DoublePointer.py
@Author:Sapphire
@Date  :2020/11/3 0:22
@Desc  :删除链表中重复的结点
题干：
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
思路：双指针法（直接删除）
1.设置一个虚拟头结点，设置两个指针，pre指向虚拟头结点，cur指向头结点。
2.判断下一个节点的值和cur的值是否相等，若相等cur后移，直到下个节点的值和cur的值不同。
3.此时执行pre.next= cur.next。
4.继续走直到结尾.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        dummy = ListNode(-1)
        dummy.next = pHead
        pre = dummy
        cur = pHead
        while cur:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            if pre.next == cur:
                pre = cur
            else:
                pre.next = cur.next
            cur = cur.next
        return dummy.next


node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(2)
node_4 = ListNode(3)

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4

solution = Solution()
print(solution.deleteDuplication(node_1))