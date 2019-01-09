# description:有 500 个小孩围成一圈，编号从 1 到 500，从第一个开始报数：1，2，3，1，2，3，1，2，3，……每次报到 3 的小孩退出。
#              问第 n 个被淘汰的小孩，在最开始 500 人里是的编号是几？
# example: input:206  (正整数N，表示要计算的为第 N 个淘汰的小孩的编号，0 < N <= 500)
#          output:176 (第N个淘汰的小孩的编号)


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    n = int(line)
    kid_list=[(x+1) for x in range(500)]
    k = 0
    while n>=0:
        for j in range(500):
            if kid_list[j]>0:
                k=k+1
                if k % 3 == 0:
                    kid_list[j] = -1
                    k = 0
                    n -= 1
                    if n==0:
                        return j+1