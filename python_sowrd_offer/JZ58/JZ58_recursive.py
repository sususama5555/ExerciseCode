# -*- coding: utf-8 -*-
"""
@File  :JZ58_recursive.py
@Author:Sapphire
@Date  :2020/11/4 23:01
@Desc  :对称的二叉树
题干：
请实现一个函数，用来判断一棵二叉树是不是对称的。
注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
思路：递归法：
1、递归的思想，首先判断头结点是否为空。
2、然后将根节点的左右两个节点假设成两个独立的树，
3、如果左右两个树都为空，返回True。
4、然后看左子树的左结点和右子树的右结点、左子树的右结点和右子树的左结点是否相同，都相同返回True.
时间复杂度：O(N)
空间复杂度：O(N),最坏情况下，二叉树退化为链表
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        return self.compare(pRoot.left, pRoot.right)

    def compare(self, left, right):
        if not left and not right:
            return True
        if not left or not right or left.val != right.val:
            return False
        return self.compare(left.left, right.right) and self.compare(left.right, right.left)

    # todo 尝试优化以下代码实现
    # def isSymmetrical(self, pRoot):
    #     # write code here
    #     while pRoot.left and pRoot.right:
    #         if pRoot.left.val == pRoot.right.val:
    #             self.isSymmetrical(pRoot.left)
    #             self.isSymmetrical(pRoot.right)
    #         else:
    #             return False
    #     return True
