# 输入：有N行测试数据，每一行有两个代表整数的字符串 a 和 b，长度超过百位。规定 a>=b，a, b > 0。a和b之间用“-”连接，即a-b
#      测试结果可以用 linux 小工具 bc进行测试是否正确。
# 输出：返回表示结果整数的字符串

# description:两个长度超出常规整形变量上限的大数相减，请避免使用各语言内置大数处理库，如 Java.math.BigInteger等。
# example: input:10 10 11 12 12 11 16
#          output:16

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution1(line):
    a, b = line.strip().split('-')
    a = [int(item) for item in a][::-1]
    b = [int(item) for item in b][::-1]

    res = ''
    for i in range(len(b)):
        if a[i] >= b[i]:
            res = res + str(a[i] - b[i])
        else:
            res = res + str(10 + a[i] - b[i])
            a[i + 1] = a[i + 1] - 1

    if len(a) == len(b):
        res = res[::-1]
        for j in range(len(res)):
            if res[j] != '0':
                return res[j:]
    else:
        for j in range(len(b), len(a)):
            if a[j] >= 0:
                res = res + str(a[j])
            else:
                res = res + str(a[j] + 10)
                a[j + 1] = a[j + 1] - 1

    return res[::-1]


def solution2(line):
    a, b = line.strip().split('-')
    a = [int(item) for item in a]
    b = [int(item) for item in b]
    res = ''
    for i in range(len(b)):
        flag_a = len(a) - 1 - i
        flag_b = len(b) - 1 - i
        if a[flag_a] >= b[flag_b]:
            res = str(a[flag_a] - b[flag_b]) + res
        else:
            res = str(10 + a[flag_a] - b[flag_b]) + res
            while a[flag_a - 1] == 0:
                a[flag_a - 1] = 9
                flag_a -= 1
            a[flag_a - 1] -= 1
    for j in range(len(a) - 1 - i - 1, -1, -1):
        res = str(a[j]) + res
    zero_flag = 0
    for i in range(len(res)):
        if res[i] != '0':
            zero_flag = 1
            break
    if zero_flag == 0:
        return 0
    return res[i:]

