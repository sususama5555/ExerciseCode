# -*- coding: utf-8 -*-
"""
@File  :JZ23.py
@Author:Sapphire
@Date  :2020/9/26 1:10
@Desc  :二叉搜索树的后序遍历序列
题干：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
解题思路：
1、后续遍历的最后一个节点是根节点
2、BST(二叉搜索树)特性：
若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值
3、综上，除去末尾根节点，BST的后续遍历中，前面一部分都小于根节点的数是左子树，后一部分都大于根节点的是右子树。
不符合则判断不是BST的后序遍历。
然后递归剩下的左右子树，直到所有子树都满足以上条件，才判断是BST的后序遍历
"""
import copy


class Solution:
    """
    todo 优化：子树序列长度只需 <= 2，则该子树满足BST的后续遍历
    """
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        root = sequence.pop()
        left = []
        right = []
        for i in range(len(sequence) + 1):
            tmp_list = copy.deepcopy(sequence)
            tmp_list.insert(i, root)
            left = tmp_list[:i + 1]
            right = tmp_list[i:]
            if max(left) <= root <= min(right):
                left.pop()
                right.pop(0)
                break
            if len(right) <= 1:
                return False

        result_left = self.VerifySquenceOfBST(left) if left else True
        result_right = self.VerifySquenceOfBST(right) if right else True
        return result_left and result_right


back_list = [4, 8, 6, 12, 16, 14, 10]
solution = Solution()
print(solution.VerifySquenceOfBST(back_list))
