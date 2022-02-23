# -*- coding: utf-8 -*-
"""
@File  :JZ3.py
@Author:Sapphire
@Date  :2021/1/7 23:53
@Desc  :从尾到头打印链表
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
"""
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead_1(self, listNode: ListNode) -> List[int]:
        # write code here
        # 反转数组
        res = []
        while listNode:
            # 遍历链表，存入数组中
            res.append(listNode.val)
            listNode = listNode.next
        # 数组反向输出
        return res[::-1]

    def printListFromTailToHead_2(self, listNode: ListNode) -> List[int]:
        # write code here
        # 递归 P.S->层级不超过988
        if listNode is None:
            return []
        return self.printListFromTailToHead_2(listNode.next) + [listNode.val]

    def printListFromTailToHead_3(self, listNode: ListNode) -> List[int]:
        # write code here
        # 使用栈
        if not listNode:
            return []
        # 辅助栈
        stack = []
        res = []
        while listNode:
            stack.append(listNode.val)  # 进栈
            listNode = listNode.next
        while stack:
            res.append(stack.pop())  # 出栈
        return res
