# -*- coding: UTF-8 -*-
# description: 后台对于每次请求服务都有一次服务质量评分告警，其数值 score 范围为 0~10,
#              比如：当服务出现抖动,延迟增大或者返回不合预期时，score 会增大，当服务延迟较小且返回正常时，score 会减小，
#              现在有一批某天的小爱服务日志，格式为：
#               id (每次请求 id ，全局唯一), start_time (服务开始时间，inclusive), end_time(服务结束时间,exclusive),
#               score(服务打分)， 后台系统的某一刻t的告警分数 total_socre为t时刻所有处于连接状态的服务分数之和.
#               为了计算简便， 已经将 start_time 与 end_time 转换为 unix timestamp 时间戳,
#               现在运维想从日志中找出一天中整个系统服务的告警分数 total_score 最大值, 要求申请的存储为常量.
#
# example: input:1 6 10 4 2 3 8 3 3 7 9 1 4 5 6 2 (输入多个以空格分隔的整数，每4个整数为一组（组数<10^7),
#                                                 这4个整数分别代表 id, start_time, end_time, score，其值均小于10^6)
#          output:8 (输出一个整数，表示 total_score 的最大值)


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    number_array = [int(x) for x in line.split(" ")]
    length = len(number_array)
    res = [0]*(10**6)

    for i in range(length//4):
        start_time = number_array[4*i+1]
        end_time = number_array[4*i+2]
        res[start_time] += number_array[4*i+3]
        res[end_time] -= number_array[4*i+3]

    for i in range(1,10**6):
        res[i] += res[i-1]  # 关键是理解这个，可以画一条时间轴，每个节点都有不同的高度，代表着score

    return max(res)




test1="1 6 10 4 2 3 8 3 3 7 9 1 4 5 6 2"
print(solution(test1))
