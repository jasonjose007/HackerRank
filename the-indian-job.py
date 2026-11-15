# The Indian Job
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    T = int(input_data[0])
    idx = 1
    out = []

    for _ in range(T):
        N = int(input_data[idx])
        G = int(input_data[idx + 1])
        idx += 2

        A = [int(x) for x in input_data[idx : idx + N]]
        idx += N

        S = sum(A)
        if S > 2 * G:
            out.append("NO")
            continue
        if S <= G:
            out.append("YES")
            continue

        dp = 1
        for x in A:
            dp |= dp << x

        low = S - G
        high = G

        mask = ((1 << (high - low + 1)) - 1) << low
        if dp & mask:
            out.append("YES")
        else:
            out.append("NO")

    print("\n".join(out))


if __name__ == "__main__":
    solve()