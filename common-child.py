# Common Child
# Platform: HackerRank
# Difficulty: Medium
# Topics: Algorithms

import sys


def commonChild(s1, s2):
    # Pre-filter characters that are not in both strings
    # This preserves the LCS while potentially reducing work,
    # though the bit-parallel algorithm is O(N * M / 64) anyway.
    # Note: filtering characters might change indices, but LCS only depends on order of matching characters.
    # Any character not present in the other string can never be part of a common child.
    set1 = set(s1)
    set2 = set(s2)
    common_chars = set1 & set2

    s1 = [c for c in s1 if c in common_chars]
    s2 = [c for c in s2 if c in common_chars]

    if not s1 or not s2:
        return 0

    # Ensure s1 is the shorter (or equal) string to minimize bit length
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    # Precompute match bitmasks for each character in s1
    match = {}
    for i, c in enumerate(s1):
        match[c] = match.get(c, 0) | (1 << i)

    v = 0
    for c in s2:
        m = match.get(c, 0)
        x = m | v
        y = (v << 1) | 1
        v = x & (x ^ (x - y))

    return bin(v).count("1")


def main():
    input_data = sys.stdin.read().split()
    if len(input_data) >= 2:
        s1 = input_data[0]
        s2 = input_data[1]
        print(commonChild(s1, s2))


if __name__ == "__main__":
    main()