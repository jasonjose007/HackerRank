# Introduction to Nim Game
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    g = int(next(it))
    results = []
    for _ in range(g):
        n = int(next(it))
        nim_sum = 0
        for _ in range(n):
            nim_sum ^= int(next(it))
        results.append("First" if nim_sum != 0 else "Second")
    print("\n".join(results))

if __name__ == "__main__":
    solve()