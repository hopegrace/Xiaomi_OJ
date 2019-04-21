# -*- coding: UTF-8 -*-
# description: 小明目前在一家银行的IT部门工作。 银行每天经常会有很多存款业务，所以每天总会收到大量硬币。
#              如何给这些硬币分类排序成了令业务部门十分头疼的一个问题。 这一天，业务部门向IT部门提交了一个需求，
#              希望IT部门能够出一套为硬币进行排序的解决方案，使得面值小的硬币排到前面，其中最核心的算法部门交给了小明来实现。
#              如果你是小明，你会给出一个什么样的算法呢？
#           注： 1.要求不使用任何系统排序函数或库排序函数！！！
#               2.要求时间复杂度为O(n)，空间复杂度为O(1)，也就是不允许建立新数组，只能在原数组上进行排序！！！
#
#         输入格式：一个字符串，只包含a、b、c三种字符，分别表示1元，2元，5元三种硬币
#         输出格式：一个字符串，已按照a、b、c完成排序，表示经过排序后的一排硬币
#
# example: input:cba
#          output:abc


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    res = [0] * 3
    for item in line.strip():
        if item == "a":
            res[0] += 1
        elif item == "b":
            res[1] += 1
        else:
            res[2] += 1
    ans = "a" * res[0] + "b" * res[1] + "c" * res[2]
    return ans


test1 = 'cba'
print(solution(test1))

test2 = "aabc"
print(solution(test2))

test3 = "cbbbbbcccc"
print(solution(test3))
