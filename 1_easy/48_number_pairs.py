# description:有一串可能含重复数字的列表，例如 N = {4,13,5,6,35,85,3}，对于任意 A ∈ N，B ∈ N, 使 A+B = 10 或 |A-B| = 10；
#             即两数之和为 10 或两数之差的绝对值为 10。找出所有满足条件的数字对 {A,B} 的个数。(A, B的顺序与原始数组保持一致)
#
# example: input:13,3,6,8,12,4,45,56,66,16 (一行文本由英文逗号分隔，如 6,4,16)
#          output:4 （满足条件的数字对的个数）

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    num_list =[int(x) for x in line.split(',')]
    length =len(num_list)
    count=0
    for i in range(length):
        for j in range(i+1,length):
            if num_list[i]+num_list[j]==10 or abs(num_list[i]-num_list[j])==10:
                count += 1
    return count
