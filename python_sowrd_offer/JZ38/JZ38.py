# -*- coding: utf-8 -*-
"""
@File  :JZ38.py
@Author:Sapphire
@Date  :2020/10/11 2:25
@Desc  :二叉树的深度：
题干：
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。、
思路：
递归的方法，比较左边路径和右边路径哪边最长，选择最长的一边路径，加上root结点本身的长度。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot is None:
            return 0
        else:
            return max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1
