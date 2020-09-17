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
    """
    非递归版本
    """
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        pHeadList = []
        while pHead1 and pHead2:
            # 当一个链表遍历完后，退出循环
            if pHead1.val > pHead2.val:
                pHeadList.append(pHead2)
                pHead2 = pHead2.next
            else:
                pHeadList.append(pHead1)
                pHead1 = pHead1.next
        # 记录没遍历完的链表
        if not pHead1:
            pHeadList.append(pHead2)
        else:
            pHeadList.append(pHead1)
        for i in range(len(pHeadList) - 1):
            pHeadList[i].next = pHeadList[i + 1]
        return pHeadList[0]


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
