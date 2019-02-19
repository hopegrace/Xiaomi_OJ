# -*- coding: UTF-8 -*-
# description: 有一类正整数我们叫做归一数字，对于任意一个归一数字 N，满足以下特性：
#              N的每一位的平方和组成一个数，新数字的平方和再组成一个新数字，如此往复运算，直到最终结果为1。
#              若一个数字能最终归一成 1，则该数字为归一数字，否则不是归一数字。
#              举例： 82可以分解为8^2+2^2=68，68继续分解为6^2+8^2=100，100可以分解为1^2+0^2+0^2=1。所以82可以归一。
#
# example: input:50      (一个正整数N（0<N<100000000）)
#          output:false     (输出N是否为归一数的判断结果，若是则返回'true'，否则返回'false'（均为字符串）)


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    N = int(line)
    number_set = set()

    while N not in number_set:
        number_set.add(N)
        N = sum([int(digit)**2 for digit in str(N)])

    return 'true' if N == 1 else 'false'


test1 = '82'
print(solution(test1))  # true

# 关键在于查找的终止条件。
# 在leetcode中称为Happy Number,称对于任何一个正整数，算各个数位上数字的平方和，以此构成新的数字，然后继续求平方和，一直算下去。
# 若经过若干次运算后结果收敛到1，则该数字为Happy Number，否则就是Happy Number。Leetcode题目描述中给出了一个关键的条件：
#    不是Happy Number的数在经过多次运算后会从某个数开始陷入循环。
# 这句话实际上给出了终止查找的条件。此外，非快乐数有一个特点，循环的数字中必然出现4。https://en.wikipedia.org/wiki/Happy_number
#
# 有个暴力的方法：设一个数字N有m位，则它的平方和不可能超过9^2 + 9^2 + ... + 9^2 (一共m个) = 81*m
#               对任意的m>=4,有81*m < 10^(m-1) < N (因为N有m位)。
#               所以，任何大于等于1000的数字，它的各个数位上的平方和形成的新数字都比它本身小，从而不断变小，直到1000以内。
#               而1000以内的数字，即三位数，经过暴力计算，所有的要么归于1，要么无限循环，而循环里面必然有一个4.
#
# 注：更多数学上的证明或者描述可参看以下两篇文章：
#    (1) http://math.bard.edu/student/pdfs/alison-mutter.pdf
#    (2) https://pdfs.semanticscholar.org/bc54/f5857ba3b538dfe6876e922ae75597cc080d.pdf
