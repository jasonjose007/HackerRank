# The Longest Common Subsequence
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    
    a = [int(x) for x in data[2:2+n]]
    b = [int(x) for x in data[2+n:2+n+m]]
    
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        ai = a[i-1]
        dp_i = dp[i]
        dp_prev = dp[i-1]
        for j in range(1, m + 1):
            if ai == b[j-1]:
                dp_i[j] = dp_prev[j-1] + 1
            else:
                val1 = dp_prev[j]
                val2 = dp_i[j-1]
                dp_i[j] = val1 if val1 > val2 else val2
                
    i = n
    j = m
    lcs = []
    while i > 0 and j > 0:
        if a[i-1] == b[j-1]:
            lcs.append(a[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] >= dp[i][j-1]:
            i -= 1
        else:
            j -= 1
            
    lcs.reverse()
    print(*(lcs))

if __name__ == '__main__':
    solve()