# Fibonacci Modified
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    t1, t2, n = map(int, data[:3])
    if n == 1:
        print(t1)
        return
    for _ in range(3, n + 1):
        t1, t2 = t2, t1 + t2 * t2
    print(t2)

if __name__ == "__main__":
    solve()