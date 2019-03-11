# -*- coding: UTF-8 -*-
# description: 石头收藏家小明在徒步登山时发现了一堆美丽的石头。这些石头价值不菲，但是都很重，小明自身的力气有限，一次只能拿他拿得动的一部分。
#              每块石头的重量不同，价值也不同。问小明在力所能及的情况下能拿走价值多少的石头。
#              说明：小明只能搬运一次。例如：小明只能拿得动 10 kg，每块石头的重量分别为2kg，3kg，5kg，7kg，
#              对应的价值分别为 1万，5万，2万，4万。小明能拿的是 3kg 以及 7kg 的石头，价值 9 万。
#         输入格式：使用分号(;)分隔三组数据。 第一组为一个整数，表示小明一次能搬运的最大重量。
#                 第二组为一个使用逗号(,)分隔的数组，表示每块石头的重量。
#                 第三组为一个使用逗号(,)分隔的数组，表示每块石头的对应的价值。
#         输出格式：一个整数，表示小明这次能带回去的石头的总价。
#
# example: input:10;2,3,5,7;1,5,2,4
#          output:9


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    max_weight,stone_weight,stone_value = line.split(";")
    max_weight = int(max_weight)
    stone_weight = [int(x) for x in stone_weight.split(",")]
    stone_value = [int(x) for x in stone_value.split(",")]
    stone_number =len(stone_weight)

    dp=[[0 for x in range(max_weight+1)] for y in range(stone_number+1)]

    for i in range(stone_number):
        tmp_weight = stone_weight[i]
        tmp_value = stone_value[i]
        for j in range(1,max_weight+1):
            if j>=tmp_weight:
                dp[i+1][j] = max(dp[i][j], dp[i][j - tmp_weight] + tmp_value)
            else:
                dp[i+1][j] = dp[i][j]

    return str(dp[stone_number][max_weight])


test1="10;2,3,5,7;1,5,2,4"
print(solution(test1))