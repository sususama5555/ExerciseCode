# -*- coding: utf-8 -*-
"""
@File  :JZ39_pruning.py
@Author:Sapphire
@Date  :2020/10/11 2:30
@Desc  :平衡二叉树（判断）：
题干：
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
在这里，我们只需要考虑其平衡性，不需要考虑其是不是排序二叉树
思路（较优解）：
改为从下往上遍历，如果子树是平衡二叉树，则返回子树的高度；如果发现子树不是平衡二叉树，则直接停止遍历，这样至多只对每个结点访问一次。
tip1:
利用后序遍历：左子树、右子树、根节点,可以先递归到叶子节点，然后在回溯的过程中来判断是否满足条件。
tips2:
在JZ39_complex.py解法的基础上，如果不满足平衡二叉树的定义，则返回-1，
并且如果左子树不满足条件了，直接返回-1，右子树也是如此，相当于 剪枝 ，加速结束递归。
算法复杂度为O（N）
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def IsBalanced_Solution(self, pRoot):
        return self.dfs(pRoot) != -1

    def dfs(self, pRoot):
        if pRoot is None:
            return 0
        left = self.dfs(pRoot.left)
        if left == -1:
            return -1
        right = self.dfs(pRoot.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return max(left, right) + 1
