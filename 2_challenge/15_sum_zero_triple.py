# -*- coding: UTF-8 -*-
# description: 给出一个整数数组, 数组中是否存在任意3个数a,b,c满足 a+b+c=0? 找出数组中所有满足以上条件的三元组。
#              最后输出这些三元组的个数（包含相同元素的三元组只计算一次）。
#
# example: input:-1,0,1,2,-1,-4 （一个包含多个整数（正或负）的字符串，每个整数之间用逗号分隔）
#          output:2 （输入满足加和结果正好等于 0 的三元组的个数）


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    number_list = [int(x) for x in line.split(',')]
    number_list.sort()

    res = []
    i = 0
    length = len(number_list)

    while i < length:
        start = i + 1
        end = length - 1

        while start < end:
            triple_sum = number_list[i] + number_list[start] + number_list[end]
            if triple_sum == 0 and [number_list[i], number_list[start], number_list[end]] not in res:
                res.append([number_list[i], number_list[start], number_list[end]])
                start += 1
                end -= 1
            elif triple_sum < 0:
                start += 1
            else:
                end -= 1

        i += 1

    return len(res)
