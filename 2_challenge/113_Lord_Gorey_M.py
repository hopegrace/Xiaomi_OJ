# -*- coding: UTF-8 -*-
# description: 黑暗女王希尔瓦娜斯将高弗雷复活为被遗忘者的一员。这个时候的高弗雷，已经完全没有生前的样子，看起来阴险又狡诈，
#              言语不再有任何礼节性的修饰，时常将恶毒的语言挂在嘴上，谈及自己的过去，满满的只有怨恨。
#              高弗雷当然不愿意臣服于希尔瓦娜斯，但是为了达成毫无察觉的背叛，他需要证明自己的“忠诚”——前去摧毁联盟第七军团的据点。
#
#               第七军团的据点有数不清的敌人，高弗雷拿着一把附魔火枪，射出的子弹会在敌人间跳跃，一发子弹就能对所有敌人造成2点伤害，
#               如果该子弹导致了任意敌人死亡（即血量小于等于0），该子弹还会再次对所有敌人造成2点伤害，直到没有新的敌人死亡为止。
#               那么，高弗雷需要打出几颗子弹才能消灭所有敌人呢？
#
# example: input:1 12 3 6 10    (输入是每个敌人的血量，用空格分开，回车结束。0<敌人的数量<=10000; 0<敌人的血量<=10^9)
#          output:2   (输出是一个数字，是高弗雷最少需要打出的子弹的个数)


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""

def solution(line):
    blood = [int(x) for x in line.split(" ")]
    blood.sort()

    frequency = (blood[-1] + 1) // 2 + 1   # 总共需要这么多次-2伤害
    additional = set()
    for item in blood:
        additional.add((item + 1) // 2)

    return frequency - len(additional)  # 有additional次数的-2伤害是由敌人死亡造成的


test = "1 12 3 6 10"
print(solution(test))  # 2

test2 = "76 75 33 17 77 6 66 89 40 82 20 46"
print(solution(test2))  # 35
