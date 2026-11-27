# Xor-sequence
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def prefix_xor(n):
    if n < 0:
        return 0
    r = n & 7
    if r == 0 or r == 1:
        return n
    if r == 2 or r == 3:
        return 2
    if r == 4 or r == 5:
        return n + 2
    return 0

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    q = int(data[0])
    out = []
    idx = 1
    for _ in range(q):
        l = int(data[idx])
        r = int(data[idx + 1])
        idx += 2
        out.append(str(prefix_xor(r) ^ prefix_xor(l - 1)))
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()