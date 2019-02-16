# -*- coding: UTF-8 -*-
# description: 实现一个算法，可以进行任意非负整数的加减乘除组合四则运算。注意运算符的优先级。
#
# example: input:3 + 5 （输入为一行算式，使用空格分隔数字与运算符。数字为任意非负整数，运算符为+ - * /，不考虑括号。）
#          output:8 （输出算式的结果。如果是小数，向下取整（包含中间步骤结果）。如果出现“除0异常”，输出err）


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):  # 用栈来实现

    def priority(op1, op2):
        if op1 in ['*', '/'] and op2 in ['+', '-']:
            return True
        else:
            return False

    calculate_dict = {
        '+': lambda x1, x2: x2 + x1,  # 之所以是x2在前，是因为两次pop相当于反向取出最后两个数据
        '-': lambda x1, x2: x2 - x1,
        '*': lambda x1, x2: x2 * x1,
        '/': lambda x1, x2: x2 // x1 if x1 != 0 else 'err'  # 由于是非负数之间的除法，向下取整可直接用//
    }

    formula = [x for x in line.split()]
    symbols = ['+', '-', '*', '/']

    formula_suffix = []  # 由中缀表达式变为后缀表达式
    tmp_stack = []
    for item in formula:
        if item not in symbols:
            formula_suffix.append(item)
        elif len(tmp_stack) == 0:
            tmp_stack.append(item)
        elif priority(item, tmp_stack[-1]):
            tmp_stack.append(item)
        else:
            while tmp_stack and not priority(item, tmp_stack[-1]):
                formula_suffix.append(tmp_stack.pop())
            tmp_stack.append(item)
    while tmp_stack:
        formula_suffix.append(tmp_stack.pop())

    cal_stack = []  # 计算后缀表达式的结果
    for item in formula_suffix:
        if item not in symbols:
            cal_stack.append(int(item))
        else:
            res = calculate_dict[item](cal_stack.pop(), cal_stack.pop())
            if res == 'err':
                return 'err'
            else:
                cal_stack.append(res)

    return str(cal_stack[0])


test1 = '3 + 5'
print(solution(test1))  # 依次为8 17 0 err 1838.

test2 = '12 + 45 / 9'
print(solution(test2))

test3 = '1 / 2'
print(solution(test3))

test4 = '1 / 0'
print(solution(test4))

test5 = '12 + 34 * 56 - 78'
print(solution(test5))
