# -*- coding: UTF-8 -*-
# description: 给出一个无序数列，每次只能交换相邻两个元素，求将原数列变成递增数列的最少交换次数。
#              如：数列：2,3,1，交换3和1后变成：2,1,3；交换1和2之后变成：1,2,3。总共交换2次。。
# example: input:2,3,1 (逗号隔开的正整数数列)
#          output:2    (正整数)


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    number = [int(x) for x in line.strip().split(',')]
    exchange_times=0

    def need_exchange(number):
        for i in range(len(number)-1):
            if number[i]>number[i+1]:
                return i+1
        return 0

    while need_exchange(number) != 0:
        i = need_exchange(number)-1
        number[i], number[i + 1] = number[i + 1], number[i]
        exchange_times +=1

    return exchange_times






print(solution('2,3,5'))


