# CamelCase
# Platform: HackerRank
# Difficulty: Easy
# Topics: Algorithms

import sys

def main():
    s = sys.stdin.read().strip()
    if not s:
        return
    print(1 + sum(1 for c in s if c.isupper()))

if __name__ == '__main__':
    main()