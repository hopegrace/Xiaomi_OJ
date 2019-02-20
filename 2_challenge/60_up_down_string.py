# -*- coding: UTF-8 -*-
# description: 字符串S由字符+和-构成。字符串D是一个数字字符串，其长度比S要大 1，其格式要求如下：
#                1.D中不包含数字0；
#                2.D中必须包含数字1，且最大数字不大于D的长度；
#                3.D中的数字不重复出现。
#               根据S，可以转换得到唯一的D，S与D的关系为：
#                1.S[i] 为 + 表示 D[i] < D[i+1];
#                2.S[i] 为 - 表示 D[i] > D[i+1]，且 D[i] - D[i+1] = 1.
#               现给出字符串S的值，请构造出合法的字符串D。 如输入 +-+-，输出 13254。
#               因为 1 < 3 > 2 < 5 > 4，符合增减增减（+-+-）的趋势。
#
#
# example: input:++++     (只由 + 和 - 构成的一个字符串。)
#          output:12345       (一个不含0且没有重复数字的字符序列。)


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):

    res = ["1"]
    for i in range(len(line)):
        res.append(str(i + 2))
        if line[i] == "+":
            continue
        else:
            j = i
            while j >= 0 and line[j] == "-":
                res[j], res[j + 1] = res[j + 1], res[j]
                j -= 1

    return "".join(res)


test1 = "++++"
print(solution(test1))  # 12345

test2 = "----"
print(solution(test2))  # 54321

test3 = "+-+-++"
print(solution(test3))  # 1325467

########## 补充证明 #############
# 初始化一个整型数组，第一个数字为1，然后开始往数组后面升序添加数字，
# 并且检查对应的符号，若为‘+’，不作处理；
# 若为‘-’，与前一个数字交换，再检查前一个符号，
# 如果还是‘-’的话，继续交换，直到前一个符号是‘+’。
