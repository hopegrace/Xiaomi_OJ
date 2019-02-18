# -*- coding: UTF-8 -*-
# description: 对于给定的算术表达式，按规则输出计算结果，仅包含加法和大小判断。
#
# example: input:972919822976663297>74058  (一行字符串，用加号、大于、小于( + < > )连接的两个不限大小的非负整数)
#          output:Y                        (当符号为 + 时, 计算两个数相加的和, 并以字符串格式返回；
#                                           当符号为 < 时, 如果左数小于右数, 返回大写字母字符 Y, 否则返回大写字母字符 N；
#                                           当符号为 > 时, 如果左数大于右数, 返回大写字母字符 Y, 否则返回大写字母字符 N。)


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    def bigger(item1, item2, len1, len2):
        if len1 == len2:
            for i in range(len1):
                if int(item1[i]) == int(item2[i]):
                    continue
                else:
                    return int(item1[i]) > int(item2[i])
            return 'equal'  # 长度相等，所有元素也相等，则两者相等
        else:
            return len1 > len2

    def add(item1, item2, len1, len2):
        list1 = [int(x) for x in list(item1)][::-1]
        list2 = [int(x) for x in list(item2)][::-1]
        list2.extend([0] * (len1 - len2))

        for i in range(len1):
            element_add = list1[i] + list2[i]
            if element_add < 10:
                list1[i] = element_add
            else:
                list1[i] = element_add - 10
                if i + 1 == len1:
                    list1.append(1)
                else:
                    list1[i + 1] += 1

        return "".join([str(x) for x in list1[::-1]])

    # import re
    # num1,num2=re.split(r'[+><]',line)
    # sign=line[len(num1)]

    for item in ["+", ">", "<"]:
        tmp = line.find(item)
        if tmp >= 0:
            num1 = line[:tmp]
            num1_len = len(num1)
            num2 = line[(tmp + 1):]
            num2_len = len(num2)
            sign = item
            break

    if sign == "+":
        if num1_len > num2_len:
            return add(num1, num2, num1_len, num2_len)
        else:
            return add(num2, num1, num2_len, num1_len)
    else:
        res = bigger(num1, num2, num1_len, num2_len)
        if res == 'equal':
            return 'N'
        elif sign == ">":
            return 'Y' if bigger(num1, num2, num1_len, num2_len) else 'N'
        else:
            return 'N' if bigger(num1, num2, num1_len, num2_len) else 'Y'


test1 = '972919822976663297>74058'
print(solution(test1))  # 输出为Y

test2 = '875098336507333719633571722631534917759993913379786689>53558270653237768027942884431075534537929401567824882097903948774409200'
print(solution(test2))  # 输出为N

test3 = '7625022925148127196027859399571498914361+790786706794530'
print(solution(test3))  # 输出为7625022925148127196027860190358205708891

test4 = "91605925589308617120639+44791376625729389745455"
print(solution(test4))  # 输出为136397302215038006866094

test5 = "22906433671447571628000741785817076923549016768967401245935474350289424<22906433671447571628000741785817076923549016768967401245935474350289424"
print(solution(test5))  # 输出为N

test6 = "266501993977907789993240011668803136337150448+135100221616274963452811197217591461222234550"
print(solution(test6))  # 输出为401602215594182753446051208886394597559384998

test7 = "99970+999"
print(solution(test7))  # 输出为1000969
