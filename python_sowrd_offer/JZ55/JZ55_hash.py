# -*- coding: utf-8 -*-
"""
@File  :JZ55_hash.py
@Author:Sapphire
@Date  :2020/11/1 0:31
@Desc  :链表中环的入口结点
题干：
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
思路：
在遍历链表时，使用set（或者list）存储已经遍历的节点。
如果后续节点在set中（节点相同 = 地址相同），
那么说明形成了环，该节点即为环的入口。
时间复杂度：O(n)
空间复杂度：O(n) -- 最坏情况下，单链表的所有结点都在存入set
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    python3 集合set 方法：
    添加：s.add( x )，x为元素；s.update( x )，参数可以是元素，列表，元组，字典等
    删除：s.remove( x )；s.discard( x )，元素不存在，不会发生错误；set.pop()随机移除一个元素
    清空：s.clear()
    获取交集：x.intersection(y)
    于判断两个集合是否包含相同的元素：set.isdisjoint(set)
    元素是否都包含在指定集合中：set.issubset(set)
    判断指定集合的所有元素是否都包含在原始的集合中，与上条相反：set.issuperset(set)
    获取并集：set.union(set1, set2...)
    返回两个集合中不重复的元素集合：set.symmetric_difference(set)
    """
    def EntryNodeOfLoop(self, pHead):
        # write code here
        node_list = set()
        while pHead:
            if pHead in node_list:
                return pHead
            node_list.add(pHead)
            node_list.update(pHead)
            pHead = pHead.next
        return None
