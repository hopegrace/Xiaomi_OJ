# description: 判断一个数字是否为优秀数字。优秀数字定义为，一个整数M(M>=0)，有2条规则：
#                   规则1：存在一个正整数N(N>=0)，使得M=2^N+1；
#                   规则2：存在一个正整数N(N>=0)，使得M=2^N-1；
#              若同时满足规则1和规则2，则输出Very Good
#              若满足规则1而不满足规则2，则输出Good
#              若不满足规则1而满足规则2，则输出Bad
#              若都不满足，则输出Normal

# example: input:8(一个整数M(M>=0))
#          output:Normal (输出该数属于的类型)


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    M = int(line)
    s = M-1
    t = M+1

    number_s=number_t=0
    while s != 0:
        s=s&(s-1) # 本质上就是抹去了二进制中的0位
        number_s += 1
        if number_s >=2:
            number_s = -1
            break

    while t != 0:
        t=t&(t-1) # 本质上就是抹去了二进制中的0位
        number_t += 1
        if number_t >=2:
            number_t = -1
            break

    if number_s == 1:
        if number_t == 1:
            return 'Very Good'
        else:
            return 'Good'
    elif number_t == 1:
        return 'Bad'
    else:
        return 'Normal'


