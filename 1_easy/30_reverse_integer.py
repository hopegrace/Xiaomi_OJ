# description:输入32位无符号整数，输出它的反向位。 例，输入4626149（以二进制表示为00000000010001101001011011100101），
#             返回2808701440（以二进制表示为10100111011010010110001000000000）。
# example: input:4626149 （一个无符号32位整数字符串）
#          output:2808701440 （一个无符号32位整数，为输入整数的反向位）

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    num = bin(int(line))
    num_list = list(num)[2:][::-1]
    for i in range(len(num_list),32):
        num_list.append('0')
    num_str=''.join(num_list)
    return int(num_str,2)











