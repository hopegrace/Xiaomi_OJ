# description: 水果店有好多筐香蕉，我的要求是买回来的每一筐里必须有相同数量的香蕉。为了实现这个目标，你可以每次做两件事情。
#              1）放弃框里的一部分香蕉 2）连筐带香蕉放弃一整筐
#              我想知道我最多能得到多少香蕉。
# example: input:5 0 29 14 (以空格分割的多个正整数，每个正整数表示一筐香蕉的总香蕉数)
#          output:29 (最多能得到的香蕉数)


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    num_list = [int(x) for x in line.split()]
    num_list.sort()
    length = len(num_list)
    max_banana = 0

    for i in range(length):
        max_banana = max(max_banana, num_list[i] * (length - i))

    return max_banana

