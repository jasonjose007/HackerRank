# Sansa and XOR
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys


def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    t = int(data[idx])
    idx += 1
    out = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        if n % 2 == 0:
            out.append("0")
        else:
            ans = 0
            for i in range(0, n, 2):
                ans ^= int(data[idx + i])
            out.append(str(ans))
        idx += n
    print("\n".join(out))


if __name__ == "__main__":
    solve()