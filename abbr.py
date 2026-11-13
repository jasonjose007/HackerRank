# Abbreviation
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def abbreviation(a, b):
    n, m = len(a), len(b)
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = True

    for i in range(n):
        for j in range(m + 1):
            if not dp[i][j]:
                continue
            
            # If a[i] is lowercase, we can always delete it
            if a[i].islower() and j <= m:
                dp[i + 1][j] = True
            
            # If a[i] matches b[j] (either exact uppercase or upper of lowercase)
            if j < m and a[i].upper() == b[j]:
                dp[i + 1][j + 1] = True

    return "YES" if dp[n][m] else "NO"

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    q = int(input_data[0])
    idx = 1
    out = []
    for _ in range(q):
        a = input_data[idx]
        b = input_data[idx + 1]
        idx += 2
        out.append(abbreviation(a, b))
    print('\n'.join(out))

if __name__ == '__main__':
    main()