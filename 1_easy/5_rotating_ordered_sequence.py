# description:给出一个有序数列随机旋转之后的数列，如原有序数列为：[0,1,2,4,5,6,7] ，旋转之后为[4,5,6,7,0,1,2]。
#             假定数列中无重复元素，且数列长度为奇数。 求出旋转数列的中间值。如数列[4,5,6,7,0,1,2]的中间值为4。
# example: input:4,5,6,7,0,1,2
#          output:4

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    num_list = [int(x) for x in line.strip().split(',')]
    length = len(num_list)
    location = length - 1  # 表示未移动
    if num_list[0] >= num_list[-1]:
        for i in range(1, length):
            if num_list[i] < num_list[i - 1]:
                location = length - 1 - i  # location表示最后一位在原来的顺序中的位置
                break

    if location >= ((length - 1) // 2):
        return num_list[(length - 1) // 2 * 3 - location]  # (length-1)-return_location = location - (length-1)//2
    else:
        return num_list[(length - 1) // 2 - location - 1]  # return_location-0 = (length-1)//2 - (location+1)

