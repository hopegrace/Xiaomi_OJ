# -*- coding: UTF-8 -*-
# description: 给定两个数组，由数字0-9组成的，长度分别为a和b，需要用a、b两个数组中的数字组合得到长度为k(k<=a+b)的正整数，
#           输出所有可能的组合中数值最大的一个（原同一数组中的数字顺序不能改变）
#        输入格式：a、b 数组中的数字间用逗号隔开，两个数组以及k之间用空格隔开，如：1,3,4,5,1,2 8,9,1 5，
#                 其中a = [1,3,4,5,1,2]，b = [8,9,1]，k = 5. 数组a, b元素个数不大于20.
#        输出格式：长度为k的所有组合中数值最大的整数，如：95121
#                 从a或b中取数的时候需保证a，b 内部的顺序不变，如第一个数取到b中的9，那么b中只有1可以后续取用；
#                 第二个数取到a中的5，则a中还剩下1,2可以后续取用。
# example: input:6,3,8,9,4,6,0 3,5,7 6
#          output:963570


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    def max_array(array, k):  # 取得一个数组中k位长的最大数字
        drop = len(array) - k
        res = []
        for digit in array:
            while drop and res and res[-1] < digit:
                # 如果res栈顶元素比array[i]小，则不断弹出栈顶元素，直到1.栈空，2.剩下的数组元素不足以填满栈至k
                res.pop()
                drop -= 1
            res.append(digit)
        return res[:k]

    def merge(array_a, array_b):
        res = []
        while array_a or array_b:
            if array_a > array_b:
                res += [array_a[0]]
                array_a = array_a[1:]
            else:
                res += [array_b[0]]
                array_b = array_b[1:]
        return res
        # 可以简化为一行：return [max(array_a,array_b).pop(0) for _ in array_a+array_b]
        # python中，列表比较是基于字典序(也成为字母序)，可参考https://ask.helplib.com/others/post_12803474
        # 故max返回的是第一个值比较大的序列，再用pop返回该序列第一个元素,同时该序列变短，然后继续比较下去

    array_1, array_2, k = line.split()
    array_1 = [int(x) for x in array_1.split(',')]
    array_2 = [int(x) for x in array_2.split(',')]
    k = int(k)
    res = []

    for i in range(max(0, k - len(array_2)), min(k, len(array_1)) + 1):
        max_1 = max_array(array_1, i)  # 从array_1中选择i个数使得最大
        max_2 = max_array(array_2, k - i)  # 从array_2中选择k-i个数使得最大
        candidate = merge(max_1, max_2)  # 获得合并的k位数使得最大
        res = max(candidate, res)    # 所有合并的k位数中最大的k位数

    return "".join([str(x) for x in res])


test1 = "6,3,8,9,4,6,0 3,5,7 6"
print(solution(test1))  # 963570

test2 = "2,6,8,4,3 6,9,2,5 3"
print(solution(test2))  # 985

test3 = "3,7,2 7,9,5,1 7"
print(solution(test3))  # 7953721
