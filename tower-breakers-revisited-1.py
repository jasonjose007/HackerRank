# Tower Breakers, Revisited!
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys


def solve():
    data = sys.stdin.read().split()
    if not data:
        return

    max_h = 1000001
    spf = list(range(max_h))
    for i in range(2, 1001):
        if spf[i] == i:
            spf[i * i : max_h : i] = [i] * ((max_h - 1 - i * i) // i + 1)

    it = iter(data)
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it))
        xor_sum = 0
        for _ in range(n):
            x = int(next(it))
            cnt = 0
            while x > 1:
                x //= spf[x]
                cnt += 1
            xor_sum ^= cnt
        out.append("1" if xor_sum else "2")

    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    solve()