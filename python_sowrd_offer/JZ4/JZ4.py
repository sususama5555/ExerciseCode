# -*- coding: utf-8 -*-
"""
@File  :JZ4.py
@Author:Sapphire
@Date  :2021/1/8 0:07
@Desc  :重建二叉树
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, vin):
        if not pre:
            return None
        root = TreeNode(pre[0])
        index = vin.index(root.val)
        root.left = self.reConstructBinaryTree(pre[1:index + 1], vin[0:index])
        root.right = self.reConstructBinaryTree(pre[index + 1:], vin[index + 1:])
        return root
