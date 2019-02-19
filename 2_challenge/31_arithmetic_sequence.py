# -*- coding: UTF-8 -*-
# description: 给出一个正整数N（2<=N<=10000000），统计有多少公差为2的正整数等差数列，使得数列的和为N。
#              举例： 正整数15，可以写为15和3,5,7两个等差数列。 其中15自身就是一个等差数列，3+5+7=15也是一个符合条件的等差数列，
#              所以输出为 2，表示有两个符合条件的等差数列。请注意时间复杂度限制
#
# example: input:30      (一个正整数，表示等差数列中所有数的和，范围为 [2,10000000])
#          output:4     (一个正整数，表示可以找到多少符合条件的正整数等差数列。 (由于一个数字也可以算做等差数列，所以输出至少为1))


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""
def solution(line):
    N = int(line)
    # 设数列为x1,x1+2,x1+4,...,x1+2n，则有(n+1)(x1+n)=N,n和x1为正整数,变为有多少组正整数解的问题

    res=1
    for n in range(1,N//2):  # N//2也可以换成int(math.sqrt(N)+2)来加速运算
        if N%(n+1):
            continue
        elif N/(n+1) - n>=1:
            res += 1

    return res

test1='30'
print(solution(test1))


