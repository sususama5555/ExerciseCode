# -*- coding: utf-8 -*-
"""
@File  :JZ48.py
@Author:Sapphire
@Date  :2020/10/25 1:40
@Desc  :不用加减乘除做加法：
题干：
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
思路：
二进制 位运算
reference:https://zhuanlan.zhihu.com/p/74641093
"""


class Solution:
    def Add(self, num1, num2):
        while num2:
            sum = num1 ^ num2
            carry = 0xFFFFFFFF&(num1 & num2)<<1
            carry = -(~(carry - 1) & 0xFFFFFFFF) if carry > 0x7FFFFFFF else carry
            num1 = sum
            num2 = carry
        return num1