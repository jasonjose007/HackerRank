# Taum and B'day
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        b = int(data[idx])
        w = int(data[idx + 1])
        bc = int(data[idx + 2])
        wc = int(data[idx + 3])
        z = int(data[idx + 4])
        idx += 5
        cost = b * min(bc, wc + z) + w * min(wc, bc + z)
        out.append(str(cost))
    print("\n".join(out))

if __name__ == "__main__":
    solve()