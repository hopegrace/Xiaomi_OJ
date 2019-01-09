# 输入：多个数字，每个数字以空格分开。数字数量 N < 20，输入数字的最大值小于256.
# 输出：只出现过唯一一次的数字

# description:给出N个数字。其中仅有一个数字出现过一次，其他数字均出现过两次，找出这个出现且只出现过一次的数字。要求时间和空间复杂度最小
# example: input:10 10 11 12 12 11 16
#          output:16

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    input_nums = [int(x) for x in line.strip().split()]
    output=0
    for i in range(len(input_nums)):
        output = output^input_nums[i]
    return str(output)

# 异或规律 x^0=x,x^x=0，1^2^...^n^...^n^...^1000=1^2^...^1000^(n^n)=1^2^...^1000 (无论这两个n在何处)
