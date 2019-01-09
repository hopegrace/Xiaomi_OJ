# -*- coding: UTF-8 -*-
# description: 给出一组不重复的正整数，从这组数中找出所有可能的组合使其加合等于一个目标正整数 M，如：
#              一组数为 1, 2, 3，目标数为 4，那么可能的加合组合为：1111 / 112 / 121 / 13 / 211 / 22 / 31
#              注意相同的组合数字顺序不同也算一种，所以这个例子的结果是 7 种。
# example: input:1,2,3 4 （一组连续不重复的 N 个正整数（, 隔开，0<N<100）以及目标正整数（与数组之间用空格隔开））
#          output:7 （所有可能的加和等于目标正整数 M 的组合种数）


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    number_list, M = line.split()
    number_list = [int(x) for x in number_list.split(',')]
    M = int(M)


    return 0


print(solution('1,2,3 4'))





