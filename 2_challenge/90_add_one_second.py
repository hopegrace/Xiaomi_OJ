# -*- coding: UTF-8 -*-
# description: 在某个古老的神秘国度，有一位长者，他有一项特殊的能力，那就是能为自己的生命加一秒，与此同时，周围的人会相应的-1s
#              每当电子表的小时数与分钟数一样时(24小时制，00:00:00~23:59:59)，那1分钟的最后1秒将会消失不见
#              也就是说，比如，06:06:58的下一秒将是06:07:00
#              现在，与长者共处了一段时间后，对于你来说，你度过的时间究竟是多少
#
# example: input:2d06 05 24    (现实世界中经过的时间，格式为{天}d{小时} {分} {秒}，时分秒补足2位)
#          output:2d06 04 30   (对于你而言的时间，格式同输入。)


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    input_time = line.split(" ")
    days = int(input_time[0][:-3])
    hours = int(input_time[0][-2]) * 10 + int(input_time[0][-1])
    minutes = int(input_time[1][0]) * 10 + int(input_time[1][1])
    seconds = int(input_time[2][0]) * 10 + int(input_time[2][1])

    d_second = days * 24
    h_second = hours + 1 if minutes > hours or (minutes == hours and seconds == 59) else hours
    total_loss = d_second + h_second

    res = (days * 24 + hours) * 3600 + minutes * 60 + seconds - total_loss
    res_days = res // (3600 * 24)
    res_hours = (res - res_days * (3600 * 24)) // 3600
    res_minutes = (res - res_days * (3600 * 24) - res_hours * 3600) // 60
    res_seconds = res - res_days * (3600 * 24) - res_hours * 3600 - res_minutes * 60


    output = [str(res_days) + 'd' + ('0' + str(res_hours) if res_hours < 10 else str(res_hours)),
              '0' + str(res_minutes) if res_minutes < 10 else str(res_minutes),
              '0' + str(res_seconds) if res_seconds < 10 else str(res_seconds)]
    return " ".join(output)


test1 = "2d06 05 24"
print(solution(test1))  # 2d06 04 30

test2 = "2d06 06 59"
print(solution(test2))  # 2d06 06 04

test3 = "52d05 01 46"
print(solution(test3))  # 52d04 40 53
