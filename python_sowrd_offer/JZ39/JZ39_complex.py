# -*- coding: utf-8 -*-
"""
@File  :JZ39_complex.py
@Author:Sapphire
@Date  :2020/10/11 2:30
@Desc  :平衡二叉树（判断）：
题干：
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
在这里，我们只需要考虑其平衡性，不需要考虑其是不是排序二叉树
思路：
自顶向下，对于每个节点，都计算一下左子树以及右子树的差的绝对值，即每个节点都判断一下。
遍历每个结点，借助一个获取树深度的递归函数，根据该结点的左右子树高度差判断是否平衡，然后递归地对左右子树进行判断。
缺陷：算法复杂度为O（N**2）
在判断上层结点的时候，会多次重复遍历下层结点，增加了不必要的开销，时间复杂度较高。

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def IsBalanced_Solution(self, pRoot):
        if pRoot is None:
            return True
        left = self.depth(pRoot.left)
        right = self.depth(pRoot.right)
        return abs(left - right) <= 1 and self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def depth(self, pRoot):
        """
        与JZ38的求二叉树的深度同理，递归求出当前节点下最大深度
        """
        if pRoot is None:
            return 0
        return max(self.depth(pRoot.left), self.depth(pRoot.right)) + 1
