# -*- coding: UTF-8 -*-
# description: 德州扑克是风靡全球的一种扑克游戏。扑克有四种花色，分别为黑桃（S）、红桃（H）、梅花（C）、方片（D）。
#              每种花色有13张牌，从小到大分别为2、3、4、5、6、7、8、9、10、J、Q、K、A。
#              考虑德州扑克中的如下三种牌形：
#              1.同花顺（Straight Flush）：同一花色，并且连续的五张牌。 例如：{SK SQ SJ S10 S9} 对于连续的五张牌，有一个特例，
#                即 {A、2、3、4、5} 也算作连续的五张牌。但 {K、A、2、3、4}，{Q、K、A、2、3}，{J、Q、K、A、2} 不算作连续的五张牌。
#              2.同花（Flush）：同一花色但不连续的五张牌。 例如：{H10 H7 H4 H3 H2}
#              3.顺子（Straight）：连续但不是同一花色的五张牌。 例如：{SA H2 D3 C4 D5}
#
#              这三种牌形的大小关系是：顺子 < 同花 < 同花顺。 现在，我们为了游戏的趣味性，在扑克中加入了5张魔术牌（用M表示），
#              你可以将每张魔术牌变成你想要的任何一张牌。 你从牌堆里随机抽了五张牌，请你给出最大可能的牌形。如果三种牌形都无法组成，请输出GG。
#
#         输入格式：一行字符串，表示使用空格分隔的五张牌，每张牌由花色与点数组成(或使用M来表示魔术牌)。
#         输出格式：对于单组输入，输出一行字符串，表示能够组成的最大牌形。 只有Flush、Straight、Straight Flush、GG四种结果。
#
# example: input:M SA H2 D3 C4
#          output:Straight


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    cards = [x for x in line.strip().split()]


    pass


test1 = "H10 H7 H4 H3 H2"
print(solution(test1))  # Flush

test2 = "M SA H2 D3 C4"
print(solution(test2))  # Straight

test3 = "M M M M D4"
print(solution(test3))  # Straight Flush

test4 = "S8 HJ DA H8 H5"
print(solution(test4))  # GG