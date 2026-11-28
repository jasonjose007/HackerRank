# Anagram
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys
from collections import Counter


def anagram(s: str) -> int:
    n = len(s)
    if n % 2 != 0:
        return -1
    mid = n // 2
    c1 = Counter(s[:mid])
    c2 = Counter(s[mid:])
    return sum((c1 - c2).values())


def main() -> None:
    data = sys.stdin.read().split()
    if not data:
        return
    q = int(data[0])
    out = []
    for i in range(1, q + 1):
        out.append(str(anagram(data[i])))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()