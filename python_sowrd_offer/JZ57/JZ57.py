# -*- coding: utf-8 -*-
"""
@File  :JZ57.py
@Author:Sapphire
@Date  :2020/11/3 23:43
@Desc  :二叉树的下一个结点
题干：
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
思路：
1、如果该节点有右子树，那么它的下一个节点就是它的右子树的最左侧子节点；
2、如果该节点没有右子树且是父节点的左子树，那么下一节点就是父节点；
3、如果该节点没有右子树且是父节点的右子树，比如i节点，那么我们往上找父节点，找到一个节点满足： 它是它的父节点的左子树的节点。
时间复杂度：最坏情况下为O(N)
空间复杂度：O(1)
"""


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def GetNext(self, pNode):
        if not pNode:
            return None
        if pNode.right:
            res = pNode.right
            while res.left:
                res = res.left
            return res
        while pNode.next:
            tmp = pNode.next
            if tmp.left == pNode:
                return tmp
            pNode = tmp
        return None
