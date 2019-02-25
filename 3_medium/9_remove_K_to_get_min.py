# -*- coding: UTF-8 -*-
# description: 有一行由N个数字组成的数字字符串，字符串所表示的数是一正整数。移除字符串中的 K 个数字，使剩下的数字是所有可能中最小的。
#              假设：字符串的长度一定大于等于K，字符串不会以 0 开头
#
# example: input:1432219 3   (一行由N个数字组成的数字字符串（0<N<20），和一个正整数K(K<N)，两个数据由空格隔开，如:1432219 3。)
#          output:1219       (移除K位后可能的最小的数字字符串。如1432219移除 4, 3, 2这3个数字后得到1219，为所有可能中的最小值。)


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    N, K = line.split()
    K = int(K)
    number = [int(x) for x in list(N)]

    res=[]
    for digit in number:
        while K>0 and res and res[-1]>digit:
            res.pop()
            K -= 1
        res.append(digit)

    while K>0:  # 有的不一定能在前面删掉K个数字，如"112 1"
        res.pop()
        K -= 1

    return ''.join(str(x) for x in res).lstrip('0') or '0'


test1 = "1432219 3"
print(solution(test1))  # 1219

test2 = "10200 1"
print(solution(test2))  # 200
