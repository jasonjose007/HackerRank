# Zero-Move Nim
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    g = int(input_data[0])
    idx = 1
    out = []

    for _ in range(g):
        n = int(input_data[idx])
        idx += 1
        xor_sum = 0
        for _ in range(n):
            p = int(input_data[idx])
            idx += 1
            if p % 2 == 1:
                xor_sum ^= p + 1
            else:
                xor_sum ^= p - 1

        if xor_sum != 0:
            out.append("W")
        else:
            out.append("L")

    print("\n".join(out))


if __name__ == "__main__":
    solve()