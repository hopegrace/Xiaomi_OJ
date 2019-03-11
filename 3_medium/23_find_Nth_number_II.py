# -*- coding: UTF-8 -*-
# description: 假如有一组字符串符合如下规律：
#                                     S1=1
#                                     S2=12
#                                     S3=123
#                                     ......
#                                     S18=123456789101112131415161718
#              即对于Sn来说，就是将1到n的数字拼接在一起。
#              现在将所有的字符串拼接在一起，组成一个无限长的字符串S=1121231234⋯12345678910111213⋯
#              找出该字符串的第n位数字是多少。
#
# example: input:6  （一个整数（1<整数<10^15）,表示所求的位数是多少位）
#          output:3  （一个整数，表示该位上的数字是多少）


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""

def solution(line):
    def calculate(item):
        t = len(str(item))
        
    number = int(line)

    pass


test1="1"
print(solution(test1))  # 1

test2= "6"
print(solution(test2))  # 6

test3="7"
print(solution(test3))  # 1

