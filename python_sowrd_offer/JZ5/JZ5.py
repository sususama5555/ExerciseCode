# -*- coding: utf-8 -*-
"""
@File  :JZ5.py
@Author:Sapphire
@Date  :2021/1/8 0:22
@Desc  :用两个栈实现一个队列
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
"""


class SolutionA:
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def push(self, node):
        # write code here
        self.stack_1.append(node)

    def pop(self):
        # return xx
        if not self.stack_1:
            return None
        while self.stack_1:
            self.stack_2.append(self.stack_1.pop())
        res = self.stack_2.pop()
        while self.stack_2:
            self.stack_1.append(self.stack_2.pop())
        return res


class SolutionB:
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def push(self, node):
        # write code here
        self.stack_1.append(node)
        self.stack_2.insert(0, node)

    def pop(self):
        # return xx
        if not self.stack_1:
            return None
        self.stack_1.pop(0)
        return self.stack_2.pop()
