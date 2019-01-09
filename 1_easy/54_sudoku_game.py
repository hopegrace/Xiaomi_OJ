# description:数独盘面是个九宫，每一宫又分为九个小格。在这八十一格中给出一定的已知数字和解题条件，利用逻辑和推理，在其他的空格上填入1-9的数字。
#             使1-9每个数字在每一行、每一列和每一宫中都只出现一次，所以又称"九宫格"。
#             一个合法的数独棋盘满足上面的条件，即1-9每个数字在每一行、每一列和每一宫中都只出现一次，而并不要求一定有解。
#             请判断给出的数独棋盘是否合法。
# example: input:5,3,-,6,-,-,-,9,8 -,7,-,1,9,5,-,-,- -,-,-,-,-,-,-,6,- 8,-,-,4,-,-,7,-,- -,6,-,8,-,3,-,2,- -,-,3,-,-,1,-,-,6 -,6,-,-,-,-,-,-,- -,-,-,4,1,9,-,8,- 2,8,-,-,-,5,-,7,9
#                从左到右从上到下，使用空格分隔每一宫，使用逗号分隔每一格，没有数字则代表该格为空
#          output:true (true或false表示该数独棋盘是否合法)


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    str_list = line.split()
    for i in range(9):
        str_list[i] = str_list[i].split(',')
        for j in range(9):
            if str_list[i][j] != '-':
                str_list[i][j] =int(str_list[i][j])
        if len([x for x in str_list[i] if type(x)==int])!= len(set([x for x in str_list[i] if type(x)==int])): # 判断每一宫
            return 'false'
    matrix = [['-' for i in range(9)] for j in range(9)]  # 整体转成二维矩阵表示
    for i in range(9):
        for j in range(9):
            matrix[(i//3)*3+(j//3)][(i%3)*3+(j%3)]=str_list[i][j]

    for i in range(9):
        if len([x for x in matrix[i] if type(x) == int]) != len(set([x for x in matrix[i] if type(x) == int])): # 判断每一行
            return 'false'
        if len([x for x in matrix[:][i] if type(x) == int]) != len(set([x for x in matrix[:][i] if type(x) == int])): # 判断每一列
            return 'false'

    return 'true'
