# -*- coding: utf-8 -*-
"""
@File  :JZ24_DFS.py
@Author:Sapphire
@Date  :2020/9/27 0:26
@Desc  :二叉树中和为某一值的路径：
提干：
输入一颗二叉树的根节点和一个整数，按字典序打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
思路：
`输出二叉树的从根结点到每个叶子节点的路径`的变种，使用DFS（深度优先搜索），
只是判断条件上多了一个`路径的和为指定数`
todo 使用非递归的方法
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def __init__(self):
        self.result = []

    def FindPath(self, root, expectNumber):
        # write code here
        if root is None:
            return []
        # 使用DFS拿到所有路径
        self.DFSFindPath(root, [root.val])
        # 筛选出sum为指定整数的路径
        return [path for path in self.result if sum(path) == expectNumber]

    def DFSFindPath(self, root, path):
        """
        使用深度优先搜索（遍历），递归找到树的所有的路径（二叉树的从根结点到每个叶子节点的路径）
        """
        if not root.left and not root.right:
            self.result.append(path)
        if root.left:
            self.DFSFindPath(root.left, path + [root.left.val])
        if root.right:
            self.DFSFindPath(root.right, path + [root.right.val])

