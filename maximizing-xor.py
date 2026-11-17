# Maximizing XOR
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def maximizingXor(l, r):
    q = l ^ r
    return (1 << q.bit_length()) - 1

if __name__ == '__main__':
    lines = sys.stdin.read().split()
    if lines:
        l = int(lines[0])
        r = int(lines[1])
        print(maximizingXor(l, r))