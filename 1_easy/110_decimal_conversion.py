# description: 给出一个P进制整数N，求N的Q进制表示 (0<=N<=32767， 2<=P<=16, 2<=Q<=16).
#               大于9的数字依次使用小写字母a、b、c、d、e、f 表示。请勿使用已存在的进制转换库或函数，比如PHP中的base_convert()等。
# example: input:31 10 16 (输入3个数，以空格分隔： 第1个数是待转换的数， 第2个数是待转换的数的进制， 第3个数是转换后的数的进制。)
#          output:1f (输入转换后的数)


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    N, P, Q = line.split(' ')
    P = int(P)
    Q = int(Q)

    total = 0
    for i in range(len(N)):
        if P > 10 and ord(N[i]) >= 97:
            total += (ord(N[i]) - 97 + 10) * pow(P, (len(N) - i - 1))

        else:
            total += int(N[i]) * pow(P, (len(N) - i - 1))

    stack = []
    while total // Q >= 1:
        res = total % Q
        if res >= 10:
            stack += chr(97 + (res - 10))
        else:
            stack += str(res)
        total = total // Q
    if total >= 10:
        stack += chr(97 + (total - 10))
    else:
        stack += str(total)

    return ''.join(stack[::-1])

