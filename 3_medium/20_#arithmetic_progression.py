# -*- coding: UTF-8 -*-
# description: 等差数列是常见数列的一种，公差常用字母d表示。对于数列S，它满足了(S[i]−S[i−1])=d(i>1)。
#              显然，一个数字无法构成等差数列，而任意两个数字可以形成一个等差数列。
#              这里给出了一个长度为N(0<N<200)的数字序列，每个位置有一个整数(−100≤整数≤100)，
#              需要找到这个数字序列里包含多少个等差数列，序列顺序固定，无需排序。
#
#           输入数据格式：S[0] S[1] S[2] ... S[N](以半角空格符分隔，N>1),其中数列S的项为整数
#           输出数据格式：等差数列数量M
#
# example: input:2 7 4 5 6
#          output:12
#        [2 7 4 5 6]该数列包含等差数列：
#        [2 7] [2 4] [2 5] [2 6] [7 4] [7 5] [7 6] [4 5] [4 6] [5 6] [2 4 6] [4 5 6]
#        共有12个，故应输出12


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""

import collections


def solution(line):
    numbers = [int(x) for x in line.split()]
    length = len(numbers)
    res = length * (length - 1) / 2
    dp = [collections.Counter() for i in range(len(numbers))]

    for i in range(len(numbers)):
        for j in range(i):
            tmp_d = numbers[i] - numbers[j]
            dp[i][tmp_d] += 1
            if not (tmp_d in dp[j]):
                continue
            dp[i][tmp_d] += dp[j][tmp_d]
            res += dp[j][tmp_d]

    return int(res)


test1 = "2 7 4 5 6"
print(solution(test1))  # 12

test2 = "3 3 3 3"
print(solution(test2))  # 11
