# -*- coding: UTF-8 -*-
# description: 每次打ADC时，都会纠结是出『暗影战斧』还是『破甲弓』，现在给出护甲的计算公式、当前英雄等级、对方英雄护甲，
#              计算出买哪个装备单次攻击伤害更高.
#
#               首先,我们计算对方英雄的护甲值： 护甲值 = 原始护甲值 - 护甲穿透。
#               然后，我们计算护甲可以提供的伤害减免，伤害减免公式为： 伤害减免 = (护甲值) / (602 + 护甲值)。
#               英雄的攻击力为： 100 + 装备攻击
#               实际英雄受的伤害为： 攻击力 x (100% - 伤害减免)
#             暗影战斧 axe +85 物理攻击 唯一被动（切割）：增加（100+英雄等级*10）点护甲穿透
#             破甲弓 bow +80 物理攻击 唯一被动：增加 45% 护甲穿透（实际穿透的护甲值为 原始护甲 x ( 1 - 45%) ）
#
# example: input:15 100    (一行数字，每行两个数（空格隔开）：x y（己方英雄等级 对方英雄护甲）。)
#          output:axe        (如果『暗影战斧』伤害更高，那么输出 axe，如果『破甲弓』更优秀，那么输出 bow。 如果两个一样，那么输出 same。)


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    a, b = line.split()
    a = int(a)
    b = int(b)

    hux = b - (100 + a * 10)
    x = (100 + 85) * (1 - hux / (602 + hux))
    huy = b * (1 - 0.45)
    y = (100 + 80) * (1 - huy / (602 + huy))

    if x > y:
        return "axe"
    elif x < y:
        return "bow"
    else:
        return "same"


test1 = "15 100"
print(solution(test1))  # 分别输出axe,bow,axe

test2 = "0 1000"
print(solution(test2))

test3 = "0 200"
print(solution(test3))
