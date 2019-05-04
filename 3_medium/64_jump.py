# -*- coding: UTF-8 -*-
# description: 给定一个数字串 (均为正整数)，现在需要从第一个数跳跃到最后一个，所在位置的数字表示可以跳跃的最大步数。
#              求出从第一个位置跳跃到最后位置所需的最少步数。
#
#         输入格式：一个数字串，每个数字用空格隔开，如 1 2 3 4 5 6 7。
#         输出格式：一个整数，表示最少步数，比如需要从第一位1跳到最后一位7，则 1->2->4->7，最少需要3步。
#
# example: input:1 2 3 4 5 6 7
#          output:3


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""
# 贪心策略,只考虑必然可以到达


def solution(line):
    arr = [int(x) for x in line.strip().split()]
    n = len(arr)

    reach = arr[0]
    last_reach = 0
    res = 0
    for i in range(n):
        if i > last_reach:
            res += 1
            last_reach = reach
        reach = max(reach, i + arr[i])
    return res


test1 = '1 2 3 4 5 6 7'
print(solution(test1))  # 3

test2 = "3 1 1 1 1"
print(solution(test2))  # 2

test3 = "2 3 2 3 2 3 2 3 2 3"
print(solution(test3))  # 5

test4 = "2 3 4 2 5 2 3 5 1 2 3 4"
print(solution(test4))  # 4



# # 提交版本
# import sys
#
# for line in sys.stdin:
#     arr = [int(x) for x in line.strip().split()]
#     n = len(arr)
#
#     reach = arr[0]
#     last_reach = 0
#     res = 0
#     for i in range(n):
#         if i > last_reach:
#             res += 1
#             last_reach = reach
#         reach = max(reach, i + arr[i])
#     print(res)
