# description:在你面前有一个n阶的楼梯，你一步只能上1阶或2阶。 请问计算出你可以采用多少种不同的方式爬完这个楼梯。
# example: input:5 （一个正整数，表示这个楼梯一共有多少阶）
#          output:8 （一个正整数，表示有多少种不同的方式爬完这个楼梯）

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution1(line):  # 使用递归
    stairs = int(line)

    def DP(n):
        if n <= 3:
            return n
        else:
            return DP(n - 1) + DP(n - 2)
    return DP(stairs)


def solution2(line):  # 使用循环
    stairs = int(line)
    DP_list = [1] * stairs
    DP_list[1] = 2
    for i in range(2, stairs):
        DP_list[i] = DP_list[i - 1] + DP_list[i - 2]
    return DP_list[stairs - 1]
