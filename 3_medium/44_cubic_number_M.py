# -*- coding: UTF-8 -*-
# description: 给出一个数字N(0<=N<=1e6),将N写成立方数和的形式，求出需要的最少的立方数个数。
#              举例： 假设N=17，可得1+8+8=17，最少需要3个立方数，则输出3.
#                    假设N=28，可得1+1+1+1+8+8+8=28，需要7个立方数，又得1+27=28，需要2个立方数，所以最少立方数为2，则输出2
#
# example: input:17  (一个正整数N(0≤N≤1e6))
#          output:3  (需要的最少的立方数个数（整型）)


"""
@param string line 为单行测试数据
@return string 处理后的结果
"""

# 动态规划


def solution(line):
    N = int(line.strip())
    if N == 0 or N == 1:
        return 1

    dp = [float("inf")] * (N + 1)
    dp[0] = 0
    m = int(pow(N, 1 / 3))
    for i in range(1, m + 1):
        for v in range(i**3, N + 1):
            dp[v] = min(dp[v], dp[v - i**3] + 1)
    return dp[N]


test1 = "1"
print(solution(test1))  # 1

test2 = "17"
print(solution(test2))  # 3

test3 = "28"
print(solution(test3))  # 2


# # #  C++ 版本
#
#include <bits/stdc++.h>
#
# using namespace std;
#
# int main() {
#     string s;
#     vector<int> dp(1000003, 1000003);
#     dp[0] = 0;
#     int tmp_max = 0;
#     while(getline(cin, s)) {
#         int N = stoi(s);
#         if(N <= tmp_max) cout << dp[N] << endl;
#         else {
#             int m = pow(N, 1.0 / 3);
#             for(int i = 1; i <= m; ++ i) {
#                 for(int j = max(tmp_max, i * i * i); j <= N; ++ j) {
#                     dp[j] = min(dp[j], dp[j - i * i * i] + 1);
#                 }
#             }
#             cout << dp[N] << endl;
#             tmp_max = N;
#         }
#     }
# }

