# Mark and Toys
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys


def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    k = int(data[1])
    prices = [int(x) for x in data[2:2 + n]]
    prices.sort()

    count = 0
    for p in prices:
        if k >= p:
            k -= p
            count += 1
        else:
            break

    print(count)


if __name__ == '__main__':
    solve()