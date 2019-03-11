# -*- coding: UTF-8 -*-
# description: 给定两个数组，由数字0-9组成的，长度分别为a和b，需要用a、b两个数组中的数字组合得到长度为k(k<=a+b)的正整数，
#           输出所有可能的组合中数值最大的一个（原同一数组中的数字顺序不能改变）
#        输入格式：a、b 数组中的数字间用逗号隔开，两个数组以及k之间用空格隔开，如：1,3,4,5,1,2 8,9,1 5，
#                 其中a = [1,3,4,5,1,2]，b = [8,9,1]，k = 5. 数组a, b元素个数不大于20.
#        输出格式：长度为k的所有组合中数值最大的整数，如：95121
#                 从a或b中取数的时候需保证a，b 内部的顺序不变，如第一个数取到b中的9，那么b中只有1可以后续取用；
#                 第二个数取到a中的5，则a中还剩下1,2可以后续取用。
# example: input:6,3,8,9,4,6,0 3,5,7 6
#          output:963570


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""

def solution(line):
    array_a,array_b,k=line.split()
    array_a = [int(x) for x in array_a]
    array_b = [int(x) for x in array_b]
    k=int(k)
    len_a= len(array_a)
    len_b= len(array_b)






test1 = "6,3,8,9,4,6,0 3,5,7 6"
print(solution(test1))  # 963570

test2 = "2,6,8,4,3 6,9,2,5 3"
print(solution(test2))  # 985

test3 = "3,7,2 7,9,5,1 7"
print(solution(test3))  # 7953721
