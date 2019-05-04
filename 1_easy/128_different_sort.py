# description: 有一天利姆鲁想教他的哥布林部下学数学，因为他之前教过因子，现在想考考他们。
#              利姆鲁问现在有n个数，需要用因子个数的多少进行排序，因子个数多的排在后面，因子个数少的排在前面，
#              如果因子个数相同那么就比较这个数的大小，数大的放在后面，数小的放在前面。
#              现在让你说出排序之后第K个位置的数字是多少。

# example: input:4 6 1 2 3 4 5 6 (第1个整数为整数K，1<K<10^6；第2个为整数n，表示数字的数量，n<10^7,接下来为n个整数，每个数都不大于10^6.
#          output:5 (输出排序之后的第K位置的数值。)


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""
# def count_factors(n):
#     if n==1:
#         return 1
#     factors = 2
#     i = 2
#     while i<=(n//2):
#         if n%i==0:
#             if n//i>i:
#                 factors +=2
#             elif n//i==i:
#                 factors += 1
#             else:
#                 break
#         i += 1
#     return factors
#
# def solution(line):
#     input_data = [int(x) for x in line.strip().split()]
#     K = input_data.pop(0)
#     N = input_data.pop(0)
#     factors_list = []
#
#     for x in input_data:
#         factors_list.append(count_factors(x))
#     factor_dict = dict(zip(input_data,factors_list))
#
#     cmp_key=cmp_to_key(lambda x,y:x[0]-y[0] if x[1]==y[1] else x[1]-y[1])
#     res = sorted(factor_dict.items(),key=cmp_key)
#     return res[K-1][0]
#
#
# from functools import cmp_to_key
# test1="4 6 1 2 3 4 5 6"
# print(solution(test1))  # 5


import sys
from functools import cmp_to_key


def count_factors(n):
    if n == 1:
        return 1
    factors = 2
    i = 2
    while i <= (n // 2):
        if n % i == 0:
            if n // i > i:
                factors += 2
            elif n // i == i:
                factors += 1
            else:
                break
        i += 1
    return factors


for line in sys.stdin:
    input_data = [int(x) for x in line.strip().split()]
    K = input_data.pop(0)
    N = input_data.pop(0)
    factors_list = []

    for x in input_data:
        factors_list.append(count_factors(x))
    factor_dict = dict(zip(input_data, factors_list))

    cmp_key = cmp_to_key(lambda x, y: x[0] - y[0] if x[1] == y[1] else x[1] - y[1])
    res = sorted(factor_dict.items(), key=cmp_key)
    print(res[K - 1][0])
