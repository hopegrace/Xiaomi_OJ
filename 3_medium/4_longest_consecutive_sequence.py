# description:输入一个乱序的数列，输出其中最长连续数列长度，要求算法复杂度为 O(n) 。
# example: input:54,55,300,12,56
#          output:3

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""
# 一种方法是排序后遍历，找到最长的连续部分，时间复杂度为O(NlogN)，空间复杂度为O(1)。
# 另外一种方法是转为集合，将所有数转入集合中，然后再遍历，就能O(1)的判断一个数是否在集合中，所以可以一个个向上或者向下检查。
#  为了避免之后重复检查，每查到一个数，就可以从集合中移除。这样，遇到一个数，都检查它的上下边界，就能找出最长的连续数列。
#  时间复杂度为O(N)，因为我们不会检查不存在于数组中的数，而存在数组的数也只会检查一次。空间复杂度为O(N)。


def solution(line):
    numbers = [int(x) for x in line.split(",")]
    number_set = set(numbers)
    max_res = 0
    for number in numbers:
        tmp = number
        res = 0
        while tmp in number_set:
            number_set.remove(tmp)
            tmp += 1
            res += 1

        tmp = number - 1
        while tmp in number_set:
            number_set.remove(tmp)
            tmp -= 1
            res += 1

        max_res = max(res, max_res)
    return str(max_res)


test1 = "100,4,200,1,3,2"
print(solution(test1))  # 五个test的结果分别为4,2,1,5,6

test2 = "54,55,300,12"
print(solution(test2))

test3 = "1"
print(solution(test3))

test4 = "5,4,3,2,1"
print(solution(test4))

test5 = "1,2,3,4,5,6"
print(solution(test5))
