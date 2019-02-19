# -*- coding: UTF-8 -*-
# description: 规定两种操作：一种是在字符串末尾加字符A。另一种是先反转整个字符串，再给字符串末尾加上字符B。
#              给出一个初始串S，一个终点串T。问能否通过这两个操作从S变换到T。
#              如果可以输出1(若初始串和终点串相同，视为可以变换)，不可以则输出0。
#
# example: input:AB ABB      (由英文空格分隔的两个字符串，每个字符串只由AB两个字符组成)
#          output:0          (1或0，1表示可以变换，0表示不可以变换。)


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    S, T = line.split(" ")

    res_list = [T]
    while len(res_list[0]) > len(S):
        tmp_list = res_list
        res_list = []
        for item in tmp_list:
            if item[-1] == 'A':
                res_list.append(item[:-1])
            else:
                res_list.append(item[:-1][::-1])
    return 1 if S in res_list else 0


test1 = "AB ABB"
print(solution(test1))  # 0

test2 = "AAAB AAABA"
print(solution(test2))  # 1

test3 = "AABB BBAAB"
print(solution(test3))  # 1
