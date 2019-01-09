# -*- coding: UTF-8 -*-
# description: 给出三个队列s1，s2，s3，判断s3是否是由s1和s2交叉得来。
#              如：s1为aabcc,s2为dbbca。当s3为aadbbcbcac时，返回true。
#              (即将s1拆成三部分:aa,bc,c分别插入s2对应位置),否则返回false。
# example: input:aabcc,dbbca,aadbbcbcac
#          output:true


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


# def solution(line):
#     s1, s2, s3 = line.strip().split(',')
#     s1, s2, s3 = list(s1), list(s2), list(s3)
#     len1, len2, len3 = len(s1), len(s2), len(s3)
#
#     if len(s1) + len(s2) != len(s3):
#         return 'false'
#
#     matched = [[False for i in range(len2 + 1)] for j in range(len1 + 1)]
#     # 动态规划矩阵matched[l1][l2]表示s1取l1长度,s2取l2长度，是否能匹配s3的l1+12长度。
#     # 则有matched[l1][l2] = s1[l1-1] == s3[l1+l2-1] && matched[l1-1][l2] || s2[l2 - 1] == s3[l1+l2-1] && matched[l1][l2-1]
#     # 边界条件是其中一个长度为0，另一个去匹配s3
#
#     matched[0][0] = True
#
#     for i in range(1, len1 + 1):
#         if s1[i - 1] == s3[i - 1]:
#             matched[i][0] = True
#
#     for i in range(1, len2 + 1):
#         if s2[i - 1] == s3[i - 1]:
#             matched[0][i] = True
#
#     for i1 in range(1, len1 + 1):
#         for i2 in range(1, len2 + 1):
#             i3 = i1 + i2
#             if s1[i1 - 1] == s3[i3 - 1]:
#                 matched[i1][i2] = matched[i1][i2] or matched[i1 - 1][i2]
#             if s2[i2 - 1] == s3[i3 - 1]:
#                 matched[i1][i2] = matched[i1][i2] or matched[i1][i2 - 1]
#
#     return str(matched[len1][len2]).lower()

def solution(line):
    s1, s2, s3 = line.strip().split(',')
    s1, s2, s3 = list(s1), list(s2), list(s3)
    len1, len2, len3 = len(s1), len(s2), len(s3)

    if len(s1) + len(s2) != len(s3):
        return 'false'

    matched = [[0 for i in range(len2 + 1)] for j in range(len1 + 1)]
    # 动态规划矩阵matched[l1][l2]表示s1取l1长度,s2取l2长度，是否能匹配s3的l1+12长度。
    # 则有matched[l1][l2] = s1[l1-1] == s3[l1+l2-1] && matched[l1-1][l2] || s2[l2 - 1] == s3[l1+l2-1] && matched[l1][l2-1]
    # 边界条件是其中一个长度为0，另一个去匹配s3

    matched[0][0] = 1

    for i in range(1, len1 + 1):
        if s1[i - 1] == s3[i - 1]:
            matched[i][0] = 1

    for i in range(1, len2 + 1):
        if s2[i - 1] == s3[i - 1]:
            matched[0][i] = 1

    for i1 in range(1, len1 + 1):
        for i2 in range(1, len2 + 1):
            i3 = i1 + i2
            if s1[i1 - 1] == s3[i3 - 1] and matched[i1][i2] == 0:
                matched[i1][i2] = matched[i1 - 1][i2]
            if s2[i2 - 1] == s3[i3 - 1] and matched[i1][i2] == 0:
                matched[i1][i2] = matched[i1][i2 - 1]

    if matched[len1][len2] == 0:
        return 'false'
    else:
        return 'true'


print(solution('aabcc,dbbca,aadbbcbcac'))
print(solution('aabcc,dbbca,aadbbbaccc'))
print(solution('a,b,ab'))
print(solution('a,b,ba'))
print(solution('a,b,ac'))
print(solution('abc,bca,bcaabc'))
print(solution('abc,bca,aabbcc'))

# # true false true true false true false

