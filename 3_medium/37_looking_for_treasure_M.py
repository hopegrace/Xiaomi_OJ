# -*- coding: UTF-8 -*-
# description: 很久以前，有一个很古老而且很富有的民族，但是有一天，他们惨遭外敌入侵，族人都惨遭杀害无一幸免。族长在最后时刻，
#              为了防止财宝落入贼人之手，把财宝藏在了一个秘密的地方，并设置了一些机关，必须解开所有机关才能够获得宝藏。
#              假设族长一共设置 n 道机关，分别用0 ~ n-1表示。这些机关中有的可以直接解开，
#              有的机关必须要先解开另一个或另一些机关之后才能解开该机关。
#              有一天你机缘巧合来到了这个地方，请问你能否顺利解开所有机关拿到宝藏？
#         举例：假设有两个机关：0和1。 如果要求解开1之前先解开0，而对0没有先决条件要求，则可以先解开0，再解开1，从而获得宝藏；
#              如果要求解开1之前先解开0，同时解开0之前先解开1，则由于0与1互为先决条件，所以无法解开0与1，因此无法获得宝藏。
#     输入格式：单组输入，每组包含k行（0<k<1000)：
#                 第 1 行：一个正整数n，表示一共设置了多少机关，0<n<100;
#                 第 2~k 行：每行由两个整数构成，分别为a和b，表示要解开a机关必须先解开b机关，a与b的范围：0≤a,b≤n−1
#
#     输出格式：输出字符串类型的 "true" 或者 "false"，均为小写，表示是否能够解开所有机关拿到宝藏。
#
# example: input:2
#                0 1
#                1 0
#          output:'false'


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    input_data = line.split("\n")
    n = int(input_data.pop(0))
    intrigue = [int(x) for y in input_data for x in y.split()]
    k = len(intrigue) // 2
    num_list = [0 for x in range(n)]  # 有多少个机关依赖该机关，位置代表机关
    wait_list = [[] for x in range(n)]  # 每个机关依赖其他机关的列表，位置代表机关

    for i in range(k):
        num_list[intrigue[2 * i + 1]] += 1
        wait_list[intrigue[2 * i]].append(intrigue[2 * i + 1])

    solve_stack = []
    for i in range(n):
        if num_list[i] == 0:
            solve_stack.append(i)  # num_list[i]==0说明机关i不依赖其他机关，可以直接解开

    while solve_stack:  # 用已经解开的机关破解其他机关
        cur = solve_stack.pop(0)
        for item in wait_list[cur]:  # cur机关对应的要先解开的机关item,既然cur解开了，那么item必然也解开了
            num_list[item] -= 1  # 依赖item的机关的数量少1
            if num_list[item] == 0:
                solve_stack.append(item)

    for item in num_list:
        if item > 0:
            return 'false'
    return 'true'


test1 = "2\n0 1\n1 0"
print(solution(test1))  # "false"


# # 小米OJ提交版本
# import sys
# input_data = []
# for line in sys.stdin:
#     line = line.strip()
#     input_data += [line]  # 注意是[line]而不是line。line是字符串，list+=str，会将字符串拆解，每个字符作为列表的一个元素加入
# n = int(input_data.pop(0))
# intrigue = [int(x) for y in input_data for x in y.split()]
# k = len(intrigue) // 2
# num_list = [0 for x in range(n)]
# wait_list = [[] for x in range(n)]
#
#
# for i in range(k):
#     num_list[intrigue[2 * i + 1]] += 1
#     wait_list[intrigue[2 * i]].append(intrigue[2 * i + 1])
#
# solve_stack = []
# for i in range(n):
#     if num_list[i] == 0:
#         solve_stack.append(i)
#
# while solve_stack:
#     cur = solve_stack.pop(0)
#     for item in wait_list[cur]:
#         num_list[item] -= 1
#         if num_list[item] == 0:
#             solve_stack.append(item)
#
# res = 'true'
# for item in num_list:
#     if item > 0:
#         res = 'false'
# print(res)


# # 另外一种解答
# def solution2(line):
#   orders = line.split(';')
#   n = int(orders[0])
#   orders = [t.split(',') for t in orders[1:]]
#   orders = [(int(t0), int(t1)) for t0, t1 in orders]
#
#   previous = dict()
#   for a, b in orders:
#     if a in previous:
#       previous[a].append(b)
#     else:
#       previous[a] = [b]
#
#   nums = set(i for i in range(n))
#   while len(nums) > 0:
#     flag = False
#     for i in nums:
#       if i not in previous:
#         nums.remove(i)
#         flag = True
#         break
#       else:
#         if all(j not in nums for j in previous[i]):
#           nums.remove(i)
#           del previous[i]
#           flag = True
#           break
#
#     if not flag:
#       break
#
#   return len(nums) > 0 and "false" or "true"