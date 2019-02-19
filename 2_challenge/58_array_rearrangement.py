# -*- coding: UTF-8 -*-
# description: 给出一个无序数组，只要对其中的一段子数组进行升序排列，就可以使整个数组变为升序。试求出这个子数组的长度。
#              举例：有一个数组[2,6,4,8,10,9,15]，只需对其子数组[6,4,8,10,9]进行升序排列，整个数组即可变为升序，所以返回子数组的长度5。
#
# example: input:2,6,4,8,10,9,15      (使用逗号分隔的一组整数，0<整数<100，0<整数个数<500。)
#          output:5                   (一个整数，表示子数组的长度。)


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    array = [int(x) for x in line.split(",")]
    length = len(array)

    start, end = 0, length - 1
    while start < end:
        if array[start] <= min(array[start + 1:end + 1]):
            start += 1
            continue
        if start < end and array[end] >= max(array[start:end]):
            end -= 1
        else:
            break

    return 0 if end == start else end - start + 1


test1 = "2,6,4,8,10,9,15"
print(solution(test1))  # 5

test2 = "76,44,56,28,23,69,1,72"
print(solution(test2))  # 8

test3 = "4,4,4,4,4,4,4,5"
print(solution(test3))  # 0

test4 = "21,28,92,61"
print(solution(test4))  # 2

