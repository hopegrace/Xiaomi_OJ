# -*- coding: UTF-8 -*-
# description: 用一个数组表示一群正在排队的小学生，每个小学生用一对整数H,K来表示。
#              H表示这个小学生的身高，K表示这个小学生前面应该有K个人的身高>=他。
#              写一个算法，对给出的一组小学生进行排序，使每个人都符合他的(H,K)描述。
#
# example: input:6 7 0 4 4 7 1 5 0 6 1 5 2 （输入为一组整数，以空格分隔：第1个数字表示小学生的数量 n；
#                                             从第2个数字起，后续的数字两两一组，分别代表每个小学生的H和K的值）
#          output:5 0 7 0 5 2 6 1 4 4 7 1 （对小学生进行排序，每个小学生对应的H和K值为一组，按组输出，数字间使用空格分隔）


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    number_array = [int(x) for x in line.split()]
    child_num = number_array.pop(0)
    children = [[H, K] for H, K in zip(number_array[::2], number_array[1::2])]

    children.sort(key=lambda x: x[0], reverse=True)  # 按高度从高到低排
    i = 0
    while i < child_num - 1:
        j = i
        while i < child_num - 1 and children[i][0] == children[i + 1][0]:
            i += 1
        children[j:(i + 1)] = sorted(children[j:(i + 1)], key=lambda x: x[1])  # 相同高度的“前面比他高的人数”小的站前面
        # 注意：children[j:(i+1)].sort(key=lambda x: x[1])是无效的，因为切片会进行浅拷贝，得到一个新列表。
        # sort会对拷贝的版本产生影响，但原来的children序列并不会发生改变。
        # 如果没有切片,children.sort()的话,children才会发生相应的改变。
        # 而sorted会产生一个全新的列表，只有通过赋值对原来的列表产生影响。
        i += 1

    res = []  # 如果从高到低排序，每次把当前的插入，那低的一定不会影响高的“前面比他高的人数”
    for child in children:
        res.insert(child[1], child)

    res = [str(i) for k in res for i in k]
    return " ".join(res)


def solution2(line):
    number_array = [int(x) for x in line.split()]
    child_num = number_array.pop(0)
    children = [[H, K] for H, K in zip(number_array[::2], number_array[1::2])]

    children_dict = {}
    height_list = []
    for i in range(child_num):
        child = children[i]
        if child[0] in children_dict:
            children_dict[child[0]] += [(child[1], i)]  # 注意，列表添加元组,会自动将元组拆包来添加,而不是作为一个整体添加
        else:
            children_dict[child[0]] = [(child[1], i)]
            height_list.append(child[0])

    res = []
    height_list.sort(reverse=True)
    for height in height_list:
        children_dict[height].sort()
        for item in children_dict[height]:
            res.insert(item[0], children[item[1]])

    res = [str(i) for k in res for i in k]
    return " ".join(res)


test = '6 7 0 4 4 7 1 5 0 6 1 5 2'
print(solution(test))  # 输出为'5 0 7 0 5 2 6 1 4 4 7 1'
print(solution2(test))

