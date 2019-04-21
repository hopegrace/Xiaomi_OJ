# -*- coding: UTF-8 -*-
# description: 小明老师准备给一些得到小红花的小朋友发糖果做为奖励。假设有n个小朋友，每个小朋友拥有的小红花为m(n)个，他让这n个小朋友站成一排。
#              要求： 1.每个小朋友至少发一个糖果。
#                    2.如果一个小朋友比相邻的小朋友小红花多，则发他的糖果也必须比相邻的多。
#              问小明最少要发多少个糖果？
#
# example: input:19,9,35,74,22    (每位小朋友的小红花数量，使用逗号分隔)
#          output:9                (最少需要发出的糖果)


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    flowers = [int(x) for x in line.split(",")]
    length = len(flowers)
    reward = [1] * length

    for i in range(length - 1):
        if flowers[i + 1] > flowers[i]:
            reward[i + 1] = reward[i] + 1

    for i in range(length - 2, -1, -1):
        if flowers[i] > flowers[i + 1]:
            reward[i] = max(reward[i], reward[i + 1] + 1)

    return sum(reward)


print(solution("19,9,35,74,22"))


