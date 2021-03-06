# -*- coding: utf-8 -*-
"""
@File  :JZ19.py
@Author:Sapphire
@Date  :2020/9/22 16:55
@Desc  :顺时针打印矩阵：详解见./mix_code/spiral_order.py
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
"""


class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        m = len(matrix)
        n = len(matrix[0])
        order_list = []
        if not (matrix and m and n):
            return order_list
        if n == 1:
            return [i[0] for i in matrix]
        if m == 1:
            return matrix[0]
        for i in range(int((min(m, n) + 1) / 2)):
            for j in range(i, n - i):
                order_list.append(matrix[i][j])
            if m < n and m % 2 and i == int((m - 1) / 2):
                # 当最后一层只剩一行时，遍历后结束其他三条边的统计
                break
            for j in range(i + 1, m - i):
                order_list.append(matrix[j][(n - 1) - i])
            for j in range(i + 1, n - i):
                order_list.append(matrix[(m - 1) - i][(n - 1) - j])
            for j in range(i + 1, m - i - 1):
                order_list.append(matrix[(m - 1) - j][i])
        return order_list


test_matrix_1 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    # [16, 17, 18, 19, 20]
]
test_matrix_2 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
test_matrix_3 = [[x for x in range(6 * y, 6 * (y + 1))] for y in range(6)]
spiral_order = Solution()
print(spiral_order.printMatrix(test_matrix_1))
print(spiral_order.printMatrix(test_matrix_2))
