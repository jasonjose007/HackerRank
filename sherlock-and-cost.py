# Sherlock and Cost
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys


def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        b = [int(x) for x in data[idx:idx + n]]
        idx += n
        dp0 = 0
        dp1 = 0
        for i in range(1, n):
            prev_b = b[i - 1]
            cur_b = b[i]
            ndp0 = max(dp0, dp1 + prev_b - 1)
            ndp1 = max(dp0 + cur_b - 1, dp1 + abs(cur_b - prev_b))
            dp0, dp1 = ndp0, ndp1
        out.append(str(max(dp0, dp1)))
    sys.stdout.write('\n'.join(out) + '\n')


if __name__ == '__main__':
    solve()