# -*- coding: utf-8 -*-
"""
@File  :spiral_order.py
@Author:Sapphire
@Date  :2020/9/22 10:16
@Desc  :螺旋遍历二维数组：
用迭代来做：
从外到内按层级遍历，每一层按顺序遍历四条边的数组，注意四条边有重合，需要确定边界。
见图解 ./figure/spiralOrder.py
todo 使用递归法：
[n层] = [第n层] + [n-1层]
[n-1层] = [第n-1层] + [n-2层]
......
[2层] = [第2层] + [第1层]
"""


class SpiralOrder:
    def spiralOrder(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        order_list = []
        # 当二维数组是空或任何一个维度是0，直接返回
        # todo matrix为[]时，matrix[0]边界问题
        if matrix is None or m == 0 or n == 0:
            return order_list
        if n == 1:
            return [i[0] for i in matrix]
        if m == 1:
            return matrix[0]
        # 大循环，从外向内逐层遍历矩阵
        for i in range(int((min(m, n) + 1) / 2)):
            # 从左到右遍历 上边
            for j in range(i, n - i):
                order_list.append(matrix[i][j])
            # 当最后一层只剩一行时，遍历后结束其他三条边的统计
            if m < n and m % 2 and i == int((m - 1) / 2):
                break
            # 从上到下遍历 右边
            for j in range(i + 1, m - i):
                order_list.append(matrix[j][(n - 1) - i])
            # 从右到左遍历 下边
            for j in range(i + 1, n - i):
                order_list.append(matrix[(m - 1) - i][(n - 1) - j])
            # 从下到上遍历 左边
            for j in range(i + 1, m - i - 1):
                order_list.append(matrix[(m - 1) - j][i])
        return order_list


test_matrix_1 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]
test_matrix_2 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
test_matrix_3 = [[x for x in range(6 * y, 6 * (y + 1))] for y in range(6)]
test_matrix_4 = [
    [1],
    [2],
    [3],
    [4],
    [5]
]
spiral_order = SpiralOrder()
# print(spiral_order.spiralOrder(test_matrix_1))
# print(spiral_order.spiralOrder(test_matrix_2))
# print(spiral_order.spiralOrder(test_matrix_3))
print(spiral_order.spiralOrder(test_matrix_4))
