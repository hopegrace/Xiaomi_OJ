# -*- coding: UTF-8 -*-
# description:现有等式：a*(x1^3) + b*(x2^3) + c*(x3^3) = d*(x4^3) + e*(x5^3)
#             其中a,b,c,d,e满足-50<=a,b,c,d,e<=50,且均为非0整数。x1,x2,x3,x4,x5也是如此，即属于-50到50的非零整数。
#             给出a,b,c,d,e,求出满足等式成立的x1,x2,x3,x4,x5(均为整数)的组数。
#
# example: input:-14 -42 -23 27 -48    (五个整数a,b,c,d,e)
#          output:3022                 (满足等式成立的数据的组数)


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""

from collections import defaultdict


def solution(line):
    a, b, c, d, e = [int(x) for x in line.strip().split()]
    pos = defaultdict(lambda: 0)
    zero_cal = 0
    for i in range(-50, 51):
        if i == 0:
            continue
        for j in range(-50, 51):
            if j == 0:
                continue
            for k in range(-50, 51):
                if k == 0:
                    continue
                left = a * (i**3) + b * (j**3) + c * (k**3)
                if left > 0:
                    pos[left] += 1
                if left == 0:
                    zero_cal += 1

    res = 0
    for i in range(-50, 51):
        if i == 0:
            continue
        for j in range(-50, 51):
            if j == 0:
                continue
            right = d * (i**3) + e * (j**3)
            if right > 0:
                res += 2 * pos[right]
            if right == 0:
                res += zero_cal

    return res


test1 = "-14 -42 -23 27 -48"
print(solution(test1))  # 3022


# import sys
# from collections import defaultdict
# for line in sys.stdin:
#     a, b, c, d, e = [int(x) for x in line.strip().split()]
#     pos = defaultdict(lambda:0)
#     zero_cal = 0
#     for i in range(-50, 51):
#         if i == 0:
#             continue
#         for j in range(-50, 51):
#             if j == 0:
#                 continue
#             for k in range(-50, 51):
#                 if k == 0:
#                     continue
#                 left = a * (i**3) + b * (j**3) + c * (k**3)
#                 if left > 0:
#                     pos[left] += 1
#                 if left ==0:
#                     zero_cal += 1
#
#     res = 0
#     for i in range(-50, 51):
#         if i == 0:
#             continue
#         for j in range(-50, 51):
#             if j == 0:
#                 continue
#             right = d * (i**3) + e * (j**3)
#             if right > 0:
#                 res += 2*pos[right]
#             if right == 0:
#                 res += zero_cal
#     print(res)



# # 不超时版本
# import sys
#
# for line in sys.stdin:
#     line = line.strip()
#     nums = list(map(int, line.split()))
#     v = {}
#     v2 = {}
#     v3 = {}
#     for i in range(-50, 51):
#         if i != 0:
#             for j in nums:
#                 if j not in v.keys():
#                     v[j] = []
#                 v[j].append(i * i * i * j)
#
#     for x1 in v[nums[-1]]:
#         for x2 in v[nums[-2]]:
#             if x1 + x2 not in v2.keys():
#                 v2[x1 + x2] = 0
#             v2[x1 + x2] += 1
#
#     for x1 in v[nums[0]]:
#         for x2 in v[nums[1]]:
#             if x1 + x2 not in v3.keys():
#                 v3[x1 + x2] = 0
#             v3[x1 + x2] += 1
#
#     count = 0
#     for k in v2:
#         for i in v[nums[2]]:
#             k2 = k + i
#
#             if k2 in v3.keys():
#                 n1 = v2[k]
#                 n2 = v3[k2]
#
#                 count += n1 * n2
#     d = len(nums) - len(set(nums))
#     p = 1
#     for i in range(d):
#         p *= 4
#     count = count // p
#
#     print(str(count))
