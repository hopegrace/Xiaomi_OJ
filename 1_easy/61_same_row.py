# description:给一个由 0 和 1 组成的矩阵，其中有两行相同，仅通过遍历找到相同的行。输出行数。
#              如： 1,0,0,1,0 0,1,1,0,0 1,0,0,1,0 0,0,1,1,0 0,1,0,0,0
#              输出重复的行号为 1 和 3（行号从1开始）
# example: input:1,0,0,1,0;0,1,1,0,0;1,0,0,1,0;0,0,1,1,0;0,1,0,0,0
#               (一个字符串，表示由0和1组成的矩阵，使用;分隔行，使用,分隔每行内的元素。矩阵必然存在且只有一对重复的行。)
#          output:1,3 (使用,分隔的两个整数，表示重复的两行。)


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
   str_list = line.split(';')
   length = len(str_list)
   for i in range(length):
       for j in range(i+1,length):
           if str_list[i]==str_list[j]:
               return str(i+1)+','+str(j+1)

