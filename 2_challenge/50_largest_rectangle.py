# -*- coding: UTF-8 -*-
# description: 在一个平面图上，有多个宽度固定为1，高度不同的矩形并列排着，在这些矩形所组成的图形中，能够切割出的最大矩形的面积是多少？
#              举例：高度为2,3,2的三个矩形所组成的图形，能够切割出的最大的矩形面积为6。
#
# example: input:5,6,7,8,3      (一组正整数，分别用逗号隔开，表示每个矩形的高度,0<高度<100)
#          output:20            (一个整数，表示组合成的最大的矩形面积)


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    number_array = [int(x) for x in line.split(",")]
    length = len(number_array)
    res_max = 0

    for start in range(0, length + 1):
        for end in range(length - 1, start - 1, -1):
            tmp_max = (min(number_array[start:end + 1])) * (end + 1 - start)
            res_max = max(res_max, tmp_max)

    return res_max


test = "5,6,7,8,3"
print(solution(test))  # 20

