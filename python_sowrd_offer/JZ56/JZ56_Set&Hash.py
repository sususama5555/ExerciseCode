# -*- coding: utf-8 -*-
"""
@File  :JZ56_Set&Hash.py
@Author:Sapphire
@Date  :2020/11/2 23:51
@Desc  :删除链表中重复的结点
题干：
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
思路：set集合暴力解法（hash思想）
1、遍历单链表相邻两个元素，如果相等，就加入到set当中
2、pre指针指向重复值的前一个节点，cur指向当前遍历的节点值
3、遍历单链表当前元素，在 set 中存在（说明重复），则删除，pre->next = cur->next
4、如果不在 set 中（不是重复值），则pre = pre->next， cur = cur->next
时间复杂度：O(2n)，遍历了2次单链表
空间复杂度：最坏为O(n)，最好为O(1)
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead:
            return pHead
        # 遍历单链表，如果相邻的元素相同，则加入set
        same_set = set()
        pre = pHead
        cur = pHead.next
        while cur:
            if pre.val == cur.val:
                same_set.add(pre.val)
            pre = pre.next
            cur = cur.next
        # 遍历单链表，如果下一个节点的值在set中，则该节点指向下下个节点
        vhead = ListNode(-1)
        vhead.next = pHead
        pre = vhead
        cur = pHead
        while cur:
            if cur.val in same_set:
                cur = cur.next
                pre.next = cur
            else:
                cur = cur.next
                pre = pre.next
        return vhead.next


node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(2)
node_4 = ListNode(3)

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4

solution = Solution()
print(solution.deleteDuplication(node_1))
