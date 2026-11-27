# Alice and Bob's Silly Game
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    g = int(data[0])
    ns = [int(x) for x in data[1:1 + g]]
    max_n = max(ns) if ns else 0
    if max_n < 2:
        sys.stdout.write("\n".join(["Bob"] * g) + "\n")
        return

    is_prime = bytearray([1]) * (max_n + 1)
    is_prime[0] = 0
    is_prime[1] = 0
    for i in range(2, int(max_n ** 0.5) + 1):
        if is_prime[i]:
            start = i * i
            is_prime[start::i] = bytearray((max_n - start) // i + 1)

    prefix = [0] * (max_n + 1)
    cnt = 0
    for i in range(2, max_n + 1):
        if is_prime[i]:
            cnt += 1
        prefix[i] = cnt

    out = ["Alice" if (prefix[n] & 1) else "Bob" for n in ns]
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    solve()