# Yet Another Minimax Problem
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    a = [int(x) for x in input_data[1 : n + 1]]

    k = -1
    for bit in range(29, -1, -1):
        has_0 = False
        has_1 = False
        for x in a:
            if (x >> bit) & 1:
                has_1 = True
            else:
                has_0 = True
            if has_0 and has_1:
                break
        if has_0 and has_1:
            k = bit
            break

    if k == -1:
        print(0)
        return

    s0 = [x for x in a if not ((x >> k) & 1)]
    s1 = [x for x in a if (x >> k) & 1]

    root = [None, None]
    for y in s1:
        curr = root
        for bit in range(k, -1, -1):
            b = (y >> bit) & 1
            if curr[b] is None:
                curr[b] = [None, None]
            curr = curr[b]

    ans = float("inf")
    for x in s0:
        curr = root
        res = 0
        for bit in range(k, -1, -1):
            b = (x >> bit) & 1
            if curr[b] is not None:
                curr = curr[b]
            else:
                res |= 1 << bit
                curr = curr[1 - b]
        if res < ans:
            ans = res

    print(ans)


if __name__ == "__main__":
    solve()