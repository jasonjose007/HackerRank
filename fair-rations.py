# Fair Rations
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys


def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    b = [int(x) for x in data[1:n + 1]]

    loaves = 0
    for i in range(n - 1):
        if b[i] % 2 != 0:
            b[i] += 1
            b[i + 1] += 1
            loaves += 2

    if b[-1] % 2 != 0:
        print("NO")
    else:
        print(loaves)


if __name__ == "__main__":
    solve()