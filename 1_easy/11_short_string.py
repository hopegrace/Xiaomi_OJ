# description:给定任意一个较短的子串，和另一个较长的字符串，判断短的字符串是否能够由长字符串中的字符组合出来，且长串中的每个字符只能用一次。
# example: input:uak areuok （一行数据包括一个较短的字符串和一个较长的字符串，用一个空格分隔，如： ab aab bb abc aa cccc uak areuok）
#          output:true （如果短的字符串可以由长字符串中的字符组合出来，返回字符串 “true”，否则返回字符串 "false"，注意返回字符串类型而不是布尔型。）

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    string_list = line.strip().split()
    short_string = string_list[0]
    long_string = string_list[1]

    for item in short_string:
        location = string_list[1].find(item)
        if location == -1:
            return 'false'
        else:
            string_list[1] = long_string[:location] + long_string[location + 1:]

    return 'true'

