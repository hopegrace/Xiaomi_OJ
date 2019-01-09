# description: 要吃到自己心爱的胡萝卜，小米兔需要跳过面前一些格子。现有N个格子，每个格子内都写上了一个非负数，表示当前最多可以往前跳多少格。
#              胡萝卜就放在最后一个格子上。米兔开始站在第 1 个格子，试判断米兔能不能跳到最后一个格子吃到胡萝卜呢？
# example: input:2 0 1 0 0 3 4 (输入为N个数字(N<10)，用空格隔开，第i个数字S_i(0<=S_i<10)表示米兔站在第i个格子上时，最多能往前跳的格数。)
#          output:false (若米兔能跳到最后一个格子上吃到胡萝卜，输出 “true“，否则输出 “false“)


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    num_list = [int(x) for x in line.split(' ')]
    length = len(num_list)
    location_list = [0] * length

    for i in range(length):
        for j in range(1, num_list[i] + 1):
            if i + j <= length - 1:
                location_list[i + j] = 1

    for i in range(1,length):
        if location_list[i] == 0:
            return 'false'

    return 'true'

