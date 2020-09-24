# -*- coding: utf-8 -*-
"""
@File  :JZ20.py
@Author:Sapphire
@Date  :2020/9/23 23:21
@Desc  :从上往下打印二叉树：
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
知识点：二叉树，队列，树的层次遍历
思路：
1.初始化一个队列， 将root节点入队列
2.如果队列不空，做如下操作：
3.弹出队列头，保存为node，将node的左右非空孩子加入队列
4.做2,3步骤，知道队列为空
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        layer_list = [root]
        if root is None:
            return []
        # 遍历每一层，从左到右追加元素到列表末尾，实现从上到下、从左到右的顺序
        for node in layer_list:
            if node.left:
                layer_list.append(node.left)
            if node.right:
                layer_list.append(node.right)
        return [i.val for i in layer_list]