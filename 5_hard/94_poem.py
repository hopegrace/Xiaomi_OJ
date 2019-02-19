# -*- coding: UTF-8 -*-
# description: 给出一个字符集，用这字符集里的字符写出所有长度为n且文中不包含丑陋的词句的诗篇。算出满足条件的诗篇有多少。
#              输入包含一个数字n (1<=n<=1000000000)，
#                     一个字符串s表示字符集(只包含a~z中若干个不重复的小写字母,且按照字典序增序给出，如"ace", "uvw"等)，
#                     一个字符串t表示丑陋的词句（保证t中的字符均存在于所给的字符集中）且(1<=|t|<=50)。

# example: input:3;ab;aa
#                3;ab;aaa
#                4;ab;ab
#          output:5                   (由于答案可能非常之巨大，方便起见，将最终结果对1000000007取模输出)
#                 7
#                 5
#          样例解释:三个样例中的字符集均为{a, b},可组成长度为3的诗篇有8篇: {aaa, aab, abb, aba, bbb, bba, baa, bab}
#                 其中不含子串"aa"的有5篇,不含子串"aaa"的有7篇,故前两个样例的结果分别是5和7.
#                 可组成长度为4的诗篇有16篇:
#                 {aaaa,aaab,aaba,abaa,aabb,abab,abba,abbb,bbbb,bbba,bbab,babb,bbaa,baba,baab,baaa}
#                 其中不含子串"ab"的有5篇,故第三个样例的输出是5.

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


# 设character_set有m个字符,长度为n的poem就有m^n篇，因为每个位置都有m个选择。
# 设ugly_string长为t,那就相当于有t个字符捆绑在一起，剩下n-t个位置可以任意放字符，然后排列组合，一共有(n-t+1)*(m^(n-t))种。
# 从而不包含ugly_string的一共有 m^n - (n-t+1)*(m^(n-t))
# 但是有一个问题是重复的情形，比如说第一个样例，实际上只有3种含有ugly_string的情况，但是按上面的方法计算会得到有4种。
# 这是因为aa在a前面和后面是一样的，类似的第三个样例，ab在ab前面和后面是一样的。
#
# 目前的猜想是字符串循环导致重复情形被计算，即一个情形被算两次，要加上重复导致的，所以加上(n - (T + t) + 1) * (m**(n - t - T))
#
################################################################################################################
################ 该程序有问题，待改进，如无法修正，直接用树的方法构造含有ugly_string的poem，然后再用m^n减 ###################

def solution(line):
    def get_cycle(item):
        item_len = len(item)
        for i in range(1, item_len//2+1):
            if item_len % i == 0:
                for j in range(1, item_len // i + 1):
                    if item[:i] != item[i * j:i * (j + 1)]:
                        break
                    elif i * (j + 1) == item_len:
                        return i
                    else:
                        continue
        return item_len

    n, character_set, ugly_string = line.split(";")
    n = int(n)
    m = len(character_set)
    t = len(ugly_string)

    T = get_cycle(ugly_string)
    res = m**n - (n - t + 1) * (m**(n - t)) + (n - (T + t) + 1) * (m**(n - t - T))

    return int(res % 1000000007)

test1 = "3;ab;aa"
print(solution(test1))   # 5，7，5，13,15

test2 = "3;ab;aaa"
print(solution(test2))

test3 = "4;ab;ab"
print(solution(test3))

test4 = "4;ab;aaa"
print(solution(test4))

test5 = "4;ab;aaaa"
print(solution(test5))
