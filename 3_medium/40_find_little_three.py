# -*- coding: UTF-8 -*-
# description: 给定一个奇数n，可得到一个由从1到n的所有奇数所组成的数列，求这一数列中数字3所出现的总次数。
#              例如当n=3时，可得到奇数列：1,3，其中有一个数字3，故可得1
#
#         输入格式：一个奇数,表示n,0<n<9999999999。
#         输出格式：一个整数，表示从1到n的奇数列中，数字3出现的次数。
#
# example: input:35
#          output:7


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    n=int(line)


    pass

# 初步想法:设n各个数位上的数字分别位a_m,a_(m-1),a_(m-2),...,a_1,则最高位上可以取0到a_m,其他各个位上可以取0到9,只有个位取1,3,5,7,9
# 然后判断有多少个3出现,考虑解答树. 注意取值不能大于n,a_m的情况下,a_(m-1)这个位置上只能取0到a_(m-1),类似的,往下推

test1 = "1"
print(solution(test1))  # 0

test2 = "3"
print(solution(test2))  # 1

test3 = "35"
print(solution(test3))  # 7
