# -*- coding: UTF-8 -*-
# description: 给定一个整数数组，找出两个不重叠的子数组A和B，使两个子数组元素和的差的绝对值 |SUM(A) - SUM(B)| 最大。 返回这个最大的差值。
#              例如： 有一个数组{1, 2, -3, 1}，可以从中找出两个子数组A = {1, 2}与B = {-3}，这两个子数组的元素和分别为 SUM(A) = 3，
#              SUM(B) = -3，因此可以求得差的最大值 |SUM(A) - SUM(B)| = 6。
#
#         输入格式：使用逗号(,)分隔的一个整数数组
#         输出格式：一个整数，表示两个子数组元素和的差的最大值
#
# example: input:1,2,-3,1
#          output:6


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""

# 注意不能存在重叠的意思是两个子数组在原数组中的位置不交叉，即两个子数组，左边的子数组的尾一定在右边的子数组的头前面。

def solution(line):
    def diff(array):
        n = len(array)
        left_max = [0] * n
        right_min = [0] * n

        tmp_sum = 0
        max_sum = float("-inf")
        for i in range(n):   # 从左到右计算最大子数组和
            tmp_sum += array[i]
            max_sum = max(max_sum, tmp_sum)
            if tmp_sum < 0:
                tmp_sum = 0
            left_max[i] = max_sum

        tmp_sum = 0
        min_sum = float("inf")
        for i in range(n - 1, -1, -1):  # 从右到左计算最小数组和
            tmp_sum += array[i]
            min_sum = min(min_sum, tmp_sum)
            if tmp_sum > 0:
                tmp_sum = 0
            right_min[i] = min_sum

        res = 0
        for i in range(1, n):
            res = max(res, abs(left_max[i - 1] - right_min[i]))
        return res

    nums = [int(x) for x in line.strip().split(",")]
    res1 = diff(nums)
    res2 = diff(nums[::-1])
    return max(res1, res2)


test1 = '1,2,-3,1'
print(solution(test1))

test2 = "1,3,-3,1,8"
print(solution(test2))
