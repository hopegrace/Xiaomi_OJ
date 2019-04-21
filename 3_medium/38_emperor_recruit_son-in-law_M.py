# -*- coding: UTF-8 -*-
# description: 国王为了给公主找到这个世界上最聪明的人作为驸马，发明了一个游戏。在游戏中，国王设置了多个连续的屋子，
#              从第一个屋子开始，每个屋子都会有n(n>=0)个门来进入接下来的1~n个屋子
#              （例如这个屋子有2个门，那么就是第一个门可以进入之后第一个屋子，第二个门可以进入之后第二个屋子）,
#              最后经过屋子最少的人将获得胜利，迎娶美丽的公主。
#         输入格式：一组数据，分别用逗号隔开，每一个数字表示对应的屋子共有多少扇门。
#         输出格式：一个整数，表示到达最后屋子时经过的最少的屋子数，如果不能到达则返回-1。
#
# example: input:2,3,1,1,4
#          output:2


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    nums = [int(x) for x in line.strip().split(",")]
    n = len(nums)
    reach = nums[0]
    last_reach = 0
    res = 0
    i = 1

    while i < n and i <= reach:
        if i > last_reach:
            res += 1
            last_reach = reach
        reach = max(reach, i + nums[i])
        i += 1

    return -1 if reach < (n - 1) else res


test1 = "2,3,1,1,4"
print(solution(test1))  # 2

test2 = "1,1,1,0,1"
print(solution(test2))  # -1



# # Xiaomi OJ 提交版本
# import sys
#
# for line in sys.stdin:
#     nums = [int(x) for x in line.strip().split(",")]
#     n = len(nums)
#     reach = nums[0]
#     last_reach = 0
#     res = 0
#     i = 1
#
#     while i < n and i <= reach:
#         if i > last_reach:
#             res += 1
#             last_reach = reach
#         reach = max(reach, i + nums[i])
#         i += 1
#     print(-1 if reach < (n - 1) else res)
