# -*- coding: utf-8 -*-
"""
@File  :JZ26_non-recursive.py
@Author:Sapphire
@Date  :2020/9/29 1:05
@Desc  :二叉搜索树与双向链表：
非递归法
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None

        p = pRootOfTree

        stack = []
        resStack = []

        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                node = stack.pop()
                resStack.append(node)
                p = node.right

        resP = resStack[0]
        while resStack:
            top = resStack.pop(0)
            if resStack:
                top.right = resStack[0]
                resStack[0].left = top

        return resP
