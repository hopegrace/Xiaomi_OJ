# -*- coding: UTF-8 -*-
# description: 给出平面坐标系上四个点的坐标，判断这四个点能不能连成正方形。
#
# example: input:0,0;1,1;1,0;0,1    (一行字符串，包含4组平面坐标，每组坐标形如x,y，坐标与坐标间由英文分号隔开，如：0,0;1,1;1,0;0,1)
#          output:1                 (1或0，1表示可以表示正方形，0表示不能组成正方形)


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    points = [point.split(",") for point in line.split(";")]
    points = [[int(points[i][0]), int(points[i][1])] for i in range(4)]

    distance = []
    for i in range(4):
        j = i + 1
        while j <= 3:
            distance.append((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)
            j += 1

    distance.sort()
    for i in range(1, 4):
        if distance[i] == distance[0]:
            continue
        else:
            return 0
    if distance[-1] == distance[-2] and distance[-1] > distance[0]:
        return 1
    else:
        return 0


test1 = '0,0;1,1;1,0;0,1'
print(solution(test1))
