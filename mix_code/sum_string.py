# -*- coding: utf-8 -*-
"""
@File  :sum_string.py
@Author:Sapphire
@Date  :2020/9/16 9:27
@Desc  :给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和，并以字符串输出。
要求：
# num1 和num2 的长度都小于 5100.
# num1 和num2 都只包含数字 0-9.
# num1 和num2 都不包含任何前导零。
你不能使用任何內建库，也不能直接将输入的字符串转换为整数形式。
例如：
输入：'123, 12'
返回：'135'
"""


class Solution:
    """
    思路：
    将输入分割成两个相加的字符串，反转之后迭代，从低位开始相加
    迭代次数为最大相加数的长度，长度不够需补零，注意相加进位的情况
    """
    def sum_string(self, string):
        sum_result = []
        string = string.replace(" ", "").split(",")
        str_1_reverse = string[0][::-1]
        str_2_reverse = string[1][::-1]
        tmp_carry = 0
        for i in range(max(len(str_1_reverse), len(str_2_reverse))):
            tmp_1 = int(str_1_reverse[i]) if len(str_1_reverse) > i else 0
            tmp_2 = int(str_2_reverse[i]) if len(str_2_reverse) > i else 0
            sum_result.append(str(tmp_1 + tmp_2 + tmp_carry)[-1])
            tmp_carry = 1 if tmp_1 + tmp_2 > 10 else 0
        return "".join(sum_result[::-1])


solution = Solution()
print(solution.sum_string("123, 1192"))


