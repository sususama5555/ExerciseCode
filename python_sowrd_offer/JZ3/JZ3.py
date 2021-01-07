# -*- coding: utf-8 -*-
"""
@File  :JZ3.py
@Author:Sapphire
@Date  :2021/1/7 23:53
@Desc  :从尾到头打印链表
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead_1(self, listNode):
        stack = []
        while listNode:
            stack.insert(0, listNode.val)
            listNode = listNode.next
        return stack

    def printListFromTailToHead(self, listNode):
        # write code here
        if listNode is None:
            return []
        return self.printListFromTailToHead(listNode.next) + [listNode.val]
