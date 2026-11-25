# Encryption
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import math
import sys


def solve():
    raw_input = sys.stdin.read()
    s = "".join(raw_input.split())
    if not s:
        return

    L = len(s)
    r = math.floor(math.sqrt(L))
    c = math.ceil(math.sqrt(L))
    if r * c < L:
        r += 1

    words = []
    for col in range(c):
        words.append(s[col::c])

    print(" ".join(words))


if __name__ == "__main__":
    solve()