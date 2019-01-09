# description:给出一个数组，数组中的数字皆为正整数，除了某一个数字，其他的数字都会出现三次。 找出那个只出现一次的数。

# example: input:5,1,4,5,4,5,4 (3n+1的正整数数组，使用逗号(,)分隔(n>0))
#          output:1 (单独出现的数字)


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    num_list = [int(x) for x in line.strip().split(',')]
    length = len(num_list)
    for i in range(length):
        if len(set(num_list[0:i]+num_list[i+1:])) == ((length-1)//3):
            return num_list[i]
