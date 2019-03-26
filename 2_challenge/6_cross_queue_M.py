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

def solution(line):
    s1, s2, s3 = line.strip().split(',')
    len1, len2, len3 = len(s1), len(s2), len(s3)
    if len1 + len2 != len3:
        return 'false'

    matched = [[0 for i in range(len2 + 1)] for j in range(len1 + 1)]
    # 动态规划矩阵matched[l1][l2]表示s1取l1长度,s2取l2长度，是否能匹配s3的l1+12长度。
    # 则有matched[l1][l2] = s1[l1-1] == s3[l1+l2-1] && matched[l1-1][l2] || s2[l2 - 1] == s3[l1+l2-1] && matched[l1][l2-1]
    # 边界条件是其中一个长度为0，另一个去匹配s3

    matched[0][0] = 1
    for i in range(len1):
        if s1[i] == s3[i]:
            matched[i + 1][0] = 1

    for i in range(len2):
        if s2[i] == s3[i]:
            matched[0][i + 1] = 1

    for i in range(len1):
        for j in range(len2):
            matched[i + 1][j + 1] = ((s1[i] == s3[i + j + 1] and matched[i][j + 1]) or (s2[j] == s3[i + j + 1] and matched[i + 1][j]))

    return 'true' if matched[len1][len2] else 'false'


print(solution('aabcc,dbbca,aadbbcbcac'))  # true false true true false true false
print(solution('aabcc,dbbca,aadbbbaccc'))
print(solution('a,b,ab'))
print(solution('a,b,ba'))
print(solution('a,b,ac'))
print(solution('abc,bca,bcaabc'))
print(solution('abc,bca,aabbcc'))
