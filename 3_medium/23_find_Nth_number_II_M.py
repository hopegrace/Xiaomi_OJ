# -*- coding: UTF-8 -*-
# description: 假如有一组字符串符合如下规律：
#                                     S1=1
#                                     S2=12
#                                     S3=123
#                                     ......
#                                     S18=123456789101112131415161718
#              即对于Sn来说，就是将1到n的数字拼接在一起。
#              现在将所有的字符串拼接在一起，组成一个无限长的字符串S=1121231234⋯12345678910111213⋯
#              找出该字符串的第N位置处的数字是多少。
#
# example: input:6  （一个整数（1<整数<10^15）,表示N）
#          output:3  （一个整数，表示该位上的数字是多少）


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    def get_res2(n):
        if n <= 9:
            return str(int(n))
        tmp_sum = 9
        scale = 9
        d = 1
        while n >= tmp_sum:
            if n == tmp_sum:
                return str(9)
            scale *= 10
            d += 1
            tmp_sum += (scale * d)  # 1*9 + 2*90 + 3*900 +...

        tmp_sum -= (scale * d)
        n = n - tmp_sum
        y = int(scale / 9 + n / d - 1)
        # scale/9 确定是从1、10、100、1000···中哪个开始数起,
        # n/d确定剩余的个数可以放多少个位数为d位的数,
        # 减1是因为10**(d-1)这个开头的数字也算在里面,也占了d位的空间
        res2 = int(n % d)
        return str(y + 1)[res2 - 1] if res2 else str(y % 10)

    def get_res1(N):
        start = 1
        end = 10
        d = 1
        sums = 0
        while True:
            sums += d * (start + 1 + end) * (end - start) / 2 - (10**d - 1) / 9 * (end - start)  # 说明见下面
            if sums >= N:
                break
            start *= 10
            end *= 10
            d += 1

        if sums == N:
            res1 = end
        else:
            sums -= d * (start + 1 + end) * (end - start) / 2 - (10**d - 1) / 9 * (end - start)
            n = start
            while True:
                sums += d * (n + 1) - (10**d - 1) / 9
                if sums >= N:
                    break
                n += 1
            sums -= d * (n + 1) - (10**d - 1) / 9
            res1 = N - sums

        return res1

    return get_res2(get_res1(int(line)))


test1 = "1"
print(solution(test1))  # 1

test2 = "6"
print(solution(test2))  # 3

test3 = "7"
print(solution(test3))  # 1

test4 = "1000"
print(solution(test4))  # 4

# 对于Sn来说，它的长度依赖于n,且其为一个特殊的等差数列，即公差d不断变大。设n为k位数，则有：
# n:1~9 10~99 100~999 ... 10**k~(10**(k+1) - 1)
# d: 1    2      3    ...      k+1
# 设输入的数字为N,设g(x)=sum(len(S_i),i=1:x),则需要找到使得g(x)<N的最大x，从而确定第N个数字在S_(x+1)的res1=N-g(x)位置处。
# 设对于某个数y,其在Sn的位置是f(y)，那么要求出f(y)<res1的最大y,从而得出res2=res1-f(y),res2表示的就是整数y+1的第res2位置。
# 该位置上的数字即为输出。简而言之，分为两步骤：
#       1.找到使得g(x)<N的最大x,从而得知N位置在S(x+1)上，res1=N-g(x)
#       2.找到使得f(y)<res1的最大整数y,从而得知N位置在整数y+1上，res2=res1-f(y)。
# res2即为整数y+1的res2位，由于是从0开始计数，所以用减1来索引得到。

# 问题在于g(x)和f(y)很难给出一个通用的公式，我们可以通过累加不断逼近，以此来求解res和res2。
# 更快速的方法可以参考 C++二分快速版本https://blog.csdn.net/FlushHip/article/details/86644049
#                  C++ 简单版本的方法可以参考https://blog.csdn.net/linruier2017/article/details/83996819


################################# 关键步骤数学说明：########################################
# 对于 sums += d * (start + 1 + end) * (end - start) / 2 - (10**d - 1) / 9 * (end - start)，
# 每次迭代累加的是从S_start到S_(end-1)的所有的数字位数，从而推断出上述g(x)的x是多少位的数字，
# 后面的sums += d * (n + 1) - (10**d - 1) / 9则是确定x具体是哪个数字，即确定N位置在S_(x+1)上。
# 取一般情况，start=10**(d-1),end=10**d。设想S_start到S_(end-1)堆成一个梯形，左边对齐，这里取d=4做一个示意：

# S_1000 = 123456789101112...99100101...999  1000  (空格仅为了区分)
# S_1001 = 123456789101112...99100101...999  10001001
# S_1001 = 123456789101112...99100101...999  100010011002
#   ········
# S_9999 = 123456789101112...99100101...999  10001001100210031004....99989999

# 可以看到空格左边的是一个矩形，每一行的数字个数是一致的，空格右边的部分形成一个梯形，每一行的数字个数按4递增。
# 设单位元为d,将求得右边梯形的面积乘以d,即可求得里面的数字个数，然后再加上左边的矩形中的数字个数，即：
# C_all=d*(上底+下底)*高/2 + C_rectangle
#      =d*（1 + end-start)*(end-start)/2 + C_rectangle
# 而C_rectangle每一行的数字个数都一样，从而有：
# C_rectangle=C_line * 行数 = C_line * (end-start)
# 接下来算一行多算的数字个数，即C_line,1~9每个数字1位，10~99每个数字2位，100~999每个数字3位，
# 一直下去，到start-1,即10**(d-1)-1这个数，有d-1位，而长度为d-1位的数字一共有10**(d-1) - 10**(d-2)个，从而
# C_line = 1*9 + 2*(99-10+1) + 3*(999-100+1) + ··· + (d-1)*(10**(d-1) - 10**(d-2))
#        = 1*9 + 2*90 + 3*900 + ··· + (d-1)*9*(10**(d-2))
# 则 10*C_line = 1*9*10 + 2*9*100 + 3*9*1000 +···+ (d-1)*9*(10**(d-1))
# 则 C_line = (10*C_line-C_line)/9 = (-9-90-900-···-9*(10**(d-2)) + (d-1)*9*(10**(d-1)))/9
#           = -1-10-100-···-(10**(d-2)) + (d-1)*(10**(d-1))
#           = (d-1)*(10**(d-1)) - (10**(d-1)-1)/9
# 所以C_rectangle = (d-1)*(10**(d-1))*(end-start) - (10**(d-1)-1)/9*(end-start)
# 所以C_all = d*（1 + end-start)*(end-start)/2 + C_rectangle
#          = d*（1 + end-start)*(end-start)/2 + (d-1)*(10**(d-1))*(end-start) - (10**(d-1)-1)/9*(end-start)
#          = d*（1 + end-start)*(end-start)/2 + d*(10**(d-1))*(end-start)-10**(d-1)*(end-start) - (10**(d-1)-1)/9*(end-start)
#          = d* (1 + end-start + 2*(10**(d-1)))*(end-start)/2 - 10**(d-1)*(end-start) - (10**(d-1)-1)/9*(end-start)
#          = d* (1 + end-start + 2*start)*(end-start)/2 - 10**(d-1)*(end-start) - (10**(d-1)-1)/9*(end-start)
#          = d* (1 + end+start)*(end-start)/2 - (10**d-1)/9*(end-start)

# 类似的，后面的算单个Sn的长度，即令end=start+1即可，从而sums += d * (n + 1) - (10**d - 1) / 9



##################################### Xiaomi OJ 在线提交版本#############################
# import sys
#
#
# def get_res2(n):
#     if n <= 9:
#         return str(int(n))
#     tmp_sum = 9
#     scale = 9
#     d = 1
#     while n >= tmp_sum:
#         if n == tmp_sum:
#             return str(9)
#         scale *= 10
#         d += 1
#         tmp_sum += (scale * d)  # 1*9 + 2*90 + 3*900 +...
#
#     tmp_sum -= (scale * d)
#     n = n - tmp_sum
#     y = int(scale / 9 + n / d - 1)
#     res2 = int(n % d)
#     return str(y + 1)[res2 - 1] if res2 else str(y % 10)
#
#
# def get_res1(N):
#     start = 1
#     end = 10
#     d = 1
#     sums = 0
#     while True:
#         sums += d * (start + 1 + end) * (end - start) / 2 - (10 ** d - 1) / 9 * (end - start)  # 说明见下面
#         if sums >= N:
#             break
#         start *= 10
#         end *= 10
#         d += 1
#
#     if sums == N:
#         res1 = end
#     else:
#         sums -= d * (start + 1 + end) * (end - start) / 2 - (10 ** d - 1) / 9 * (end - start)
#         n = start
#         while True:
#             sums += d * (n + 1) - (10 ** d - 1) / 9
#             if sums >= N:
#                 break
#             n += 1
#         sums -= d * (n + 1) - (10 ** d - 1) / 9
#         res1 = N - sums
#
#     return res1
#
#
# for line in sys.stdin:
#     line = line.strip()
#     N = int(line)
#     print(get_res2(get_res1(int(line))))
