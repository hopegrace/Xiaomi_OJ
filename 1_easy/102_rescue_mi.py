# description: 给定一个只包含小写字母的字符串，现在我 mi 被众友商品牌的字符串围困在其中，
#              需要我们将字符串中的 mi 全部移除然后输出，保证最后输出的字符串中没有 "mi"。
# example: input:samsungmimiapple chuizimmmiioppo (一行数据包含一个字符串，长度 <= 100000，字符串仅包含小写字母。)
#          output:samsungapple  chuizimoppo (输出处理后的字符串)


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    stack = []
    for item in line:
        if item == 'i' and len(stack) > 0 and stack[-1] == 'm':
            stack.pop()
        else:
            stack.append(item)
    return ''.join(stack)

