# description:将 M 个同样的糖果放在 N 个同样的篮子里，允许有的篮子空着不放，共有多少种不同的分法？
#             比如，把 7 个糖果放在 3 个篮子里，共有 8 种分法（每个数表示篮子中放的糖果数，数的个数为篮子数）： 1 1 5 1 2 4 1 3 3 2 2 3 2 5 0 3 4 0 6 1 0 7 0 0
#             注意：相同的分布，顺序不同也只算作一种分法，如 7 0 0、0 7 0 和 0 0 7 只算作一种。
# example: input:7,3 （输入包含二个正整数 M 和 N，以(,)分开，M 表示有几个同样的糖果，N 表示有几个同样的篮子 M与N范围：1 <= M，N <= 100。）
#          output:8 （输出一个正整数 K，表示有多少种分法。）

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    num_candy, num_basket= line.strip().split(',')
    def f(n,m):
        if m==1 or n==0:
            return 1
        if m>n:
            return f(n,n)
        return f(n,m-1) + f(n-m,m)
    return f(int(num_candy),int(num_basket))




