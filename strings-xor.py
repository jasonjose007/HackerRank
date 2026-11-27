# XOR Strings
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def main():
    lines = sys.stdin.read().split()
    if len(lines) >= 2:
        s = lines[0]
        t = lines[1]
        print("".join("1" if a != b else "0" for a, b in zip(s, t)))

if __name__ == "__main__":
    main()