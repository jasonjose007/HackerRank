# The Great XOR
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys


def main():
    data = sys.stdin.read().split()
    if not data:
        return
    q = int(data[0])
    out = []
    for i in range(1, q + 1):
        x = int(data[i])
        out.append(str((1 << x.bit_length()) - 1 - x))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()