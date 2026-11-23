# Mandragora Forest
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys


def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        h = sorted(map(int, data[idx:idx + n]))
        idx += n
        rem = sum(h)
        best = rem
        for i in range(1, n):
            rem -= h[i - 1]
            val = (i + 1) * rem
            if val > best:
                best = val
        out.append(str(best))
    sys.stdout.write('\n'.join(out) + '\n')


if __name__ == '__main__':
    solve()