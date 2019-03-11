# description: 有N*M的一个矩阵，小米兔从矩阵左上角的第一个位置开始顺时针从外向里走，很快就走遍了所有的位置，
#              可是小米兔想知道自己走过的轨迹，你能告诉小米兔它走过的轨迹吗？

# example: input:3 3  ( 第1行是2个整数，分别代表N和M的值，第2到N+1行，表示N*M的矩阵中的每一行。)
#                1 2 3
#                4 5 6
#                7 8 9
#
#          output:1 2 3 6 9 8 7 4 5 (输出为一个字符串，由小米兔走过的位置的值组成，用空格分隔。)


"""
@param string line 为一个测试用例
@return string 处理后的结果
"""


def solution(line):
    matrix = []
    for line in line.split("\n"):
        line = line.strip().split()
        matrix += [line]
    N = int(matrix[0][0])
    M = int(matrix[0][1])
    matrix.pop(0)

    direction = 0
    cycle = 0
    res = []

    while len(res) < (N * M):
        tmp = direction % 4
        if tmp == 0:
            for j in range(cycle, M - cycle):
                res.append(matrix[cycle][j])
        elif tmp == 1:
            for i in range(cycle + 1, N - cycle):
                res.append(matrix[i][M - cycle - 1])
        elif tmp == 2:
            for j in range(M - cycle - 2, cycle - 1, -1):
                res.append(matrix[N - cycle - 1][j])
        elif tmp == 3:
            for i in range(N - cycle - 2, cycle, -1):
                res.append(matrix[i][cycle])
            cycle += 1
        direction += 1
    res = " ".join([str(x) for x in res])
    return res


test = "3 4\n1 2 3 4\n 4 5 6 7\n 7 8 9 10"
print(solution(test))



# # 提交版本
# import sys
#
# matrix=[]
# for line in sys.stdin:
#     line = line.strip().split()
#     matrix += [line]
#
# N = int(matrix[0][0])
# M = int(matrix[0][1])
# matrix.pop(0)
#
# direction = 0
# cycle = 0
# res = []
#
# while len(res) < (N * M):
#     tmp = direction % 4
#     if tmp == 0:
#         for j in range(cycle, M - cycle):
#             res.append(matrix[cycle][j])
#     elif tmp == 1:
#         for i in range(cycle + 1, N - cycle):
#             res.append(matrix[i][M - cycle - 1])
#     elif tmp == 2:
#         for j in range(M - cycle - 2, cycle - 1, -1):
#             res.append(matrix[N - cycle - 1][j])
#     elif tmp == 3:
#         for i in range(N - cycle - 2, cycle, -1):
#             res.append(matrix[i][cycle])
#         cycle += 1
#     direction += 1
# res = " ".join([str(x) for x in res])
# print(res)