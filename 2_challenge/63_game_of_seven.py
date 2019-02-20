# -*- coding: UTF-8 -*-
# description: 数7游戏，从1开始报数，遇到7的倍数以及含7的数字直接pass。写出一个算法，计算第N个数是多少。
#
# example: input(多个example): 1 7 8 24 123 3467 88888  99999  (一个正整数 N，表示需要计算的数为第N个数，1<=N<=100000)
#          output(对应input) : 1 8 9 30 169 5493 168223 198026 (第N个数的数值)

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""

def solution(line):
    N = int(line)

    count = 0
    number = 0
    while count <N:
        number +=1
        if number%7==0 or '7' in str(number):
            continue
        else:
            count += 1

    return number

test1="99999"
print(solution(test1))  # 198026


