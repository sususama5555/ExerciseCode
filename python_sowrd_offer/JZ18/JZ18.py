# -*- coding: utf-8 -*-
"""
@File  :JZ18.py
@Author:Sapphire
@Date  :2020/9/22 16:03
@Desc  :二叉树的镜像
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root is None:
            return None
        root.left, root.right = root.right, root.left
        self.Mirror(root.left)
        self.Mirror(root.right)
        return root

    def invertTree(self, root):
        """
        self.Mirror的简化版
        """
        if not root:
            return None
        # 一行解决，上一种形式的精简版
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
