# -*- coding: UTF-8 -*-
# description: 有一个不为空且仅包含正整数的数组，找出其中出现频率最高的前K个数，时间复杂度必须在 O(nlogn) 以内。
#
# example: input:1,1,1,2,2,3 2 （一行数据包括两部分，一个正整数数组（数字间 ',' 分隔）和一个正整数K(1≤K≤数组长度),数组和K之间有一个空格）
#          output:1,2 （输出包含前 K 个出现频率最高的数（出现频率相同时，较小的数在前），用','分隔，保证升序排列。）


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    number_list, K = line.split()
    number_list = [int(x) for x in number_list.split(',')]
    K = int(K)

    d = {}
    res = []

    for num in number_list:
        if num in d.keys():
            d[num] += 1
        else:
            d[num] = 1
    d_sort = sorted(d.items(), key=lambda item: item[1], reverse=True)
    # d.items()将d这个字典转为可迭代对象，其元素为元组(d.key1,d.value1),(d.key2,d.value2)之类的，key参数对应的lambda表达式则表明使用第二个元素作为比较参数

    i = 0
    length_d = len(d_sort)
    while i < K:
        if i<length_d-1 and d_sort[i][1] == d_sort[i + 1][1] and d_sort[i][0] > d_sort[i + 1][0]:
            res.append(str(d_sort[i + 1][0]))
            if i == K - 1:
                break
            res.append(str(d_sort[i][0]))
            i += 2
        else:
            res.append(str(d_sort[i][0]))
            i += 1

    return ",".join(res)

