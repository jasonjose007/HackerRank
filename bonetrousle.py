# Bonetrousle
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    t = int(input_data[0])
    idx = 1
    out = []

    for _ in range(t):
        n = int(input_data[idx])
        k = int(input_data[idx + 1])
        b = int(input_data[idx + 2])
        idx += 3

        min_sum = b * (b + 1) // 2
        max_sum = b * (2 * k - b + 1) // 2

        if n < min_sum or n > max_sum:
            out.append("-1")
        else:
            rem = n - min_sum
            d = rem // b
            r = rem % b

            # First (b - r) elements get shifted by d
            # Last r elements get shifted by d + 1
            res = [str(i + d) for i in range(1, b - r + 1)] + \
                  [str(i + d + 1) for i in range(b - r + 1, b + 1)]
            
            out.append(" ".join(res))

    print("\n".join(out))

if __name__ == '__main__':
    solve()