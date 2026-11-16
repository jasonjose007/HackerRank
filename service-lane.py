# Service Lane
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys


def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    t = int(data[1])
    width = list(map(int, data[2:2 + n]))
    idx = 2 + n
    out = []
    for _ in range(t):
        i = int(data[idx])
        j = int(data[idx + 1])
        idx += 2
        out.append(str(min(width[i:j + 1])))
    print('\n'.join(out))


if __name__ == '__main__':
    main()