# Swap Permutation
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    k = int(input_data[1])

    MOD = 1000000007

    if n == 1:
        print("0 1")
        return

    # 1. Compute S1: Exact k adjacent swaps
    # dp[j] = number of permutations of length current_n with j inversions
    dp = [0] * (k + 1)
    dp[0] = 1

    for i in range(2, n + 1):
        pref = [0] * (k + 2)
        s = 0
        for j in range(k + 1):
            s = (s + dp[j]) % MOD
            pref[j + 1] = s

        new_dp = [0] * (k + 1)
        for j in range(k + 1):
            low = j - i + 1
            if low < 0:
                low = 0
            new_dp[j] = (pref[j + 1] - pref[low]) % MOD

        dp = new_dp

    s1 = 0
    for j in range(k, -1, -2):