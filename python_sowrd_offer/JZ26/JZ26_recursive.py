# -*- coding: utf-8 -*-
"""
@File  :JZ26_recursive.py
@Author:Sapphire
@Date  :2020/9/29 1:04
@Desc  :二叉搜索树与双向链表：
递归法
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Convert(self, root):
        if not root:
            return None
        if not root.left and not root.right:
            return root

        # 将左子树构建成双链表，返回链表头
        left = self.Convert(root.left)
        p = left

        # 定位至左子树的最右的一个结点
        while left and p.right:
            p = p.right

        # 如果左子树不为空，将当前root加到左子树链表
        if left:
            p.right = root
            root.left = p

        # 将右子树构造成双链表，返回链表头
        right = self.Convert(root.right)
        # 如果右子树不为空，将该链表追加到root结点之后
        if right:
            right.left = root
            root.right = right

        return left if left else root
