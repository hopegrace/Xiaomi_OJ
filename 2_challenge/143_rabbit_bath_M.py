# -*- coding: UTF-8 -*-
# description:小米兔每天都要去公共浴室洗澡，但是有时候公共浴室人太多，需要排队，小米兔想知道它什么时候能洗澡，你可以帮忙算算要多久才能洗完澡吗？
#             公共浴室最多可同时容纳n个人洗澡，每个人洗澡的时间为k分钟，多余的人只能在外面排队等候。（ps：保证不会有插队现象出现）
#             小米兔在第a时刻准备好去公共浴室洗澡，问小米兔什么时候才能洗完澡(初始状态：公共浴室为空）。
#             注意：如果有和小米兔同一时刻去公共浴室的。小米兔排到该时刻全部人的后面。（因为小米兔会礼让）
#
# example: input:2 5 3                     (第一行三个整数n,k,q, 且1≤n≤100,1≤k≤50,1≤q≤1e5)
#                1 1 2 1 3 1               (第二行q组整数(每组两个整数x，y代表在x时刻有y人去澡堂洗澡，1≤x≤1e5,1≤y≤100）)
#                4                         (第三行一个整数a，表示小米兔a时刻准备去洗澡)
#
#          output:12   (输出小米兔洗完澡的时刻，每组输出占一行。)


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""

# 1.使用append而不是使用+=来加速，因为+=是要返回一个新的list
# 2.在循环里面尽量不要访问对象的属性，而是使用变量存储，如append1 = wait.append,可以加速
# 3.注意切片带来的影响，切片虽然是生成一个新的list，但是是浅层复制。
# 4.del，remove比切片效率高

from collections import defaultdict


def solution(line):
    line = line.strip().split(";")
    n, k, q = [int(x) for x in line[0].split()]

    arrival = [int(i) for i in line[1].split()]
    arrival_dict = defaultdict(lambda: 0)
    for arrival_time, arrival_num in zip(arrival[::2], arrival[1::2]):
        arrival_dict[arrival_time] = arrival_num

    last = int(line[2])
    arrival_dict[last] += 1   # 小米兔到达

    wait, wash = [], []
    time = 1
    while True:
        while wash and time - wash[0][1] == k:  # wait:arrival_time,start_wash_time
            wash.pop(0)

        current_arrival = arrival_dict[time]  # i 时刻到达的人数
        while time <= last and current_arrival:
            wait.append([time, -1])
            current_arrival -= 1

        while len(wash) < n and wait:
            wait[0][1] = time
            wash.append(wait.pop(0))

        if time > last and not wash and not wait:
            break
        time += 1

    return time


test1 = "2 5 3;1 1 2 1 3 1;4"
print(solution(test1))   # 12
test2 = "21 9 10;6501 70 6526 79 6585 63 6650 6 6696 82 6724 62 6816 96 6859 28 6896 92 6901 3;6655"
print(solution(test2))   # 6664


# # 提交版本，问题：Python耗时过多
#
# from collections import defaultdict
#
# n, k, q = [int(x) for x in input().strip().split()]
#
# arrival = [int(i) for i in input().strip().split()]
# arrival_dict = defaultdict(lambda: 0)
# for arrival_time, arrival_num in zip(arrival[::2], arrival[1::2]):
#     arrival_dict[arrival_time] = arrival_num
#
# last = int(input())
# arrival_dict[last] += 1   # 小米兔到达
#
# wait, wash = [], []
# time = 1
# append1 = wait.append
# append2 = wash.append
#
# while True:
#     while wash and time - wash[0][1] == k:  # wait:arrival_time,start_wash_time
#         del wash[0]
#
#     current_arrival = arrival_dict[time]  # i 时刻到达的人数
#     while time <= last and current_arrival:
#         append1([time, -1])
#         current_arrival -= 1
#
#     while len(wash) < n and wait:
#         wait[0][1] = time
#         append2(wait[0])
#         del wait[0]
#
#
#     if (not wash) and (not wait) and time > last:
#         break
#     time += 1
#
# print(time)


# # C++ 版本

# #include <bits/stdc++.h>
#
# using namespace std;
#
# vector<int> arrival(1e5+1, 0);
#
# struct people{
#     int arrival_time, start_wash_time;
#     people(int a, int b): arrival_time(a), start_wash_time(b) {}
# };
#
# int main(){
#     int n, k, q;
#     cin >> n >> k >> q;
#     for(int i = 0; i < q; i++) {
#         int x, y;
#         cin >> x >> y;
#         arrival[x] += y;
#     }
#     int last;
#     cin >> last;
#     arrival[last]++;
#     int time = 1;
#     queue<people> wash, wait;
#     for(;; time++){
#
#         while(!wash.empty() && time - wash.front().start_wash_time == k) wash.pop();
#         int num = arrival[time];
#         while(time <= last && num--) wait.push(people(time, -1));
#         while(wash.size() < n && !wait.empty()) {
#             wait.front().start_wash_time = time;
#             wash.push(wait.front());
#             wait.pop();
#         }
#         if(time > last && wash.empty() && wait.empty()) break;
#     }
#     cout << time << endl;
# }


