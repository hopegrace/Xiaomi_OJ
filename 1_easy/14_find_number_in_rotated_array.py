# description:假设一个有序的数组，经过未知次数的旋转（例如0 1 2 4 5 6 7 被旋转成 4 5 6 7 0 1 2），
#             从中查找一个目标值，如果存在，返回其下标，不存在，返回-1。注：假设数组无重复数字
# example: input:4,5,6,7,0,1,2 6 （输入一个有序经过旋转的数组和要查找的目标数字，数组中各数字用“逗号”分隔，数组和目标数字用“空格”分隔）
#          output:2 （一个整数，表示该目标数字的下标（不存在返回-1））

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    num_list, target= line.strip().split(' ')
    num_string=''.join(num_list.split(','))
    return num_string.find(target)






