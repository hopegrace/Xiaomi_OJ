# 输入：两个非负数a和b, 以空格分开，a和b保证小于2^32
# 输出：一行数据处理的结果，也即a+b的结果

# example: input:233 666
#          output:899

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    a, b = line.strip().split()
    return str(int(a) + int(b))
