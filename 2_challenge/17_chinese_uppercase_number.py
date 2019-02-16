# -*- coding: UTF-8 -*-
# description: 实现一个算法，可以将小写数字转换成大写数字。
#
# example: input:8900000000 （输入一个整数。范围在0～450亿之间。）
#          output:捌拾玖亿元整 （输出对应的大写数字，以“元整”结尾。大写数字要符合汉语读写习惯）


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    number_array = [int(x) for x in list(line)]
    uppercase_cn = ["零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖"]
    count_labels = ['', '拾', '佰', '仟']
    count_units = ['', '万', '亿']
    suffix = '元整'

    res = []
    if number_array == [0]:
        res.insert(0, uppercase_cn[0])
    else:
        while number_array:
            process_part, number_array = number_array[-4:], number_array[:-4]
            tmp = ''.join([uppercase_cn[x] + (y if x != 0 else '') for x, y in list(zip(process_part[::-1], count_labels))[::-1]])
            tmp = tmp.rstrip('零').replace('零零零', '零').replace('零零', '零')
            pop_unit = count_units.pop(0)
            if tmp:
                tmp += pop_unit
                res.append(tmp)

    res.insert(0, suffix)
    return ''.join(res[::-1])


test1 = '0'
print(solution(test1))  # 零元整

test2 = '5'
print(solution(test2))  # 伍元整

test3 = '233'
print(solution(test3))  # 贰佰叁拾叁元整

test4 = '1001'
print(solution(test4))  # 壹仟零壹元整

test5 = '40607'
print(solution(test5))  # 肆万零陆佰零柒元整

test6 = '8900000000'
print(solution(test6))  # 捌拾玖亿元整
